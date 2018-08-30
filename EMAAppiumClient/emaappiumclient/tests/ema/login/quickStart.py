import os
import unittest

from emaappiumclient.tests.ema.login.welcome import welcome
from emaappiumclient.tests.ema.queryFactory import queryFactory
from emaappiumclient.util.driver.driverFactory import driverFactory
from emaappiumclient.util.unittest.baseTest import baseTest
from emaappiumclient.util.unittest.testLoader import testLoader


class quickStart(baseTest):
    def filePath(self):
        return os.path.split(os.path.realpath(__file__))[0]

    def beginTest(self):
        pass

    def endTest(self):
        pass

    def test_ui(self):
        pass

    def test_startUsingNow_btn(self):
        self.driver.waitForSeconds(2)
        queryDict = queryFactory().getQuery().login_welcome_startUsingBtn()
        startUsing_btn = self.driver.findView(queryDict)
        self.driver.clickOnView(startUsing_btn)

        self.driver.waitForSeconds(3)
        filename = self.filePath() + "/" + "anonymousMain.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        imgBase64 = self.driver.page_base64(self.filePath(), 'anonymousMain')
        screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'anonymousMain')
        self.assertTrue(imgBase64 == screenshotBase64)

    def test_last_test(self):
        pass


suite = testLoader().loadAllTestsFromClass(False, None, welcome)
suite = testLoader().loadAllTestsFromClass(False, suite, quickStart)
unittest.TextTestRunner(verbosity=2).run(suite)
driverFactory().stopDriver()
