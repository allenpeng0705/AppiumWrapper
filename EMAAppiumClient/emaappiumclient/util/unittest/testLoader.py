import unittest
import sys
from emaappiumclient.util.unittest.baseTest import baseTest

class testLoader(unittest.TestLoader):
    def loadAllTestsFromClass(self, needCreateDriver, testSuite, testCaseClass):
        """Return a suite of all tests cases contained in testCaseClass"""
        if not issubclass(testCaseClass, baseTest):
            raise TypeError("Test cases should be derived from baseTest." \
                                " Maybe you meant to derive from baseTest?")
        testCaseNames = self.getTestCaseNames(testCaseClass)
        if testCaseNames is not None and hasattr(testCaseClass, 'runTest'):
            testCaseNames = ['runTest']
  
        if testSuite is None:
            testSuite = unittest.TestSuite()

        if 'test_ui' in testCaseNames:
            uicase = testCaseClass(needCreateDriver, 'test_ui')
            testSuite.addTest(uicase)

        hasLastTest = False
        if 'test_last_test' in testCaseNames:
            hasLastTest = True
               
        for casename in testCaseNames:
            #case = globals()[testCaseClass](needCreateDriver, casename)
            if casename == 'test_ui' or casename == 'test_last_test':
                continue
            case = testCaseClass(needCreateDriver, casename)
            testSuite.addTest(case)

        if hasLastTest == True:
            case = testCaseClass(needCreateDriver, 'test_last_test')
            testSuite.addTest(case)

        return testSuite

    def loadAllTestsFromClasses(self, needCreateDriver, testSuite, *testCaseClasses):
  
        if testSuite is None:
            testSuite = unittest.TestSuite()

        for case_class in testCaseClasses:
            self.loadAllTestsFromClass(needCreateDriver, testSuite, case_class)

        return testSuite

    def loadSpecialTestsFromClass(self, testSuite, testCaseClass, *cases):
        """case is organized by tuple (test_method_name, needCreateDriver)"""
        if not issubclass(testCaseClass, baseTest):
            raise TypeError("Test cases should be derived from baseTest." \
                                " Maybe you meant to derive from baseTest?")
  
        if testSuite is None:
            testSuite = unittest.TestSuite()
        for case in cases:
            #case = globals()[testCaseClass](needCreateDriver, casename)
            testCaseNames = self.getTestCaseNames(testCaseClass)
            if case[0] not in testCaseNames:
                raise TypeError("Test case must be one test function of testCaseClass!")
            testcase = testCaseClass(case[1], case[0])
            testSuite.addTest(testcase)

        return testSuite



 

