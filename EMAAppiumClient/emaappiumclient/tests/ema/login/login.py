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
from welcome import welcome


class login(baseTest):
    def filePath(self):
        return os.path.split(os.path.realpath(__file__))[0]

    def beginTest(self):
        pass

    def endTest(self):
        pass

    def test_ui(self):
        self.driver.waitForSeconds(5)
        filename = self.filePath() + "/" + "login.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        imgBase64 = self.driver.page_base64(self.filePath(), 'login')
        screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'login')
        self.assertTrue(imgBase64 == screenshotBase64)

    def test_sso_btn(self):
        queryDict = queryFactory().getQuery().login_login_SSOBtn()
        sso_btn = self.driver.findView(queryDict)
        self.driver.clickOnView(sso_btn)
        self.driver.waitForSeconds(5)
        filename = self.filePath() + "/" + "sso.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        imgBase64 = self.driver.page_base64(self.filePath(), 'sso')
        screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'sso')

        query_dict = queryFactory().getQuery().login_sso_backBtn()
        back_btn = self.driver.findView(query_dict)
        self.driver.clickOnView(back_btn)

        self.assertTrue(imgBase64 == screenshotBase64)        

    def test_last_test(self):
        pass


suite = testLoader().loadAllTestsFromClass(False, None, welcome)
suite = testLoader().loadAllTestsFromClass(False, suite, login)
unittest.TextTestRunner(verbosity=2).run(suite)
driverFactory().stopDriver()