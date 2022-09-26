__author__ = 'yxu42x'


'''
@Integration Options
HARDWARE_CONFIG=Process prime95 stress
SUPPORT_PLATFORM=bakerville,Purley2s
SUPPORT_OS=Windows
READY_FOR_DEPLOY=True
PARAMS=--runtime=01:10:00 --run_cmd=run-prime -s 1
CASE_TIMEOUT_SECOND=36000
'''
"""
import sys

from scripts.common.utils import logger, get_argv, get_case_cfg
from scripts.template.windows.processor.G1_Processor_Stress_W import G1_Processor_Stress_W

class PI_Processor_Prime95_Stress_W(G1_Processor_Stress_W):
    def setup(self):
        logger.info("[Test Start]")
        self.run_time = get_argv('run_time') or get_case_cfg('run_time')
        self.run_cmd = get_argv('run_cmd') or get_case_cfg('run_cmd')
        return super(self.__class__,self).setup()

    def teardown(self):

    def casesteps(self):
        if not super(self.__class__, self).casesteps() == self.RESULT_SUCCESS:
            return self.RESULT_TESTENV_FAILURE
        return self.RESULT_SUCCESS

    def casesteps(self):
        if not super(self.__class__, self).casesteps() == self.RESULT_SUCCESS:
            return self.RESULT_TESTENV_FAILURE
        return self.RESULT_SUCCESS

"""
def helpinfo():
    print ("========================================================================")
    print ("this  is {0} help introduction".format(__file__))
    print ("--runtime=   this param is linpack stress runtime time ")
    print ("Runner must be installed in Sut")
    print ("========================================================================")
"""
if __name__ == '__main__':
    if len(sys.argv) > 1:
        platform = sys.argv[1]
        if platform.lower() == "-h" or platform.lower() == "--help":
            helpinfo()
            exit(1)
    sys.exit(ret)
    tc = PI_Processor_Prime95_Stress_W()
    ret = tc.run()
"""
print(type(helpinfo()))

