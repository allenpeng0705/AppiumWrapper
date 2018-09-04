import os
import unittest

from emaappiumclient.tests.ema.queryFactory import queryFactory
from emaappiumclient.util.driver.driverFactory import driverFactory
from emaappiumclient.util.unittest.baseTest import baseTest
from emaappiumclient.util.unittest.testLoader import testLoader


class messageList(baseTest):
    def filePath(self):
        return os.path.split(os.path.realpath(__file__))[0]

    def beginTest(self):
        pass

    def endTest(self):
        pass

    def test_ui(self):
        self.driver.waitForSeconds(10)
        filename = self.filePath() + "/" + "messageList.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        self.driver.waitForSeconds(10)
        imgBase64 = self.driver.page_base64(self.filePath(), 'messageList')
        screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'messageList')
        self.assertTrue(imgBase64 == screenshotBase64)
        pass

    def test_menu_ui(self):
        # click login button

        self.driver.waitForSeconds(13)

        query = queryFactory().getQuery()
        left_menu = self.driver.findView(query.top_bar_menu())
        self.driver.clickOnView(left_menu)

        self.driver.waitForSeconds(3)
        filename = self.filePath() + "/" + "left_menu.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        self.driver.waitForSeconds(5)
        # query = queryFactory().getQuery()
        # messageList = self.driver.findView(query.msg_messages_list())

        self.driver.swipe(800, 1200, 800, 400, 500)

        # touchActions = self.driver.moveTo(200, 400, touchActions,True)
        # self.driver.touchUp(200, 400, touchActions)
        filename = self.filePath() + "/" + "scroolTo.png"
        self.driver.takeScreenshotAsPNGFileByPath(filename)

        # self.driver.waitForSeconds(2)
        # message_item = self.driver.findView(query.menu_messages_item())
        # self.driver.clickOnView(message_item)
        #
        # self.driver.waitForSeconds(12)
        # messageList = self.driver.findView(query.msg_messages_list())
        # self.driver.scroolOnView(messageList, 200, 120, None, False)

        self.driver.waitForSeconds(10)
        # imgBase64 = self.driver.page_base64(self.filePath(), 'left_menu')
        # screenshotBase64 = self.driver.screenshot_base64(self.filePath(), 'left_menu')
        # self.assertTrue(imgBase64 == screenshotBase64)
        pass

    def test_last_test(self):
        pass


suite = testLoader().loadAllTestsFromClass(False, None, messageList)
unittest.TextTestRunner(verbosity=2).run(suite)
driverFactory().stopDriver()
