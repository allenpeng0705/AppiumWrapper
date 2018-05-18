import unittest
import os
import random
import string
import base64
from appium.webdriver.common.touch_action import TouchAction
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
# from selenium.webdriver.common.keys import Keys
import urllib2
import json
from time import sleep
#from emaappiumclient.conf.globalconf import emaconfiguration
from emaappiumclient.util.driver.driver import driver
from emaappiumclient.util.driver.driverFactory import driverFactory
from emaappiumclient.util.unittest.baseTest import baseTest
from emaappiumclient.util.unittest.testLoader import testLoader

def str_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class sample01(baseTest):

    def beginTest(self):
        # set up appium
        # ** Important Note **
        # Make sure you have build the UICatalog applcation in your local repository
        #app = os.path.join(os.path.dirname(__file__),
        #                   '../../apps/UICatalog.zip')
        #app = os.path.abspath(app)
        self._values = []

    def endTest(self):
        pass

    def _open_menu_position(self, index):
        # Opens up the menu at position [index] : starts at 0.
        table = self.driver.driver.find_element_by_class_name("XCUIElementTypeTable")
        self._row = table.find_elements_by_class_name("XCUIElementTypeTableCell")[index]
        self._row.click()

    def test_find_element(self):
        # first view in UICatalog is a table
        table = self.driver.driver.find_element_by_class_name("XCUIElementTypeTable")
        self.assertIsNotNone(table)

        # is number of cells/rows inside table correct
        rows = table.find_elements_by_class_name("XCUIElementTypeTableCell")
        self.assertEqual(18, len(rows))

        # is first one about buttons
        self.assertEqual(rows[0].get_attribute("name"), "Action Sheets")

        # there is nav bar inside the app
        nav_bar = self.driver.driver.find_element_by_class_name("XCUIElementTypeNavigationBar")
        self.assertTrue(nav_bar)

    def test_frames(self):
        # go into webview frame
        self._open_menu_position(15)

        # get the contexts and switch to webview
        contexts = self.driver.driver.contexts
        self.assertEqual([u'NATIVE_APP', u'WEBVIEW_1'], contexts)
        self.driver.driver.switch_to.context(contexts[1])

        # Find the store link
        sleep(4) # let the page load, perhaps
        logo = self.driver.driver.find_element_by_xpath('//*/UIATextField[@value="http://apple.com"]')
        self.assertIsNotNone(logo)

        # leave the webview
        self.driver.driver.switch_to.context(contexts[0])

        # Verify we are out of the webview
        scroll_after = self.driver.driver.find_element_by_class_name("XCUIElementTypeScrollView")
        self.assertTrue(scroll_after)

    def test_location(self):
        # get third row location
        row = self.driver.driver.find_elements_by_class_name("XCUIElementTypeTableCell")[2]
        self.assertEqual(row.location['x'], 0)
        self.assertEqual(row.location['y'], 178.8125)

    def test_screenshot(self):
        # make screenshot and get is as base64
        screenshot = self.driver.takeScreenshotAsPNGData()
        self.assertTrue(screenshot)
        #base64data = base64.b64decode(screenshot)
        imgfile = file('screenshot.png', 'wb')
        imgfile.write(screenshot)
        imgfile.close()


        # make screenshot and save it to the local filesystem
        success = self.driver.takeScreenshotAsPNGFileByPath('/Users/allenpeng/Desktop/uitest/foo.png')
        self.assertTrue(success)
        #self.assertTrue(os.path.isfile("foo.png"))

        # get rid of the file
        #os.remove("foo.png")

    def test_text_field_edit(self):
        # go to the text fields section
        self._open_menu_position(13)

        text_field = self.driver.driver.find_elements_by_class_name("XCUIElementTypeTextField")[0]

        # get default/empty text
        default_val = text_field.get_attribute("value")

        # write some random text to element
        rnd_string = str_generator()
        text_field.send_keys(rnd_string)
        self.assertEqual(text_field.get_attribute("value"), rnd_string)

        # clear and check if is empty/has default text
        text_field.clear()
        self.assertEqual(text_field.get_attribute("value"), default_val)

    def test_alert_interaction(self):
        # go to the alerts section
        self.driver.driver.find_element_by_name('Alert Views').click()
        
        triggerOk = self.driver.driver.find_element_by_accessibility_id("Simple")

        # TOFIX: Looks like alert object is not proper state
        # something to do with UIActionSheet vs. UIAlertView?
        # triggerOk = elements[0]
        triggerOk.click()
        alert = self.driver.driver.switch_to_alert()

        # dismiss alert
        alert.accept()

        # trigger modal alert with cancel & ok buttons
        triggerOkCancel = self.driver.driver.find_element_by_accessibility_id("Okay / Cancel")
        triggerOkCancel.click()
        alert = self.driver.driver.switch_to_alert()

        # check if title of alert is correct
        self.assertEqual(alert.text, "A Short Title Is Best A message should be a short, complete sentence.")
        alert.accept()

    def test_slider(self):
        # go to controls
        self._open_menu_position(10)

        # get the slider
        slider = self.driver.driver.find_element_by_class_name("XCUIElementTypeSlider")
        self.assertEqual(slider.get_attribute("value"), "42%")

        slider.set_value(0)
        self.assertEqual(slider.get_attribute("value"), "0%")

    def test_sessions(self):
        data = json.loads(urllib2.urlopen("http://localhost:4723/wd/hub/sessions").read())
        self.assertEqual(self.driver.driver.session_id, data['sessionId'])

    def test_size(self):
        table = self.driver.driver.find_element_by_class_name("XCUIElementTypeTable").size
        row = self.driver.driver.find_elements_by_class_name("XCUIElementTypeTableCell")[0].size
        self.assertEqual(table['width'], row['width'])
        self.assertNotEqual(table['height'], row['height'])

    def test_source(self):
        # get main view soruce
        source_main = self.driver.driver.page_source
        self.assertIn("XCUIElementTypeTable", source_main)
        self.assertIn("Text Fields", source_main)

        # got to text fields section
        self._open_menu_position(13)
        sleep(10)
        source_textfields = self.driver.driver.page_source
        self.assertIn("XCUIElementTypeStaticText", source_textfields)
        self.assertIn("Text Fields", source_textfields)

        self.assertNotEqual(source_main, source_textfields)

# suite = unittest.TestSuite()
# suite.addTest(samp le01(False,'test_find_element'))
# suite.addTest(sample01(False,'test_frames'))
# suite.addTest(sample01(False,'test_location'))
# suite.addTest(sample01(False,'test_screenshot'))
# suite.addTest(sample01(False,'test_text_field_edit'))
# suite.addTest(sample01(False,'test_alert_interaction'))
# suite.addTest(sample01(False,'test_slider'))
# suite.addTest(sample01(False,'test_sessions'))
# suite.addTest(sample01(False,'test_size'))
# suite.addTest(sample01(False,'test_source'))

suite1 = testLoader().loadAllTestsFromClass(True, None, sample01)
unittest.TextTestRunner(verbosity=2).run(suite1)

 