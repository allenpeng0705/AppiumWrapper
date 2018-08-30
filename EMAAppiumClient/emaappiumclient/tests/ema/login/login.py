import os
import unittest

from emaappiumclient.tests.ema.login.welcome import welcome
from emaappiumclient.tests.ema.queryFactory import queryFactory
from emaappiumclient.util.driver.driverFactory import driverFactory
from emaappiumclient.util.unittest.baseTest import baseTest
from emaappiumclient.util.unittest.testLoader import testLoader


class login(baseTest):
    def filePath(self):
        return os.path.split(os.path.realpath(__file__))[0]

    def beginTest(self):
        pass

    def endTest(self):
        pass

    def test_ui(self):
        self.driver.waitForSeconds(2)
        # click login button
        query = queryFactory().getQuery()
        login_btn = self.driver.findView(query.login_welcome_loginBtn())
        self.driver.clickOnView(login_btn)

        self.driver.waitForSeconds(3)
        filename = self.filePath() + "/" + "login.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        imgBase64 = self.driver.page_base64(self.filePath(), 'login')
        screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'login')
        self.assertTrue(imgBase64 == screenshotBase64)

    def test_sso_btn(self):
        self.driver.waitForSeconds(2)
        query = queryFactory().getQuery()
        sso_btn = self.driver.findView(query.login_login_SSOBtn())
        self.driver.clickOnView(sso_btn)
        self.driver.waitForSeconds(3)

        filename = self.filePath() + "/" + "sso.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        imgBase64 = self.driver.page_base64(self.filePath(), 'sso')
        screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'sso')
        self.assertTrue(imgBase64 == screenshotBase64)
        # click back
        back_btn = self.driver.findView(query.login_sso_backBtn())
        self.driver.clickOnView(back_btn)

    def test_last_test(self):
        pass

suite = testLoader().loadAllTestsFromClass(False, None, welcome)
suite = testLoader().loadAllTestsFromClass(False, suite, login)
unittest.TextTestRunner(verbosity=2).run(suite)
driverFactory().stopDriver()
