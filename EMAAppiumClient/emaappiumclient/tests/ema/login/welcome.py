import unittest
import os
import json
from time import sleep

from emaappiumclient.util.driver.driver import driver
from emaappiumclient.util.driver.driverFactory import driverFactory
from emaappiumclient.tests.ema.query import query
from emaappiumclient.tests.ema.queryFactory import queryFactory
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
        self.driver.waitForSeconds(5)
        # permission allow
        if self.driver.name == "EMA Android driver":
            queryDict = queryFactory().getQuery().app_permission_allow()
            app_permission_allow = self.driver.findView(queryDict)
            self.driver.clickOnView(app_permission_allow)

        # save welcome png.
        filename = self.filePath() + "/" + "welcome.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        imgBase64 = self.driver.page_base64(self.filePath(), 'welcome')
        screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'welcome')
        self.assertTrue(imgBase64 == screenshotBase64)

    def test_login_btn(self):
        queryDict = queryFactory().getQuery().login_welcome_loginBtn()
        login_btn = self.driver.findView(queryDict)
        self.driver.clickOnView(login_btn)
        self.driver.waitForSeconds(5)
        filename = self.filePath() + "/" + "login.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        imgBase64 = self.driver.page_base64(self.filePath(), 'login')
        screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'login')

        query_dict = queryFactory().getQuery().login_login_backBtn()
        back_btn = self.driver.findView(query_dict)
        self.driver.clickOnView(back_btn)

        self.assertTrue(imgBase64 == screenshotBase64)
        """
        queryDict = queryFactory().getQuery().login_login_SSOBtn()
        sso_btn = self.driver.findView(queryDict)
        self.assertTrue(sso_btn != None)
        driverFactory().stopDriver()
        """

    """
    def test_startuing_btn(self):
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


suite = testLoader().loadAllTestsFromClass(False, None, welcome)
unittest.TextTestRunner(verbosity=2).run(suite)
driverFactory().stopDriver()
