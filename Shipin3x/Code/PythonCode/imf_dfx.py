from falconvalley.fw.imf.commands import imf_helper_cmd    # imf_helper_cmd file contains wrapper functions for framework.
from falconvalley.fw.imf.parsers import imf_dfx_parser    # imf_dfx_parser contains parsers for dfx commands that have been converted to module functions.
from falconvalley.fw.imf.constants_tables import imfFunctions as FunctionName
from falconvalley.fw.imf.constants_tables import MailboxResultDict as mbStatCodes
from falconvalley.fw.imf import constants_tables as ct
from falconvalley.fw import fwUtils

import datetime
import os
import struct
import common

import components.dimmeeprom as spds
import falconvalley.sv.fnvUtils as fu

SMALL_PAYLOAD=1
LARGE_PAYLOAD=0
DWORDS_PER_64B = 64/4


_testName = "imf_dfx"
_logfile = _testName + ".log"
_log = common.toolbox.getLogger(_testName)
_log.setConsoleLevel(common.toolbox.INFO)
_log.setConsoleFormat('simple')
_log.setFile(_logfile, overwrite=True, dynamic=True)
_log.setFileFormat('time')
_log.setFileLevel(common.toolbox.INFO)

FW_CONFIG = {}
try:
	from common.pysv_config import CFG
	FW_CONFIG["project"] = CFG.baseaccess.project
except Exception:
	# assume older and not defined as elkvalley
	FW_CONFIG["project"] = "elkvalley"
FW_CONFIG["proj"] = "ekv"
if (FW_CONFIG["project"] == "barlowvalley"):
	FW_CONFIG["proj"] = "bwv"

if (FW_CONFIG["proj"] == "bwv"):
	import namednodes
	sxpc = namednodes.sv.sxpcontroller
else:
	import components.sxpcontroller as sxpc

def imf_readCsr(address, size=1, device=None, mailbox='os', timeout=10, raw=False,logging=False, log=_log):
    """
    Brief:
        Function to perform read csr command using injection module framework. This is the rev 2.0 version of read csr.

    Description:

    Argument(s):
        address - CSR address to be read from
        size - Number of consecutive addresses to access
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        csrSequence object and status on success False on failure

    Example:

    Related:
    -

    Author(s):
        Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.csrSequenceHeader(address=address)
    inputData.size = size
    if raw == True:
        outputData = None
    else:
        outputData = imf_dfx_parser.csrSequence(address=address)
    ret = imf.executeModuleAutoFill(funcName=FunctionName.READ_CSR, params=inputData, outputObject=outputData,sxp=device,mailbox=mailbox,timeout=timeout,logging=logging)
    return ret

def imf_writeCsr(address, value, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform write csr using injection module framework. This is the rev 2.0 version of write csr.

    Description:

    Argument(s):
        address - CSR address to be write to
        value - Value to be written to address
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Mailbox status code on success false on failure

    Example:
        imf_writeCsr(address=0xc0000000,value=0xdeadbeef)
        imf_writeCsr
    Related:
    -

    Author(s):
        Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.csrSequence(address=address, value=value)
    ret = imf.executeModuleAutoFill(funcName=FunctionName.WRITE_CSR, params=inputData, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_readPmic(offset, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform read pmic command using injection module framework

    Description:

    Argument(s):
        offset - PMIC offset
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        readPmicOutput object and mailbox status code returned by command.

    Example:
        imf_readPmic(offset=0x2c)
    Related:
    -

    Author(s):
        Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.readPmicInput(pmicOffset=offset)
    outputData = imf_dfx_parser.readPmicOutput()
    ret = imf.executeModuleAutoFill(funcName=FunctionName.READ_PMIC, params=inputData, outputObject=outputData, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_writePmic(offset, data, disablePmicRead=0, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform WRITE_PMIC using injection module framework

    Description:

    Argument(s):
        offset - PMIC offset
        data - Data to be written to PMIC
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Dictionary containing writePmicOutput object and mailbox status code returned by command.

    Example:

    Related:
    -

    Author(s):
        Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()


    fwu = fwUtils.FwUtils()
    if (fwu._getProject() == 'elkvalley'):
        inputData = imf_dfx_parser.writePmicInput(pmicOffset=offset, data=data)
        outputData = imf_dfx_parser.writePmicOutput()
        ret = imf.executeModuleAutoFill(funcName=FunctionName.WRITE_PMIC, params=inputData,outputObject=outputData, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)

    elif (fwu._getProject() == 'barlowvalley'):
        inputData = imf_dfx_parser.bwvWritePmicInput(pmicOffset=offset, data=data, disablePmicRead = disablePmicRead)
        outputData = imf_dfx_parser.writePmicOutput()
        ret = imf.executeModuleAutoFill(funcName=FunctionName.WRITE_PMIC, params=inputData, outputObject=outputData, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    else:
        printf('Unknown project.')
        return False
    return ret

def imf_spiRead(address, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform spi IO read command using injection module framework

    Description:

    Argument(s):
        address - Source SPI address
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Dictionary containing spiReadOutput object and mailbox status code returned by command.

    Example:

    Related:
    -

    Author(s):
        Rose Carignan
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.spiReadInput(address=address, payloadType=SMALL_PAYLOAD)
    outputData = imf_dfx_parser.spiReadOutput()
    ret = imf.executeModuleAutoFill(funcName=FunctionName.SPI_READ, params=inputData,outputObject=outputData, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_spiReadRaw(address, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform spi IO read command using injection module framework (returns list of dword output payload register values instead of object in dictionary)

    Description:
        Function performs spi IO read command and returns payload as list of dword output payload register values.

    Argument(s):
        address - Source SPI address
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Dictionary containing mailbox status code returned by command and list of dword output payload register values.

    Example:

    Related:
    -

    Author(s):
        Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.spiReadInput(address=address, payloadType=SMALL_PAYLOAD)
    ret = imf.executeModuleAutoFill(funcName=FunctionName.SPI_READ, params=inputData, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    if ret == False:
        return False
    payload = ret['result'] # Result stores list of DWORD register values read from mb_<mailbox>_output_payload registers.
    resultStart = len(payload) - DWORDS_PER_64B
    result = payload[resultStart:] # Spi Read output is in last 64 bytes of output payload.
    ret = {'status':ret['status'],'result':result}
    return ret

def imf_spiWrite(address, data, payloadType, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform spi IO write command using injection module framework

    Description:

    Argument(s):
        address - Source SPI address
        data - 64 bytes of data using small payload
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Mailbox status code returned by command.

    Example:

    Related:
    -

    Author(s):
        Rose Carignan
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.spiWriteInput(address=address, length=0, payloadType=payloadType, data=data)
    ret = imf.executeModuleAutoFill(funcName=FunctionName.SPI_WRITE, params=inputData,outputObject=None, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_getThermalPolicy(device=None, mailbox='os', timeout=10, raw=False, logging=False):
    """
    Brief:
        Function to perform get thermal policy command using injection module framework

    Description:

    Argument(s):
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Dictionary containing getThermalPolicyOutput object and mailbox status code returned by command.

    Example:

    Related:
    -

    Author(s):
        Rose Carignan
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    outputData = imf_dfx_parser.getThermalPolicyOutput()
    if raw == True: # Return raw register values instead of object
        outputData = None
    ret = imf.executeModuleAutoFill(funcName=FunctionName.GET_THERMAL_POLICY, params=None,outputObject=outputData, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_setThermalPolicy(thermalThrottling, thermalAlerting, criticalShutdownAction, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform set thermal policy command using injection module framework

    Description:

    Argument(s):
        thermalThrottling - Enable thermal throttling.
        thermalAlerting - Enable thermal alerting.
        criticalShutdownAction - Enable criticalShutdownAction
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Mailbox status code returned by command.

    Example:

    Related:
    -

    Author(s):
        Rose Carignan
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.setThermalPolicyInput(thermalThrottling=thermalThrottling, thermalAlerting=thermalAlerting, criticalShutdownAction=criticalShutdownAction)
    ret = imf.executeModuleAutoFill(funcName=FunctionName.SET_THERMAL_POLICY, params=inputData,outputObject=None, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_setMigration(die, startPointer=None, endPointer=None, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Run Migration DFx command (0xE3:0xFA).

    Description:
        Forces FW to die spare a rank and die

    Alias: -

    Argument(s):
        die          - die number to spare
        startPointer - Used in order to migrate only part of the die
        endPointer   - Used in order to only migrate part of the die (must be larger than startPointer if used)
        device       - SXP controller object
        mailbox      - mailbox to use. Default is os.
        timeout      - Timeout to use for the command.

    Return Value(s):
        True - in case of success.
        False - in case of any error.

    Example:
        setMigration(die=0, rank=0)

    Related: -

    Author(s):
       Konrad Sobocinski - Noelle Takahashi
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.setMigrationInput(die=die, startPointer=startPointer, endPointer=endPointer)
    ret = imf.executeModuleAutoFill(funcName=FunctionName.MIGRATION, params=inputData, outputObject=None, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_getSecurityNonce(device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform get security nonce command using injection module framework

    Description:

    Argument(s):
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Dictionary containing getSecurityNoneOutput object and Mailbox status code returned by command.

    Example:

    Related:
    -

    Author(s):
        Rose Carignan
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    outputData = imf_dfx_parser.getSecurityNonceOutput()
    ret = imf.executeModuleAutoFill(funcName=FunctionName.GET_SECURITY_NONCE, params=None, outputObject=outputData, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_updateThermalPollPeriod(period, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform update thermal poll period command using injection module framework

    Description:

    Argument(s):
        period - Time in ms to change the thermal polling period to.
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Mailbox status code returned by command.

    Example:

    Related:
    -

    Author(s):
        Rose Carignan
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.updateThermalPollPeriodInput(period=period)
    ret = imf.executeModuleAutoFill(funcName=FunctionName.UPDATE_THERMAL_POLL_PERIOD, params=inputData, outputObject=None, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_translateAddress(address, level, translate_type, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform translate address command using injection module framework

    Description:

    Argument(s):
        address - The DPA address to translate.
        level - The address level to translate. the leve n, n-1, n-2 are represented as numbers 2, 1, 0 as input to the command.
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Dictionary containing translateAddressOutput object and Mailbox status code returned by command.

    Example:

    Related:
    -

    Author(s):
        Rose Carignan
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.translateAddressInput(address=address, level=level, translate_type=translate_type)
    outputData = imf_dfx_parser.translateAddressOutput()
    ret = imf.executeModuleAutoFill(funcName=FunctionName.TRANSLATE_ADDRESS, params=inputData, outputObject=outputData, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_sxpRawCommand(operation, sequenceNumber, address, chunk, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform sxp raw command (codeword) using injection module framework

    Description:

    Argument(s):
        operation - Operation to perform using this command Normal Write(1), Read(2), and Force Write(3)
        sequenceNumber - Sequence number for specifying the chunk of codeword to work with. Valid values are 0-3.
        address - PDA address to perform the SXP operation.
        chunk - Payload chunk of the codeword.
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Dictionary containing sxpRawCommandOutput object and Mailbox status code returned by command.

    Example:

    Related:
    -

    Author(s):
        Rose Carignan
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.sxpRawCommandInput(operation=operation, sequenceNumber=sequenceNumber, address=address, chunk=chunk)
    outputData = imf_dfx_parser.sxpRawCommandOutput()
    ret = imf.executeModuleAutoFill(funcName=FunctionName.SXP_CODEWORD, params=inputData, outputObject=outputData, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_readSram(address, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform read sram command using injection module framework

    Description:

    Argument(s):
        address - The address of the SRAM register to be read.
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Dictionary containing readSramOutput object and Mailbox status code returned by command.

    Example:

    Related:
    -

    Author(s):
        Rose Carignan
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.readSramInput(address=address)
    outputData = imf_dfx_parser.readSramOutput()
    ret = imf.executeModuleAutoFill(funcName=FunctionName.SRAM_READ, params=inputData, outputObject=outputData, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_writeSram(address, value, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform write sram command using injection module framework

    Description:

    Argument(s):
        address - The address of the SRAM register to be written to.
        value - The value to write to the SRAM register.
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Dictionary containing writeSramOutput object and Mailbox status code returned by command.

    Example:

    Related:
    -

    Author(s):
        Rose Carignan
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.writeSramInput(address=address, value=value)
    outputData = imf_dfx_parser.writeSramOutput()
    ret = imf.executeModuleAutoFill(funcName=FunctionName.SRAM_WRITE, params=inputData, outputObject=outputData, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_sxpIoRead(address, length, mode, payloadType, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform SXP Read utilizing injection module framework.

    Description:
        Function to perform SXP Read utilizing injection module framework.

    Argument(s):
        address - SXP address to be read from (must be 64 byte aligned)
        mode - Mode of SXP memory addressing. 0: Pda, 1: Dpa
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Dictionary containing sxpIoReadOutput object and Mailbox status code returned by command.

    Example:

    Related:
    -

    Author(s):
    Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.sxpIoReadInput(address=address,length=length, mode=mode, payloadType=payloadType)
    outputData = imf_dfx_parser.sxpIoReadOutput()
    ret = imf.executeModuleAutoFill(funcName=FunctionName.SXP_READ, params=inputData, outputObject=outputData, sxp=device, mailbox=mailbox, timeout=timeout, logging=logging)
    return ret

def imf_sxpIoWrite(address, mode, data, device=None, mailbox='os', timeout=10, logging=False):
    """
    Brief:
        Function to perform SXP Write utilizing injection module framework.

    Description:
        Function to perform SXP Write utilizing injection module framework.

    Argument(s):
        address - SXP address to be written to (must be 64 byte aligned)
        mode - Mode of SXP memory addressing. 0: Pda, 1: Dpa
        data - Data to be written to SXP.
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.

    Return Value(s):
        Mailbox status code returned by command.
    Example:

    Related:
    -

    Author(s):
    Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.sxpIoWriteInput(address=address,mode=mode,payloadType=SMALL_PAYLOAD,data=data)
    ret = imf.executeModuleAutoFill(funcName=FunctionName.SXP_WRITE, params=inputData, sxp=device, mailbox=mailbox,timeout=timeout,logging=logging)
    return ret

def imf_getFConfigSingle(token, version=0x1, device=None, mailbox='os', raw=False, timeout=10, logging=False):
    """
    Brief:
        Function to perform GET_FCONFIG injection module command for a single FConfig token.

    Argument(s):
        token - FConfig token number
        version - FConfig version
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.
        logging - Boolean for exra logging messages

    Return Value(s):
        False on failure to execute or status and result dictionary returned by executeModuleAutoFill
    Example:
        imf_getFConfigSingle(token=0x0018,device=sv.sxpcontroller000,mailbox='smbus')

    Author(s):
    Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.fConfigGetInput(version=version,transferType=imf_dfx_parser.TRANSFER_TYPE['SINGLE'],token=token)
    if raw == True:
        retFconfig = None
    else:
        retFconfig = imf_dfx_parser.fConfig()
    ret = imf.executeModuleAutoFill(funcName=FunctionName.GET_FCONFIG,params=inputData,outputObject=retFconfig, sxp=device,mailbox=mailbox,timeout=timeout,logging=logging)
    return ret

def imf_fConfig(tokens=None, other=None, filename=None, buf=None, device=None, mailbox='os', timeout=10):
        """
        Brief:
            fConfig command ported from TWIDL. Gets fConfig list from the dimm.

        Description:
            Retrieves fConfig entries that the dimm is aware of as an fConfig list.

        Argument(s):
            tokens   - A single FConfig token or a list of FConfig tokens to retrieve
            other    - An 'other' fConfig object holding the tokens to read.
            filename - File to load during object creation. If used, will not read from the device.
            buf      - Byte buffer to load from during object creation. If used, will not read from the device.
            device   - Sxp controller object
            mailbox  - mailbox to use for command
            timeout  - timeout for command

        Return Value(s):
            fConfig buflist, False on failure.

        Example:
            entryList = fConfig()

            entryList = fConfig(tokens=1)

            entryList = fConfig(tokens=[1,2])

        Related:
            -

        Author(s):
            Marcus Yazzie, Mythili Srinivasan, Stephen (Bobby) Thompson
        """
        imf = imf_helper_cmd.ImfHelperCmds()
        retFconfig = imf_dfx_parser.fConfig(other=other, filename=filename, buf=buf)

        # If we were given a filename or buffer, then we're done.
        if filename != None or buf != None: return retFconfig

        numDwords = 0
        if tokens != None:
            if type(tokens) is not list:
                # If single entry make into list
                tokens = [tokens]

            finalFconfig = imf_dfx_parser.fConfig()

            for token in tokens:
                inputData = imf_dfx_parser.fConfigGetInput(transferType=imf_dfx_parser.TRANSFER_TYPE['SINGLE'], token=token)
                result =  imf.executeModuleAutoFill(funcName=FunctionName.GET_FCONFIG, outputObject=retFconfig, params=inputData, sxp=device, mailbox=mailbox, timeout=timeout)

                if result == False:
                    return False

                if result['status']:
                    return False

                finalFconfig += retFconfig
                numDwords += retFconfig.header['numDwords']

            finalFconfig.header['numDwords'] = numDwords
            return finalFconfig

        inputData = imf_dfx_parser.fConfigGetInput(transferType=imf_dfx_parser.TRANSFER_TYPE['ALL_INITIATE'])
        fConfigHeaderSize = retFconfig.header.bitsize()
        currentDataSize = 0
        firstLoad = True

        # Execute DFX commands until total payload size indicated by first DFX output header is reached
        while firstLoad or (currentDataSize < (numDwords * 32)):
            result =  imf.executeModuleAutoFill(funcName=FunctionName.GET_FCONFIG, outputObject=retFconfig, params=inputData, sxp=device, mailbox=mailbox, timeout=timeout)

            if result == False:
                return False

            if result['status']:
                return False

            if firstLoad == True:
                numDwords = retFconfig.header['numDwords']
                finalFconfig = imf_dfx_parser.fConfig(numDwords=numDwords)
                inputData = imf_dfx_parser.fConfigGetInput(transferType=imf_dfx_parser.TRANSFER_TYPE['ALL_CONTINUE'])
                firstLoad = False

            finalFconfig += retFconfig
            currentDataSize += retFconfig.bitsize() - fConfigHeaderSize

        return finalFconfig

def imf_setFconfig(token=None, value=None, dWords=None, other=None, device=None, dWordsOverride=None, versionOverride=False, mailbox='os',timeout=10):
    """
    Brief:
        setFconfig command ported over from TWIDL. Sends an FConfig list to be set to the dimm.

    Description:
        The user must build an FConfig task buflist and pass it in.

    Argument(s):
        token          - Fconfig token
        value          - Fconfig value
        dwords         - dwords
        dWordsOverride - An override for the numDwords entry in the header of the buflist
        other          - The fConfig buflist object with a list of FConfig Entries
                       - Single FConfig entry to set
                       - Other can also be an instance of the imf_helper_cmd.InputPayloadRegisters class.
                         If this is the case the framework will execute the module with this given instance as params
        device   - Sxp controller object
        mailbox  - mailbox to use for command
        timeout  - timeout for command

    Return Value(s):
        True on success. False on failure.

    Example:
        r = setFconfig(token='rdEnable', value=True)

        entryList = fConfig()
        entryList += fConfigEntry(token='rdEnable',value=True)
        entryList += fConfigEntry(token='rdIntervalType',value=1)
        entryList += fConfigEntry(token='rdInterval',value=0x1FFF)
        r = setFconfig(other=entryList)

        entry = rdEnable(value=1)
        r = setFconfig(other=entry)

        entry = fConfigEntry(token='rdEnable',value=True)
        r = setFconfig(other=entry)

    Related:
        -

    Author(s):
        Marcus Yazzie, Mythili Srinivasan, Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    if isinstance(other,imf_helper_cmd.InputPayloadRegisters):
        return imf.executeModuleAutoFill(funcName=FunctionName.SET_FCONFIG,params=other,sxp=device,mailbox=mailbox,timeout=timeout)
    if token != None and value != None:
        myFconfig = imf_dfx_parser.fConfig()
        myFconfig += imf_dfx_parser.fConfigEntry(token, value, dWords)
    elif other != None:
        # If we get an fConfigEntry instead of fConfig, convert to fConfig
        if issubclass(type(other), imf_dfx_parser.fConfigEntry):
            myFconfig = imf_dfx_parser.fConfig()
            myFconfig += other
        elif issubclass(type(other), imf_dfx_parser.fConfig):
            myFconfig = imf_dfx_parser.fConfig(other=other)
        else:
            raise Exception("'other' parameter needs to be subclass of fConfig or fConfigEntry!!")
    else:
        raise Exception("Need 'token' and 'value' parameter or 'other' parameter!!")

    bufSize = (imf.getInjectionModuleBufferSizes(sxp=device))['IMF_INPUT_BUFFER_SIZE']
    # Iterate through all FConfig entries in list
    while len(myFconfig) > 0:
        thisFconfig = imf_dfx_parser.fConfig()
        myFconfig.header['numDwords'] = (myFconfig.bytesize() / 4) - (myFconfig.header.bytesize() / 4)

        nextEntry = myFconfig[0]
        # Load thisFconfig with as many entries can fit in a single DFX input payload
        while (thisFconfig.bytesize() + nextEntry.bytesize()) < bufSize:
            thisFconfig += nextEntry
            myFconfig = myFconfig[1:]
            if len(myFconfig) == 0:
                break

            nextEntry = myFconfig[0]

        if dWordsOverride != None:
            thisFconfig.header['numDwords'] = dWordsOverride
        else:
            thisFconfig.header['numDwords'] = (thisFconfig.bytesize() / 4) - (thisFconfig.header.bytesize() / 4)

        if versionOverride == True:
            thisFconfig.header['version'] = 0

        result = imf.executeModuleAutoFill(funcName=FunctionName.SET_FCONFIG, params=thisFconfig, sxp=device,mailbox=mailbox, timeout=timeout)
        if result == False:
            return False

        if result['status']:
            return False

    return True

def imf_rawCodeword(address, other=None, device=None, mailbox="os", timeout=10):
    """
    Brief:
        Reads a raw codeword (352 bytes) at specified address using injection module framework.

    Argument(s):
        address   - PDA address to read.
        other     - An 'other' codeword instance to copy.
        device    - Sxp controller object.
        mailbox   - mailbox to use for command.
        timeout   - timeout to use for command.

    Return Value(s):
        Raw Codeword on success. False on failure.

    Example:
       r = imf_rawCodeword(address=0x200000)

    Related:
        -

    Author(s):
        Shaun Miller, Paul Ruby, Mythili Srinivasan, Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    cw = imf_dfx_parser.codeword(address=address, other=other)
    if other != None: return cw

    # Read codeword, 88 bytes at a time.  Must perform 4 separate commands.
    for i in range(0, 4):
        # The sequence number determines how buffer interaction will work.
        cw.sequence = i
        cw.operation = 'read'
        ret = imf.executeModuleAutoFill(funcName=FunctionName.SXP_CODEWORD,
                                                       outputType=imf_dfx_parser.codeword,
                                                       params=cw,outputObject=cw,sxp=device,
                                                       mailbox=mailbox,timeout=timeout)
        if ret == False: return False
        status = ret['status']
        if status: return False
    return cw

def imf_eccPolicy(inputData=None, writeDisable=None, readDisable=None, device=None, mailbox='os', timeout=10):
    """
    Brief:
        ECC Policy DFx command using injection module framework ported from TWIDL

    Description: -

    Alias:
        eccpolicy

    Argument(s):
        inputData           - imf_dfx_parser.eccPolicy
        writeDisable        - Disables write ecc control when True. Default False.
        readDisable         - Disables read ecc control when True. Default False.
        mailbox             - mailbox to use. Default is os.
        device              - sxp controller object
        timeout             - timeout to use for command

    Return Value(s):
        False on failure to execute module
        Dictionary of mailbox status code and output payload registers

    Example:
        eccPolicy(write=True)

    Related: -

    Author(s):
       Konrad Sobocinski
       Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.eccPolicy(other=inputData, write=writeDisable, read=readDisable)
    ret = imf.executeModuleAutoFill(funcName=FunctionName.ECC_POLICY, params=inputData,sxp=device,mailbox=mailbox,timeout=timeout)
    return ret

def getSpdFconfigData(socket,channel,slot,filename=r"C:\Temp\spd_fconfigs.txt"):
    from falconvalley.sv import spd_fconfig_utils as fcu
    from falconvalley.fw.imf.parsers import imf_dfx_parser as dfxParser
    '''
    Brief:
        Function adopted from falconvalley.sv.spd_fconfig_utils.py syncAll_spd_fconfig.
        This function retrieves the FConfig data that is to be set when performing sync spd.

    Argument(s):
        socket  - socket of device to retrieve spd data for
        channel - channel of device to retrieve spd data for
        slot    - slot of device to retrieve spd data for

    Return Value(s):
        fconfig object containing fconfigs corresponding to retrieved SPD data.

    Example:
        spds.refresh()         # Do this to refresh the spd object to make sure the eeproms are detected
        spds.dimmeepromlist    # Do this to list the eeproms and associated slot, socket and channel
        getSpdFconfigData(socket=0,channel=5,slot=0)

    Author(s):
        Adopted from function written by Girish Bulusu
        Stephen (Bobby) Thompson
    '''
    # Dictionary of INDEX:[FCONFIG TOKEN, BYTE OFFSET START, BYTE OFFSET END, DWORD LENGTH, BITS TO EXTRACT]
    spdoffsets = {
        0:[0x1A,181,181,1],
        1:[0x24,130,130,1,4,7],
        2:[0x1B,178,178,1],
        3:[0x1C,180,180,1],
        4:[0x1D,320,321,1],
        5:[0x1E,325,328,1],
        6:[0x1F,329,348,5],
        7:[0x19,176,176,1],
        8:[0x3C,322,324,1], # SPD manufacturer location and date fconfig needed when core dump changes go in.
    }
    print("READING SPD DATA FOR SOCKET: %d CHANNEL: %d SLOT: %d" % (socket,channel,slot))
    fconfigList = dfxParser.fConfig()
    eeprom_spd = fcu.readSPD(socket=socket,channel=channel,slot=slot)
    for i in range(len(spdoffsets)):
        spdDataEntryVals = spdoffsets[i]
        if (len(spdDataEntryVals) == 4):
            tokenEntryList = eeprom_spd[spdDataEntryVals[1]:spdDataEntryVals[2]+1] # Get spd data from corresponding offsets
        elif (len(spdDataEntryVals) == 6):
            if (spdDataEntryVals[1] != spdDataEntryVals[2]):
                print("BIT FIELD EXTRACTION ONLY POSSIBLE FOR SINGLE BYTE ENTRIES")
                return False
            else: # Extract bits
                tokenEntryByte = eeprom_spd[spdDataEntryVals[1]:spdDataEntryVals[2]+1][0]
                tokenEntryBits = (tokenEntryByte >> (spdDataEntryVals[4]) & ((1<<(spdDataEntryVals[5] - spdDataEntryVals[4]))-1) )
                tokenEntryList = [tokenEntryBits]

        tokenEntryValue = 0x0
        for j in range(len(tokenEntryList)):
            tokenEntryValue |= (tokenEntryList[j] << j*8)

        fconfig = dfxParser.fConfigEntry(token=spdDataEntryVals[0],value=tokenEntryValue,dWords=spdDataEntryVals[3])
        fconfigList += fconfig

    temp = filename.split('.txt')
    filename = temp[0] + '.' + str(socket) + '.' + str(channel) + '.' + str(slot) + '.txt'
    print("Writing SPD FConfig data to file %s" % filename)
    fconfigList.toTextFile(filename)
    return fconfigList

def imf_reportFuseIdInformation(inputData=None, device=None, rank=None, mailbox='os', timeout=10):
    """
    Brief:
        Report Fuse Id Information DFx command through injection module framework. Ported from TWIDL.

    Description: -

    Argument(s):
        inputData   - imf_dfx_parser.reportFuseIdInformationInput
        rank        - Rank to read.
        mailbox     - mailbox to use. Default is HOST.
        device      - sxp controller object
        timeout     - timeout to use for command

    Return Value(s):
        False on failure to execute module, imf_dfx_parser.reportFuseIdInformation() on success

    Example:
        imf_reportFuseIdInformation(rank=2)

    Related: -

    Author(s):
        Konrad Sobocinski
        Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.reportFuseIdInformationInput(other=inputData, rank=rank)
    output = imf_dfx_parser.reportFuseIdInformation()
    ret = imf.executeModuleAutoFill(funcName=FunctionName.FUSE_ID,params=inputData,outputObject=output,sxp=device,mailbox=mailbox,timeout=timeout)
    return ret

def imf_getSpiManifest(device=None, mailbox='smbus', timeout=10, log=_log):
    """
    Brief:
        Get SPI Manifest data.

    Description: -

    Argument(s):
        device      - sxp controller object
        mailbox     - mailbox to use. Default is smbus.
        timeout     - timeout to use for command

    Return Value(s):
        False on failure to execute module, imf_dfx_parser.getSpiManifestOutput() on success,
        which contains the sxp timing table versions, ddrt mmrc table versions, sxp mmrc table versions,
        and loaded pIMF module id.

    Related: -

    Author(s):
        Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    output = imf_dfx_parser.getSpiManifestOutput()
    ret = imf.executeModuleAutoFill(funcName=FunctionName.GET_SPI_MANIFEST,outputObject=output,sxp=device,mailbox=mailbox,timeout=timeout)
    if (ret == False):
        log.error("IMF_ERROR: imf framework failed to execute GET_SPI_MANIFEST command")
    elif (ret['status']):
        log.error("GET_SPI_MANIFEST failed with mailbox status code x%08x"  % ret['status'])
    else:
        log.result("GET_SPI_MANIFEST returns:")
        log.result("   SDP timing table version: %d.%d.%d" % (output['singleDieSxpTimingTableMajorVersion'], output['singleDieSxpTimingTableMinorVersion'], output['singleDieSxpTimingTableRevision']))
        log.result("   DDP timing table version: %d.%d.%d" % (output['dualDieSxpTimingTableMajorVersion'], output['dualDieSxpTimingTableMinorVersion'], output['dualDieSxpTimingTableRevision']))
        log.result("   QDP timing table version: %d.%d.%d" % (output['quadDieSxpTimingTableMajorVersion'], output['quadDieSxpTimingTableMinorVersion'], output['quadDieSxpTimingTableRevision']))
        log.result("   DDRT MMRC table version : %d" % output['ddrtMmrcTableVersion'] )
        log.result("   SXP MMRC table version  : %d" % output['sxpMmrcTableVersion'])
        log.result("   PIMF Module Id          : %d" % output['pimfModuleId'])

        log.info("GET_SPI_MANIFEST raw output:")
        log.info("   status: 0x%x" % ret['status'])
        log.info("   singleDieSxpTimingTableMajorVersion     %d" % output['singleDieSxpTimingTableMajorVersion'])
        log.info("   singleDieSxpTimingTableMinorVersion     %d" % output['singleDieSxpTimingTableMinorVersion'])
        log.info("       singleDieSxpTimingTableRevision     %d" % output['singleDieSxpTimingTableRevision'])
        log.info("     dualDieSxpTimingTableMajorVersion     %d" % output['dualDieSxpTimingTableMajorVersion'])
        log.info("     dualDieSxpTimingTableMinorVersion     %d" % output['dualDieSxpTimingTableMinorVersion'])
        log.info("         dualDieSxpTimingTableRevision     %d" % output['dualDieSxpTimingTableRevision'])
        log.info("     quadDieSxpTimingTableMajorVersion     %d" % output['quadDieSxpTimingTableMajorVersion'])
        log.info("     quadDieSxpTimingTableMinorVersion     %d" % output['quadDieSxpTimingTableMinorVersion'])
        log.info("         quadDieSxpTimingTableRevision     %d" % output['quadDieSxpTimingTableRevision'])
        log.info("                  ddrtMmrcTableVersion     %d" % output['ddrtMmrcTableVersion'])
        log.info("                   sxpMmrcTableVersion     %d" % output['sxpMmrcTableVersion'])
        log.info("                          pimfModuleId     %d" % output['pimfModuleId'])
    return ret

def imf_getPliLogHeader(device=None, mailbox='os', timeout=10):
    """
    Brief:
        Retrieves PLI log metadata through injection module framework.

    Description:
        Execute injection module command for retrieving PLI log header structure resides in FW SRAM and the metadata of the PLI log including PLI flow time duration, total count of valid log entries and maximum retrievable PLI log pages.

    Argument(s):
        mailbox     - mailbox to use. Default is HOST.
        timeout     - timeout to use for command

    Return Value(s):
        @imf_dfx_parser.pliLogHeader()
        False on failure to execute module

    Example:
        imf_getPliLogHeader()

    Related:
        imf_getPliLogEntries

    Author(s):
        Deanna Shih
    """

    imf = imf_helper_cmd.ImfHelperCmds()
    output = imf_dfx_parser.pliLogMetadata()
    ret = imf.executeModuleAutoFill(funcName=FunctionName.PLI_LOG_METADATA, sxp=device, params=None, outputObject=output, mailbox=mailbox, timeout=timeout)
    if ret == False:
        return ret
    status = ret['status']
    if status:
        return False
    return ret['result']

def imf_getPliLogEntries(logPage=0, device=None, mailbox='os', timeout=10, buf=None, other=None, inputData=None):
    """
    Brief:
        Retrieves PLI log metadata through injection module framework.

    Description:
        Execute injection module command for retrieving a page of PLI log entries resides in FW SRAM.

    Argument(s):
        mailbox         - mailbox to use. Default is HOST
        logPage         - page index starting from 0 to max pages
        timeout         - timeout to use for command

    Return Value(s):
        @imf_dfx_parser.pliLogEntries()
        False on failure to execute module

    Example:
        imf_getPliLogEntries()

    Related:
        imf_getPliLogHeader

    Author(s):
        Deanna Shih
    """

    imf = imf_helper_cmd.ImfHelperCmds()
    input = imf_dfx_parser.pliLogEntriesInput(other=inputData, log_page=logPage)
    output = imf_dfx_parser.pliLogEntries()
    ret = imf.executeModuleAutoFill(funcName=FunctionName.PLI_LOG_ENTRIES, sxp=device, params=input, outputObject=output, mailbox=mailbox, timeout=timeout)
    if ret == False:
        return ret
    status = ret['status']
    if status:
        return False
    return ret['result']

def imf_getSpiRegionInfo(spiRegionToken, device=None, mailbox='smbus', timeout=10, log=_log):
    imf = imf_helper_cmd.ImfHelperCmds()
    tokens = imf_dfx_parser.SPI_REGION_TOKENS
    inputData = imf_dfx_parser.getSpiRegionInfoInput(spiRegionToken=spiRegionToken)
    outputData = imf_dfx_parser.getSpiRegionInfoOutput()
    log.info("IMF_INFO: Getting spi info for %s region" % tokens.keys()[tokens.values().index(spiRegionToken)])
    ret = imf.executeModuleAutoFill(funcName=FunctionName.GET_SPI_REGION_INFO, params=inputData, outputObject = outputData, sxp=device, mailbox=mailbox, timeout=timeout)
    if (ret == False):
        log.error("IMF_ERROR: Failed to execute get spi region injection module command")
        return False
    elif (ret['status'] != 0x0):
        log.error("IMF_ERROR: GET_SPI_REGION_INFO command failed with status %s" % mbStatCodes.get(ret['status']))
        return False
    else:
        return ret['result']

def getSramData(device, var, mapFile, mailbox='smbus', sparse=False, align=128, log=_log):
    """
    Description: -
       This function is used to get data from a var in SRAM via readCSR
    Argument(s):
        device         - sxp controller component
        var            - variable to get data for
        mapFile        - full path to map file
        sparse         - use this to indicate that we want to stop getting sram data when we've seen zeroThreshold bytes of zeros. Mostly useful for getting NLOGs from SRAM
        align          - byte alignment for returned data. This is to be used in conjuction with sparse to determine when to stop if we have a chunk of all zero
        mailbox        - mailbox to use. Default is smbus.
        log            - logger object

    Return Value(s):
        True on success, false on failure
    Author(s):
        Stephen (Bobby) Thompson
    """
    fwu = fwUtils.FwUtils()
    bytesRead = 0
    chunk = 0

    varData = []
    bytesPerDword = 4
    maxDwordsPerPayload = 22 # Maximum payload is 22 dwords for read csr
    failCount = 0
    maxBytesPerPayload = maxDwordsPerPayload * bytesPerDword

    (varBase, varSize) = fwu.getSramMapEntry(mapFile=mapFile, symbol=var, log=log)
    if varBase is None or varSize is None:
        log.error("ERROR: Failed to find requested variable in map file. Cannot get SRAM data.")
        return False

    totalPayloads = (varSize / maxBytesPerPayload) + (varSize % maxBytesPerPayload != 0)
    dwordsToRead = maxDwordsPerPayload
    varEnd = varBase + varSize
    for payload in range(totalPayloads):
        address = varBase + (payload*maxBytesPerPayload)
        log.info("INFO: %s Payload %d of %d @ 0x%x" % (var, payload+1, totalPayloads, address))

        if ((address + maxBytesPerPayload) > varEnd):
            dwordsToRead = (varEnd - address) / bytesPerDword

        ret = imf_readCsr(address=address, size=dwordsToRead, device=device, log=log)

        if (ret == False):
            log.error("ERROR -> Failed to execute READ_CSR through injection module framework")
            failCount += 1
        else:
            if (ret['status'] != 0):
                log.error("ERROR -> READ_CSR failed with mailbox status code %s" % mbStatCodes.get([ret['status']]))
                failCount += 1
            else:
                for data in ret['result']:
                    varData.append(data.value)
                    # If we're in sparse mode we're going to stop getting data when we've received a chunk of byte size "align" that is all zeros
                    if (sparse == True):
                        bytesRead += bytesPerDword
                        if (bytesRead % align == 0):
                            # Check if chunk is all zeros
                            if (all(data == 0 for data in varData[chunk*(align/bytesPerDword) - 1 : ])):
                                log.info("Running in sparse mode. Found chunk of all zeros. Returning.")
                                return varData
                            else:
                                chunk += 1
                log.result(ret['result'])
    if (failCount != 0):
        log.warning("ERROR -> Failures occurred when dumping FW state via READ_CSR. See previous log messages for details")
        return False

    return varData

def uploadModuleToSpi(filePath, spiOffset, device=None, uploadToSram=True, mailbox='smbus', log=_log):
    """
        Brief:
            Upload file to SPI (Ported from TWIDL)

        Description: -

        Alias:

        Argument(s):
            filePath     - path to file
            spiOffset    - 4kB alligned offset
            device       - sxp controller component
            mailbox      - mailbox to execute commands through
            uploadToSram - flag to indicate to upload the module to sram after writing to spi

        Return Value(s):
            True - in case of success
            False - in case of any error.

        Example:
            uploadModuleToSpi(r"C:\Users\Public\injection_modules\1.0.0.9999\eks1_dimm_prod\pimf_module.1.0.0.9999.bin", 0xe3000) ->

        Related: -

        Author(s):
            Konrad Sobocinski
    """
    from falconvalley.fw.imf.commands.imf_raw_utils import bytearray_to_int
    imf = imf_helper_cmd.ImfHelperCmds()

    if spiOffset % 4096 != 0:
        log.error("SPI offset has to be 4kB alligned")
        return False
    try:
        with open(filePath, 'rb') as _file:
            fileBin = bytearray(_file.read())
            fileSize = fileBin.__len__()
    except Exception as e:
        log.error("Failed to load file into buffer: %s" % e.message)
        return False

    # Get the module ID from the binary file.
    modId = imf.getModuleIdFromFile(filePath)

    # need to write whole 4kB block while using small payload refer to injection modules doc
    if fileSize % 4096 != 0:
        fileSize = fileSize + 4096 - (fileSize % 4096)  # extend to 4kB
    for i in xrange(0, fileSize, 64):
        intData = bytearray_to_int(fileBin[i:i + 64])
        result = imf_spiWrite(address=spiOffset + i, payloadType=1, data=intData, device=device, mailbox='smbus')
        if (result == False):
            log.error("SPI write via small payload failed!")
            return False
        else:
            if (result['status'] != 0x0):
                log.error("SPI write failed with status 0x%X" % result['status'])
                return False
            else:
                result = True
    log.result("File Upload To SPI success")

    # Save the SPI module ID if we're successful
    imf.imfRawCmd.saveSpiModuleId(sxp=device, spiModuleId=modId)

    if (uploadToSram):
        log.result("Uploading module from SPI to SRAM")
        result = imf.imfRawCmd.uploadModuleFromSpi(id=modId, sxp=device, mailbox=mailbox)
    return result

def imf_NlogSram(device, mapFullPath="", dictFullPath="", server="", forceRaw=False, nlogBin="nlog_sram.bin", mailbox='smbus', build="", sparse=True, log=_log):
    """
    Description:
        This function is used to retrieve NLOGS from sram via injection module function READ_CSR

    Argument(s):
        device       - sxp controller object
        mapFullPath  - Full path of map file
        dictFullPath - Full path of nlog dict file
        server       - Server that hosts map and dict files
        forceRaw     - Used to indicate that we still want to collect the NLOG binary data even if we don't have the dict
        nlogBin      - Raw NLOG binary file name
        log          - logging object

    Return Value(s):
        True - in case of success
        False - in case of any error.

    Author(s):
        Stephen Thompson
    """
    from falconvalley.fw import fnvFwLogFunctions as fwl
    nlogSramVar = "sSramLogBuffer"
    parseBin = True

    # Try to find the map and dict files if None were passed
    if (mapFullPath == ""):
        [found, fileDir, mapFile, dictFile] = fwl.FindFirmwarePathForDevice(fnv=device, build=build, server=server, log=log)
        if (found):
            if (found == 2):
                log.warn("Unable to find the dictionary in the FW path. Unable to parse NLOGS but the raw binary will still be collected")
                parseBin = False
            if (found == 3):
                log.warn("Unable to find the map file in the FW path. Unable to get NLOGS from SRAM")
                return False
        else:
            log.error("Unable to find FW path to map file and dictionary. We will be unable to retrieve NLOGS")
            return False

        mapFullPath = fileDir + os.sep + mapFile
        if (parseBin == True):
            dictFullPath = fileDir + os.sep + dictFile
        else:
            dictFullPath = ""
            parseBin = False
    else:
        if (not os.path.isfile(mapFullPath)):
            log.error("Map file path provided %s was not found." % mapFullPath)
            return False

        fileDir = os.path.dirname(mapFullPath)

        if (not os.path.isfile(dictFullPath)):
            log.warn("NLOG dict file provided %s was not found. We will be unable to parse NLOGS" % dictFullPath)
            if (forceRaw == False):
                log.warn("If you wish to capture the raw NLOG binary data without a dict file pass forceRaw=True")
                return False
            else:
                log.warn("forceRaw was set to true. Continuing to gather raw NLOG binary for offline parsing")
                parseBin = False

    nlogData = getSramData(device=device, var=nlogSramVar, mapFile=mapFullPath, sparse=sparse, log=log)

    if (nlogData == False):
        log.error("Failed to get NLOG data from SRAM via READ_CSR")
        return False
    try:
        binFile = open(nlogBin, "wb")
        binFile.write(struct.pack('%iI' % len(nlogData) , *nlogData))
        binFile.close()
    except Exception as e:
        log.error("Failed writing NLOG data to binary file with exception %s" % str(e))
        return False
    else:
        log.info("Finsihed getting NLOG data from SRAM")

    if (parseBin == True):
        try:
            log.info("Parsing NLOG binary data captured from SRAM with NLOG dictionary %s" % str(dictFullPath))
            fwl.NLOG_Parse(nlogBin, dictFullPath, log)
        except Exception as e:
            log.error("Failed parsing NLOG data with exception %s" % str(e))
            return False
        else:
            return True
    else:
        log.result("NLOG binary data can be found at %s" % os.path.realpath(nlogBin))
        return -1    # Return something distict so we know only to get the raw binary

def imf_formatDevice(fillPattern=0x0, preservePdasWriteCount=0x1, deviceList=None, unlockDimm=True, mailbox='smbus', timeout=7200, log=_log):
    """
    Brief:
        Function to perform format device command using injection module framework. This is the rev 1.0 version of format device.

    Description:

    Argument(s):
        fillPattern - Pattern to format the memory with
        preservePdasWriteCount - Preserve Pdas Write Count: 0x0 - Do not prserve, 0x1 - Preserve
        deviceList - For EKV project, this would be list of components.sxpcontroller.mbcomponent.ComponentMB objects as returned by
                     components.sxpcontroller.getAll() method.

                     For BWV project, this could be a list type of pysvtools.sxpcontroller.components.mbcomponent.SxpcontrollerComponent
                     objects that the user constructs, or a instance of namednodes.comp.ComponentGroup which will be an iterable data structure comprised of
                     pysvtools.sxpcontroller.components.mbcomponent.SxpcontrollerComponent.
                     Note: The namednodes.comp.ComponentGroup object is what is returned by sv.sxpcontroller.getAll() in BWV project.

                     If the deviceList parameter is None in either project, the device list for the sytem will be retrieved through fwu.sxpComponent.getAll()
                     which will return the same result as components.sxpcontroller.getAll() (list type) in EKV, and sv.sxpcontroller.getAll()
                     (namednodes.comp.ComponentGroup type) in BWV.

        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.
        unlockDimm - Bool to indicate whether or not we want this function to try and unlock the dimms
    Return Value(s):
        formatOutput object and status on success False on failure

    Example:

    Related:
    -

    Author(s):
        Lu Sun
        Stephen (Bobby) Thompson
    """
    from falconvalley.fw.imf.commands import imf_raw_utils as utils
    imf = imf_helper_cmd.ImfHelperCmds()
    fwu = fwUtils.FwUtils()

    inputData = imf_dfx_parser.formatDeviceInput(fillPattern=fillPattern, preservePdasWriteCount=preservePdasWriteCount)

    retVal = 0

    # If no device is passed, we're assuming user wants to format all of the dimms in the system
    if deviceList is None:
        log.info(ct.INFO + "No sxpcomponent was passed, formatting all dimms in the system")
        deviceList = fwu.sxpComponent.getAll()#fu.getPopFnvList(fnv=device)

    # If we're unlocking make sure we unlock all of the dimms before continuing
    if unlockDimm:
        for dev in deviceList:
            dev.unlock()

    # Looping through each device in device list to execute format. We're not polling for completion here so we don't hang up the process for each dimm
    for dev in deviceList:
        log.info(ct.INFO + "Disabling the Read Disturb before trying to format the dimm")
        from falconvalley.fw.fnvFwFunctions import setMailboxReg, getMailboxReg, getStatusReg, getReg, getRegObj
        #dev.p_reeg_ctrl.rddisturb_start = 0x0
        reg = getRegObj(reg="p_reeg_ctrl", fnv=dev)
        reg.rddisturb_start = 0x0
        deviceName = fwu.getSxpName(dev)
        log.info(ct.INFO + "Send format_device command to dimm %s... -> waiting for completion up to (%d secs)" % (deviceName, timeout))
        # poll=False indicates that we're skipping polling
        imf.executeModuleAutoFill(funcName=FunctionName.FORMAT_DEVICE, params=inputData, sxp=dev,mailbox=mailbox,timeout=timeout, poll=False)
        log.info(ct.INFO + "Current Time is: %s\n", datetime.datetime.time(datetime.datetime.now()));

    # Start polling for completion for each device in device list.
    for dev in deviceList:
        deviceName = fwu.getSxpName(dev)
        outputData = imf_dfx_parser.formatDeviceOutput()
        ret = utils.imfPollOutputData(sxp=dev, outputObject=outputData, mailbox=mailbox, timeout=timeout, log=log)
        log.info(ct.INFO + "Current Time is: %s\n", datetime.datetime.time(datetime.datetime.now()));
        if ret.dfxStatus == 0:
            if ret.imfStatus == 0x0:
                log.result(ct.INFO + "Format device succesful on dimm %s returned" % deviceName)
                log.result(ret.outputData)
            else:
                log.error(ct.ERROR + "Format NOT completed on dimm %s. Status: x%x" % (deviceName, ret.imfStatus))
                log.result(ret.outputData)
                retVal = 1
        else:
            retVal = 1
    return retVal

def imf_getMediaStatistics(tokenList=None, filename=None, device=None, mailbox='os', timeout =10, log=_log, logging=False):
    """
    Brief:
        Function to perform get media statistics utilizing injection module framework.

    Description:
        Function to perform get media statistics utilizing injection module framework.
        Only small payload type is supported.

    Argument(s):
        tokenList - List of requested tokens ids(Provide no more than 10 token ids at a time)
        filename - name of file where output is saved to
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.
        logging - Boolean for extra print messages

    Return Value(s):
        Dictionary containing getMediaStatisticsOutput object and Mailbox status code returned by command.

    Example:
        Ex. 1. Request all media statistics:
                import falconvalley.fw.imf.dfx.imf_dfx as imf_dfx
                imf_dfx.imf_getMediaStatistics()

                or

                fw.getMediaStatistics()

        Ex. 2. Request all media statistics and save it to file c:\\temp\\test_mediaStatistics.txt
                import falconvalley.fw.imf.dfx.imf_dfx as imf_dfx
                imf_dfx.imf_getMediaStatistics(filename="c:\\\\temp\\\\test_mediaStatistics.txt")

                or

                fw.getMediaStatistics(filename="c:\\\\temp\\\\test_mediaStatistics.txt")

        Ex. 3. Request first five media statistics:
                import falconvalley.fw.imf.dfx.imf_dfx as imf_dfx
                imf_dfx.imf_getMediaStatistics(tokenList=[1,2,3,4,5])

                or

                fw.getMediaStatistics(tokenList=[1,2,3,4,5])

    Related:
    -

    Author(s):
    Marcus A Yazzie
    Lu Sun
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    log.result('IMF_INFO: Using {:s} mailbox'.format(mailbox))
    # transfer type is 'All'
    if (tokenList == None):
        statCount = 0xFFFFFFFF
        chunkIndex = 0
        retVal = imf_dfx_parser.getMediaStatisticsOutput()
        while statCount != 0:
            inputData = imf_dfx_parser.getMediaStatisticsInput(transferType=1, chunkIndex=chunkIndex, payloadType=SMALL_PAYLOAD)
            outputData = imf_dfx_parser.getMediaStatisticsOutput()
            log.result('IMF_INFO: chunkIndex: {:d}'.format(chunkIndex))
            ret = imf.executeModuleAutoFill(funcName=FunctionName.GET_MEDIA_STATISTICS, params=inputData, outputObject=outputData,
                                            sxp=device, mailbox=mailbox, timeout=timeout, logging=False)

            if (ret == False):
                log.error("ERROR -> Failed to execute GET_MEDIA_STATISTICS through injection module framework")
                return False

            if (ret['status'] != 0):
                log.error("ERROR -> GET_MEDIA_STATISTICS failed with mailbox status code %s" % mbStatCodes.get(ret['status']))
                return False

            response = ret['result']
            log.result('IMF_INFO: response.size {:d}'.format(response.size))
            chunkIndex = chunkIndex + 1
            statCount = response.size
            retVal = retVal + response
        if (logging == True):
            log.result(retVal)
        if (filename != None):
            retVal.toTextFile(filename=filename)
        return retVal

    else:
        retVal = imf_dfx_parser.getMediaStatisticsOutput()
        while (len(tokenList)  > 0):
            payloadTokenListSize = min (10, len(tokenList))
            payloadTokenList = tokenList[:payloadTokenListSize]
            inputData = imf_dfx_parser.getMediaStatisticsInput(payloadType=SMALL_PAYLOAD, transferType=0, tokenList = payloadTokenList)
            outputData = imf_dfx_parser.getMediaStatisticsOutput()
            ret = imf.executeModuleAutoFill(funcName=FunctionName.GET_MEDIA_STATISTICS, params=inputData, outputObject=outputData,
                                        sxp=device, mailbox=mailbox, timeout=timeout, logging=False)
            if (ret == False):
                log.error("ERROR -> Failed to execute GET_MEDIA_STATISTICS through injection module framework")
                return False

            if (ret['status'] != 0):
                log.error("ERROR -> GET_MEDIA_STATISTICS failed with mailbox status code %s" % mbStatCodes.get([ret['status']]))
                return False

            response = ret['result']
            retVal = retVal + response
            tokenList = tokenList[payloadTokenListSize:]

        if (logging == True):
            log.result(retVal)

        if (filename != None):
            retVal.toTextFile(filename=filename)

        return retVal

DIMM_INFO_OBJ = {
}

def imf_getDIMMInfo(device=None, mailbox='os', timeout=10, log=_log, ignoreCache=False):
    """
    Brief:
        Function to perform get dimm info utilizing injection module framework.

    Description:
        Function to perform get dimm info utilizing injection module framework.

    Argument(s):
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.
        log - log object
        ignoreCache - Ignoring cached info when True.

    Return Value(s):
        Dictionary containing dimmInfoOutput object and Mailbox status code returned by command.

    Related:
    -

    Author(s):
    Lu Sun
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    fwu = fwUtils.FwUtils()
    if device is None:
        device = fwu.sxpComponent.getAll()[0]
    deviceName = fwu.getSxpName(sxp)
    outputData = imf_dfx_parser.dimmInfoOutput()
    log.info("IMF_INFO: Getting DIMM INFO for %s" % deviceName)
    if ignoreCache == True or (deviceName not in DIMM_INFO_OBJ.keys()):
        ret = imf.executeModuleAutoFill(funcName=FunctionName.DIMM_INFO, outputObject = outputData, sxp=device, mailbox=mailbox, timeout=timeout)
        if (ret == False):
            log.error("IMF_ERROR: Failed to execute DIMM_INFO injection module command")
            return False
        elif (ret['status'] != 0x0):
            log.error("IMF_ERROR: DIMM_INFO command failed with status %s" % mbStatCodes.get(ret['status']))
            return False

        DIMM_INFO_OBJ[deviceName] = ret['result']

    return DIMM_INFO_OBJ[deviceName]


def getTokenGroups():
    return imf_dfx_parser.IMS_GROUPS


def imf_decodeMedia(device=None, matrix=False, ranks=None, mailbox='os', timeout=10, log=_log):
    """
    Brief:
        Retrieves media types for all dies.

    Description:
        Calls Get Media Statistics injection module function in FW to obtain decoded media tokens for all dies.
        Parses data and to a human readable output representation.
        Note: Information is obtained post any trim override takes place (if applicable).

    Argument(s):
        device - SXP controller object
        matrix - When set to True, print layout is a rank/die matrix. Otherwise, layout is a list (Default=False).
        ranks  - When provided, only requested number of ranks are parsed. (Default=None ==> Auto discovery).
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.
        log - log object

    Return Value(s):
        MediaDecodeOutput on success
        False on failure

    Example:

        1. Request decoded media tokens and display in a list:
                fw.decodeMedia(device=sv.sxpcontroller020)

        2. Request decoded media tokens and display in a matrix:
                fw.decodeMedia(device=sv.sxpcontroller020, matrix=True)

    Related:
        -

    Author(s):
        Idan Porat
    """

    NUM_OF_CHARS_IN_LONG_TO_STRING = 16

    if ranks == None:
        dimmInfo = imf_getDIMMInfo(device = device, mailbox = mailbox, timeout = timeout, log = log)
        if dimmInfo == False:
            log.error("IMF_ERROR: Could not obtain DIMM info, assuming ranks=4")
            ranks = 4
        else:
            ranks = dimmInfo.ranks

    imsGroupsDict = getTokenGroups()
    tokens = []
    tokens.extend(imsGroupsDict['IMS_GROUP_MEDIA_DECODE_RANK0'])
    if ranks >= 2:
        tokens.extend(imsGroupsDict['IMS_GROUP_MEDIA_DECODE_RANK1'])
    if ranks == 4:
        tokens.extend(imsGroupsDict['IMS_GROUP_MEDIA_DECODE_RANK2'])
        tokens.extend(imsGroupsDict['IMS_GROUP_MEDIA_DECODE_RANK3'])
    # Remove repetitions
    tokens = list(set(tokens))
    tokens.sort()

    imsOutput = imf_getMediaStatistics(tokenList=tokens, device = device, mailbox = mailbox, timeout = timeout, log=log)
    if imsOutput == False:
        log.error("IMF_ERROR: Could not get Media Statistics")
        return False

    mediaTypesList = []

    # Build list of media types
    for token in tokens:
        value = imsOutput.getTokenValue(token)
        # Example: value == 0x0706050403020100 ---> ba = bytearray(b'\x07\x06\x05\x04\x03\x02\x01\x00')
        ba=bytearray.fromhex("{0:0{1}x}".format(value, NUM_OF_CHARS_IN_LONG_TO_STRING))
        ba.reverse()
        mediaTypesList.extend(list(ba))
    # return mediaTypesList
    mediaDecodeOutput = imf_dfx_parser.mediaDecodeOutput(mediaTypesList, matrix, ranks)

    return mediaDecodeOutput


def imf_writeIOCSR(count = None, bus = None, ioCSRValues = None, device=None, unlockDimm=True, mailbox='os', timeout=10, log=_log):
    """
    Brief:
        Function to perform Write IO CSR command using injection module framework.

    Description:
        Function to perform Write IO CSR command using injection module framework.

    Argument(s):
        count - Number of consecutive addresses to write. Currently, the supported range is 1-5.
        bus - SXP IO CSR = 0, DDRT IO CSR = 1
        ioCSRValues - List of IO CSR register values to write, max of 6 IO CSRs per mbox command.
        device - SXP controller object
        mailbox - Mailbox to use for command execution.
        timeout - Timeout to use for the command.
        log - log object

    Return Value(s):
        True - in case of success
        False - in case of any error.

    Example:
        import falconvalley.fw.imf.dfx.imf_dfx as imf_dfx
        imf_dfx.imf_writeIOCSR(count=3, bus=0, ioCSRValues = [[0x0, 0x200, 0x0, 26, 24, 1, 1], [0x0, 0x300, 0x0, 26, 24, 1, 1], [0x1, 0xC0C, 0x40, 27, 21, 0, 0]])

        or

        fw.writeIOCSR(count=3, bus=0, ioCSRValues = [[0x0, 0x200, 0x0, 26, 24, 1, 1], [0x0, 0x300, 0x0, 26, 24, 1, 1], [0x1, 0xC0C, 0x40, 27, 21, 0, 0]])

    Related:
    -

    Author(s):
        Lu Sun
    """
    from falconvalley.fw.imf.commands import imf_raw_utils as utils
    imf = imf_helper_cmd.ImfHelperCmds()

    if count < 1 or count > 5:
        log.error(ct.ERROR + "Invalid count value. Please make sure count is between 1 and 5.")
        return False

    if (bus != 0) and (bus != 1):
        log.error(ct.ERROR + "Invalid bus value. bus should be 0 for SXP IO CSR or 1 for DDRT IO CSR.")
        return False

    if not all(isinstance(entry, list) for entry in ioCSRValues):
        log.error(ct.ERROR + "Invalide input IO CSR Values. Please refer to example of this function for input format.")
        return False


    if len(ioCSRValues) > imf_dfx_parser.MAX_WRITE_IO_CSR_ENTRIES:
        log.error(ct.ERROR + "More than six IO CSR values provided. Current command supports only up to six values.")
        return False

    if ioCSRValues == None:
        log.error(ct.ERROR + "No IO CSR values provided.")
        return False

    entries = list();
    i = 0;

    # If no device is passed, we're assuming user wants to send command to first dimm in the system
    if device is None:
        device = sxpc.getAll()[0]

    if unlockDimm:
        device.unlock()

    for entry in ioCSRValues:
        if len(entry) != 7:
            log.error(ct.ERROR + "Each IO CSR needs seven parameters in the order of FUB, Offset, Value, End Bit, Start Bit, All Nibbles and All Ranks.")
            return False
        log.info(ct.INFO + "IO CSR Value %d: FUB = 0x%x, Offset = 0x%x, Value = 0x%x, End Bit = %d, Start Bit = %d, All Nibbles = %d, All ranks = %d.", i, entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6])
        ioCSRValue = imf_dfx_parser.writeIOCSRInputEntry(IO_CSR_FUB=entry[0], IO_CSR_Offset=entry[1], IO_CSR_Value=entry[2], IO_CSR_End_Bit=entry[3],
                 IO_CSR_Start_Bit=entry[4], IO_CSR_All_Nibbles=entry[5], IO_CSR_All_Ranks=entry[6])
        entries.append(ioCSRValue)
        i += 1

    inputData = imf_dfx_parser.writeIOCSRInput(count=count, bus=bus, ioCSRValuesEntries = entries)
    result = imf.executeModuleAutoFill(funcName=FunctionName.WRITE_IO_CSR, params=inputData, sxp=device,mailbox=mailbox, timeout=timeout)

    if result == False:
        return False

    if result['status']:
        log.error(ct.ERROR + "Module status 0x%x.", result['status'])
        return False

    log.result(ct.INFO + "Write IO CSR executed successfully.")
    return True

def imf_rankMarginTool(test, rankIndex, loopCount, numBurstsScale, numBursts, seqNum, device=None, mailbox='smbus', timeout=10, log=_log):
    """
    Brief:
        IMF rank margin tool function to execute the rank margin tool injection module command

    Argument(s):
        test: test number to execute
        device: sxp controller object
        mailbox: mailbox to send command through

    Return Value(s):
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    inputData = imf_dfx_parser.rankMarginToolInput(test=test, rankIndex=rankIndex, loopCount=loopCount, numBurstsScale=numBurstsScale,
                                                   numBursts=numBursts, seqNum=seqNum)
    outputData = imf_dfx_parser.rmtEntries()
    result = imf.executeModuleAutoFill(funcName=FunctionName.RANK_MARGIN_TOOL, params=inputData, outputObject=outputData, sxp=device,
                                       mailbox=mailbox, timeout=timeout)
    if result is False:
        log.error("%s failed to execute" % FunctionName.RANK_MARGIN_TOOL)
        return False

    if result['status'] != 0x0:
        log.error("%s failed with status %s" % (FunctionName.RANK_MARGIN_TOOL, mbStatCodes.get(result['status'])))
        return False

    return result['result']


def imf_resetFconfig(device=None, mailbox='smbus', timeout=10, log=_log):
    """
    Brief:
        Deletes FConfig entries from persistent store.

    Description:
        Once the user calls this routine and reboots the FConfig values in the compiled SRAM structure will be used (i.e. resetting to original values)

    Argument(s):
        device: sxp component object
        mailbox: mailbox to execute command through
        timeout: time to wait for command

    Return Value(s):
        True on success. False on failure.

    Example:
        imf_resetFconfig()

    Author(s):
        Marcus Yazzie, Mythili Srinivasan, Stephen (Bobby) Thompson
    """

    imf = imf_helper_cmd.ImfHelperCmds()
    result = imf.executeModuleAutoFill(sxp=device, funcName=FunctionName.RESET_FCONFIG, mailbox=mailbox, timeout=timeout, log=log)

    if result is False:
        return False

    if result['status']:
        log.error("IMF_ERROR: %s failed with status %s" % (FunctionName.RESET_FCONFIG, mbStatCodes.get(result['status'])))
        return False
    else:
        return True


def imf_getPowerThrottlingResult(device=None, mailbox='smbus', timeout=10, log=_log):
    """
    Brief:
        Retrieves power throttling result

    Description:
        Once user calls this command, power throttling result can be read from large payload region

    Argument(s):
        device: sxp component object
        mailbox: mailbox to execute command through
        timeout: time to wait for command

    Return Value(s):
        True on success. False on failure.

    Example:
        fw.getPowerThrottlingResult()

        import falconvalley.fw.imf.dfx.imf_dfx as imf_dfx
        imf_dfx.imf_getPowerThrottlingResult()

    Author(s):
        Lu Sun
    """

    imf = imf_helper_cmd.ImfHelperCmds()
    result = imf.executeModuleAutoFill(sxp=device, funcName=FunctionName.GET_POWER_THROTTLING_RESULT, mailbox=mailbox, timeout=timeout, log=log)

    if result is False:
        return False

    if result['status']:
        log.error("IMF_ERROR: %s failed with status %s" % (FunctionName.GET_POWER_THROTTLING_RESULT, mbStatCodes.get(result['status'])))
        return False
    else:
        return True

def imf_parseGetPowerThrottlingResult(inputList=None):
    """
    Brief:
        Interprets get power throttling result from large output payload

    Description:
        Interprets get power throttling result from large output payload

    Argument(s):
        inputList: list of 4 byte long integers read from large output payload after calling get power throttling result IMF command

    Return Value(s):
        Intepreted result on success.
        False on failure.

    Example:
        import falconvalley.fw.imf.dfx.imf_dfx as imf_dfx
        imf_dfx.imf_parseGetPowerThrottlingResult(inputList=myList)

        fw.parseGetPowerThrottlingResult(inputList=myList)


    Author(s):
        Lu Sun
    """
    if isinstance(inputList, list) == False:
        log.error("IMF_ERROR: inputList has to be type of list")
        return False

    # Convert list to byte array
    finalByteArray = bytearray()
    for i in range(0,len(inputList)):
        currentByteArray = bytearray(4)
        currentByteArray[0] = inputList[i] & 0xFF
        currentByteArray[1] = (inputList[i] >> 8) & 0xFF
        currentByteArray[2] = (inputList[i] >> 16) & 0xFF
        currentByteArray[3] = (inputList[i] >> 24) & 0xFF
        finalByteArray.extend(currentByteArray)

    outputByteArray = bytearray(1)
    outputByteArray[0] = 250
    outputByteArray.extend(finalByteArray)

    output = imf_dfx_parser.getPowerThrottlingResultOutput(buf=outputByteArray)
    return output

def imf_getLtecState(state, device=None, mailbox='smbus', timeout=10, log=_log):
    """
    Brief:
        Get the state data of LTEC feature.

    Description:
        Get the state data of the LTEC feature. Retrieves data specific to LTEC supported rails, and runtime state.

    Argument(s):
        device: sxp component object
        mailbox: mailbox to execute command through
        timeout: time to wait for command

    Return Value(s):
        GetLtecStateOutput buflist on success, False on failure to execute or failing status code.

    Example:
        import falconvalley.fw.imf.dfx.imf_dfx as imf_dfx
        imf_dfx.imf_getLtecState(device=sv.sxpcontroller020)

    Author(s):
        Stephen (Bobby) Thompson
    """
    imf = imf_helper_cmd.ImfHelperCmds()

    inputData = imf_dfx_parser.GetLtecStateInput(state=state)

    if inputData.state == imf_dfx_parser.LTEC_STATE_TOKENS.get("LTEC_RUNTIME_STATE"):
        outputData= imf_dfx_parser.GetLtecRuntimeStateOutput()
    elif inputData.state == imf_dfx_parser.LTEC_STATE_TOKENS.get("LTEC_RAIL_STATE"):
        outputData = imf_dfx_parser.GetLtecRailStateOutput()
    elif inputData.state == imf_dfx_parser.LTEC_STATE_TOKENS.get("LTEC_UPDATE_STATE"):
        outputData = imf_dfx_parser.GetLtecUpdateStateOutput()
    else:
        log.error("ERROR: Invalid state 0x%X" % state)
        return False

    result = imf.executeModuleAutoFill(sxp=device, funcName=FunctionName.GET_LTEC_STATE, params=inputData, outputObject=outputData, mailbox=mailbox, timeout=timeout, log=log)

    if result is False:
        log.error("IMF_ERROR: GET_LTEC_STATE failed to execute")
        return result

    if result['status'] != 0x0:
        log.error("IMF_ERROR: GET_LTEC_STATE failed with status code %s" % mbStatCodes.get(result['status']))
        return False

    return result['result']

def imf_triggerCapTest(device=None, mailbox='smbus', timeout=10, log=_log):
    """
    Brief:
        Triggers capapcitor self test in FW

    Description:
        Queues a message to FW to begin the cap test
        On a successful cap test, there will be no output. Check SMART
        health status to see if cap test has failed.

    Argument(s):
        device: sxp component object
        mailbox: mailbox to execute command through
        timeout: time to wait for command

    Return Value(s):
        None

    Example:
        import falconvalley.fw.imf.dfx.imf_dfx as imf_dfx
        imf_dfx.imf_triggerCapTest(device=sv.sxpcontroller020)

    Author(s):
        Daniel Garcia Briseno
    """
    imf = imf_helper_cmd.ImfHelperCmds()
    result = imf.executeModuleAutoFill(sxp=device, funcName=FunctionName.TRIGGER_CAP_TEST, mailbox=mailbox, timeout=timeout, log=log)

    if result is False:
        log.error("IMF_ERROR: TRIGGER_CAP_TEST failed to execute")
        return result

    if result['status'] != 0x0:
        log.error("IMF_ERROR: TRIGGER_CAP_TEST failed with status code %s" % mbStatCodes.get(result['status']))
        return False

    return result['result']
