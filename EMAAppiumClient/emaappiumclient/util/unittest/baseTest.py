import unittest
import os
import pdb

from emaappiumclient.util.driver.driverFactory import driverFactory

class baseTest(unittest.TestCase):
    def __init__(self, needCreateDriver=True, methodName='runTest'):
        super(baseTest, self).__init__(methodName)
        self.needCreateDriver = needCreateDriver
        self.driver = None

    def setUp(self):
        if self.needCreateDriver:
            self.driver = driverFactory().createDriver()
        else:
            self.driver = driverFactory().getCurrentDriver()
            if self.driver is None:
                self.driver = driverFactory().createDriver()
        self.beginTest()

    def tearDown(self):
        self.endTest()
        if self.needCreateDriver:
            driverFactory().stopDriver()

    def beginTest(self):
        pass

    def endTest(self):
        pass

    '''
    def allTests(self, className, ):
        loader = unittest.TestLoader()
        test_names = loader.getTestCaseNames(className)
        if test_names == None:
            return None
    '''

        



