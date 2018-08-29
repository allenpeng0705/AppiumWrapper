import os
import unittest

from emaappiumclient.tests.ema.queryFactory import queryFactory
from emaappiumclient.util.driver.driverFactory import driverFactory
from emaappiumclient.util.unittest.baseTest import baseTest
from emaappiumclient.util.unittest.testLoader import testLoader


class anonymousLocal(baseTest):
    def filePath(self):
        return os.path.split(os.path.realpath(__file__))[0]

    def beginTest(self):
        pass

    def endTest(self):
        pass

    def test_ui(self):
        # click login button

        self.driver.waitForSeconds(3)
        filename = self.filePath() + "/" + "local.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        self.driver.waitForSeconds(2)

        # imgBase64 = self.driver.page_base64(self.filePath(), 'local')
        # screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'local')
        # self.assertTrue(imgBase64 == screenshotBase64)
        pass

    def test_menu_ui(self):
        # click login button

        self.driver.waitForSeconds(3)

        query = queryFactory().getQuery()
        left_menu = self.driver.findView(query.top_bar_menu())
        self.driver.clickOnView(left_menu)

        self.driver.waitForSeconds(2)
        filename = self.filePath() + "/" + "left_menu.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        self.driver.waitForSeconds(2)
        local_item = self.driver.findView(query.menu_local_item())
        self.driver.clickOnView(local_item)

        # imgBase64 = self.driver.page_base64(self.filePath(), 'left_menu')
        # screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'left_menu')
        # self.assertTrue(imgBase64 == screenshotBase64)
        pass

    def test_last_test(self):
        pass


suite = testLoader().loadAllTestsFromClass(False, None, anonymousLocal)
unittest.TextTestRunner(verbosity=2).run(suite)
driverFactory().stopDriver()
