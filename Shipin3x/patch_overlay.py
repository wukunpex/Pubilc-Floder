#!/usr/bin/python2.7

import abc
import sys
import subprocess
import shutil
import os
import datetime
import logging
from optparse import OptionParser

log = None


class OverlayTool:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def apply_patch(self):
        pass

    @abc.abstractmethod
    def remove_patch(self):
        pass


class intel_ucode(OverlayTool):

    def __init__(self):
        if 'linux' not in sys.platform:
            raise OSError('Cannot run this on a non-Linux OS')

        cpu_family = int(subprocess.check_output('lscpu | grep family | cut -d\':\' -f2', shell=True).lstrip().rstrip())
        cpu_model = int(subprocess.check_output('lscpu | grep Model: | cut -d\':\' -f2', shell=True).lstrip().rstrip())
        cpu_stepping = int(
            subprocess.check_output('lscpu | grep Stepping: | cut -d\':\' -f2', shell=True).lstrip().rstrip())

        log.info('Detected System Info - Family: {family:02}\tModel: {model:x}\tStepping: {stepping}'.format(
            family=cpu_family, model=cpu_model, stepping=cpu_stepping))
        self.processor_string = "{family:02}-{model:x}-{stepping:02}".format(family=cpu_family, model=cpu_model,
                                                                             stepping=cpu_stepping)
        # One location here to store variables for function calls
        self.staging_loc = '/tmp/{patch_filename}'.format(patch_filename=self.processor_string)
        self.original_patch = '/lib/firmware/intel-ucode/{patch_filename}'.format(patch_filename=self.processor_string)
        self.backup_filename = '/lib/firmware/intel-ucode/{patch_filename}_clean'.format(
            patch_filename=self.processor_string)

    def apply_patch(self, patch_dir=None):
        if patch_dir is None:
            log.error('Cannot patch without a supplied patch directory.')
            return 1
        if not os.path.exists(patch_dir):
            log.error('Patch directory does not exist.')
            return 1

        patch_pdb = [f for f in os.listdir(patch_dir) if '.pdb' in f]
        if len(patch_pdb) > 1:
            log.error('Multiple .pdb files located in the patch directory: {dir}'.format(dir=patch_dir))
        else:
            patch_pdb = os.path.join(patch_dir, patch_pdb[0])

        # Move the patch to a staging area and rename for consumption
        log.info('Moving patch file to staging area: {staging_loc}'.format(staging_loc=self.staging_loc))
        shutil.copy2(patch_pdb, self.staging_loc)

        # Backup the old patch file
        log.info('Backing up existing patch to {backup}'.format(backup=self.backup_filename))
        shutil.copy2(self.original_patch, self.backup_filename)

        # Copy the new patch from staging area to the patch location
        log.info('Loading new patch file from staging location to {path}'.format(path=self.original_patch))
        shutil.copy2(self.staging_loc, self.original_patch)

        # Load the new patch
        log.info('Executing patch update')
        subprocess.check_call('echo 1 > /sys/devices/system/cpu/microcode/reload', shell=True)
        return 0

    def verify(self, patch_rev=0):
        # Use lscpu to get the number of cores and then compare that against the number of cores on the input patch
        num_cores = int(
            subprocess.check_output('lscpu | grep ^CPU\\(s\\): | cut -d\':\' -f2', shell=True).lstrip().rstrip())
        num_cores_matching_patch = int(
            subprocess.check_output(
                'cat /proc/cpuinfo | grep {patch_rev} | cut -d\':\' -f2 | wc -l'.format(patch_rev=patch_rev),
                shell=True).lstrip().rstrip())

        if num_cores != num_cores_matching_patch:
            return 1
        else:
            return 0

    def remove_patch(self):
        log.info('Restoring the original patch from {path}'.format(path=self.backup_filename))
        shutil.copy2(self.backup_filename, self.original_patch)


class cpumcupdate(OverlayTool):

    def __init__(self):
        if 'win32' not in sys.platform:
            raise OSError('Cannot run this on a non-Windows OS')

        # One location here to store variables for function calls
        self.staging_loc = r'C:\temp\patch.inc'
        self.tool_location = 'C:\cpumcupdate'
        self.install_batch = os.path.join(self.tool_location, 'uninstall.bat')
        self.uninstall_batch = os.path.join(self.tool_location, 'uninstall.bat')

    def apply_patch(self, patch_dir=None):
        if patch_dir is None:
            log.error('Cannot patch without a supplied patch directory.')
            return 1
        if not os.path.exists(patch_dir):
            log.error('Patch directory does not exist.')
            return 1

        microcode_dat = None

        # Check for a microcode.dat file
        microcode_dat = [f for f in os.listdir(patch_dir) if 'microcode.dat' in f]
        if len(microcode_dat) > 1:
            log.info('Multiple .dat files located in the patch directory: {dir}'.format(dir=patch_dir))
        elif len(microcode_dat) == 0:
            log.info('No microcode.dat found, going to use .inc file and convert.')
        else:
            microcode_dat = os.path.join(patch_dir, microcode_dat[0])
            shutil.copy2(microcode_dat, self.tool_location)

        # If no microcode.dat was found, then let's create our own
        if not microcode_dat:
            patch_inc = [f for f in os.listdir(patch_dir) if '.inc' in f]
            if len(patch_inc) > 1:
                log.error('Multiple .inc files located in the patch directory: {dir}'.format(dir=patch_dir))
                return 1
            else:
                patch_inc = os.path.join(patch_dir, patch_inc[0])

            # Move the patch to a staging area
            log.info('Moving patch file to staging area: {staging_loc}'.format(staging_loc=self.staging_loc))
            shutil.copy2(patch_inc, self.staging_loc)

            # Convert to microcode.dat for cpumcupdate consumption
            import imp
            patchutil = imp.load_source('patchutil', r'C:\cpumcupdate\patchutil.py')
            mc = patchutil.Microcode()
            mc.load_inc_file(self.staging_loc)
            mc.save_dat_file(self.tool_location+r'\microcode.dat')
            # Copy the microcode.dat file to the patch location

        # Load the new patch
        log.info('Executing the patch update via cpumcupdate')
        subprocess.check_call(self.install_batch)
        return 0

    def verify(self, patch_rev=0):

        # We have to read the patch rev out of the registry for Windows
        import _winreg as reg
        registry = reg.ConnectRegistry(None, reg.HKEY_LOCAL_MACHINE)
        key = reg.OpenKey(registry, r'HARDWARE\DESCRIPTION\System\CentralProcessor')
        # Store all patch revisions for each core in this array
        patch_revisions = []

        # Loop through every subkey to read the patch off that core, a bit messy right now
        for dev in range(256):
            try:
                subkey_name = reg.EnumKey(key, dev)
                subkey = reg.OpenKey(key, subkey_name)
                patch_rev_packed = bytearray()
                patch_rev_packed.extend(reg.QueryValueEx(subkey, 'Update Revision')[0])
                patch_rev_packed.reverse()

                patch = ""
                for x in range(4):
                    patch += "{byte:02x}".format(byte=patch_rev_packed[x])
                patch_revisions.append(patch)
                print patch
            except WindowsError, e:
                pass

        # If we have more than 1 unique patch or the patch doesn't match what we expect, fail
        if patch_rev not in set(patch_revisions) or len(set(patch_revisions)) != 1:
            return 1
        else:
            return 0

    def remove_patch(self):
        log.info('Uninstalling the patch via cpumcupdate')
        subprocess.check_call(self.uninstall_batch, shell=True)


def setup_log(suffix=""):
    global log
    time = datetime.datetime.now()
    filename = "patch_overlay"
    logfile = "%s_%s%s.log" % (filename, time.strftime("%Y_%m_%d"), suffix)
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s', '%m-%d-%Y %H:%M:%S')
    log = logging.getLogger(logfile)
    log.setLevel(logging.DEBUG)
    loggerHandler = logging.FileHandler(logfile)
    loggerHandler.setFormatter(formatter)
    channelHandler = logging.StreamHandler()
    channelHandler.setFormatter(formatter)
    log.addHandler(loggerHandler)
    log.addHandler(channelHandler)


def main(argv):
    global log
    setup_log()
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)

    parser.add_option('-p', '--patch', action="store", dest="patch_rev", type='str',
                      help="Patch revision to go to.")

    parser.add_option('-v', '--verify', action="store", dest="verify",
                      help="Verify that current patch matches input patch")

    parser.add_option('-r', '--remove',
                      action="store_true", dest="remove",
                      help="Remove a loaded patch. If used with -p, will remove the patch after application.")

    (options, args) = parser.parse_args(argv)
    log.debug('Debug options: {options}'.format(options=options))

    # Get the proper patch tool
    if 'linux' in sys.platform:
        patch_tool = intel_ucode()
        patch_dir = r'/root/patches'
    elif 'win32' in sys.platform:
        patch_tool = cpumcupdate()
        patch_dir = r'C:\patches'

    # Parse the patch input to get the patch location
    if options.patch_rev:
        options.patch_rev = options.patch_rev.zfill(8)

        # Check for a production patch
        if int(options.patch_rev, 16) >> 31 == 1:
            log.error('This tool cannot be used without a production signed patch.')
            return 1

        patch_folder = os.path.join(patch_dir, 's_{patch_rev}__p_b7__PRODUCTION'.format(patch_rev=options.patch_rev))
        log.info('Patch files should be located in {dir}'.format(dir=patch_folder))
        ret = patch_tool.apply_patch(patch_folder)
        if ret == 0:
            log.info('Patch load successful, doing verification.')
        else:
            log.info('Error during patch load.')
            return 1
        ret = patch_tool.verify(options.patch_rev)
        if ret == 0:
            log.info('Patch verification successful.')
        else:
            log.error('Patch verification failed.')		
            return 1

    if options.verify:
        options.verify = options.verify.zfill(8)
        verification = patch_tool.verify(options.verify)

        if verification:
            log.error('Verification of patch failed.')
            return 1
        else:
            log.info('Patch verification successful.')

    if options.remove:
        patch_tool.remove_patch()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
