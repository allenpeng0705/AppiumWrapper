import os
import unittest

from emaappiumclient.tests.ema.queryFactory import queryFactory
from emaappiumclient.util.driver.driverFactory import driverFactory
from emaappiumclient.util.unittest.baseTest import baseTest
from emaappiumclient.util.unittest.testLoader import testLoader


class welcome(baseTest):
    def filePath(self):
        return os.path.split(os.path.realpath(__file__))[0]

    def beginTest(self):
        pass

    def endTest(self):
        pass

    def test_ui(self):
        self.driver.waitForSeconds(2)

        welcome.allow_permission(self)

        # save welcome png.
        filename = self.filePath() + "/" + "welcome.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        imgBase64 = self.driver.page_base64(self.filePath(), 'welcome')
        screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'welcome')

        self.assertTrue(imgBase64 == screenshotBase64)

    def test_login_btn(self):
        query = queryFactory().getQuery()
        # click login button
        login_btn = self.driver.findView(query.login_welcome_loginBtn())
        self.driver.clickOnView(login_btn)
        self.driver.waitForSeconds(2)
        # save login page
        filename = self.filePath() + "/" + "login.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)
        # contrast
        imgBase64 = self.driver.page_base64(self.filePath(), 'login')
        screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'login')
        self.assertTrue(imgBase64 == screenshotBase64)
        # click back
        back_btn = self.driver.findView(query.login_login_backBtn())
        self.driver.clickOnView(back_btn)

        """
        queryDict = queryFactory().getQuery().login_login_SSOBtn()
        sso_btn = self.driver.findView(queryDict)
        self.assertTrue(sso_btn != None)
        driverFactory().stopDriver()
        """

    """
    def test_start_using_btn(self):
        queryDict = queryFactory().getQuery().login_welcome_startUsingBtn()
        startUsing_btn = self.driver.findView(queryDict)
        self.driver.clickOnView(startUsing_btn)
        
        self.driver.waitForSeconds(5)
        filename = self.filePath() + "/" + "anonymousMain.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        imgBase64 = self.driver.page_base64(self.filePath(), 'anonymousMain')
        screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'anonymousMain')
        self.assertTrue(imgBase64 == screenshotBase64)
    """

    def allow_permission(self):
        # permission allow
        if self.driver.name == "EMA Android driver":
            queryDict = queryFactory().getQuery().app_permission_allow()
            if self.driver.viewIsVisibily(queryDict):
                app_permission_allow = self.driver.findView(queryDict)
                if app_permission_allow is not None:
                    self.driver.clickOnView(app_permission_allow)
                    self.driver.waitForSeconds(2)
        else:
            pass


suite = testLoader().loadAllTestsFromClass(False, None, welcome)
unittest.TextTestRunner(verbosity=2).run(suite)
driverFactory().stopDriver()
