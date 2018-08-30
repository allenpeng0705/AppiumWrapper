import os
import unittest

from emaappiumclient.tests.ema.login.login import login
from emaappiumclient.tests.ema.queryFactory import queryFactory
from emaappiumclient.util.driver.driverFactory import driverFactory
from emaappiumclient.util.unittest.baseTest import baseTest
from emaappiumclient.util.unittest.testLoader import testLoader


class ssologin(baseTest):
    def filePath(self):
        return os.path.split(os.path.realpath(__file__))[0]

    def beginTest(self):
        pass

    def endTest(self):
        pass

    def test_ui(self):
        # click login button

        self.driver.waitForSeconds(2)
        query = queryFactory().getQuery()
        sso_login_btn = self.driver.findView(query.login_login_SSOBtn())
        self.driver.clickOnView(sso_login_btn)

        self.driver.waitForSeconds(3)
        filename = self.filePath() + "/" + "sso.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        imgBase64 = self.driver.page_base64(self.filePath(), 'sso')
        screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'sso')
        self.assertTrue(imgBase64 == screenshotBase64)

    def test_continue_btn(self):
        pass

    def test_last_test(self):
        pass

suite = testLoader().loadAllTestsFromClass(False, None, login)
suite = testLoader().loadAllTestsFromClass(False, None, ssologin)
unittest.TextTestRunner(verbosity=2).run(suite)
driverFactory().stopDriver()
