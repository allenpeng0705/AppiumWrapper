from appium import webdriver

from emaappiumclient.conf.globalconf import emaconfiguration
from emaappiumclient.util.driver.driver import driver


class androiddriver(driver):
    def __init__(self):
        self.name = "EMA Android driver"
        conf = emaconfiguration()
        desired_caps = conf.getCapabilities()
        url = conf.getAppiumServerURL()
        self.driver = webdriver.Remote(url, desired_caps)

    def startActivity(self, packageName, activityName):
        if packageName is not None and activityName is not None:
            self.driver.start_activity(packageName, activityName)

    def getCurrentActivity(self):
        if self.driver is not None:
            return self.driver.current_activity()
        else:
            return None

    def getCurrentPackage(self):
        if self.driver is not None:
            return self.driver.current_package()
        else:
            return None

    def getTestCoverage(self, broadcastIntent, ecFilePath):
        if self.driver is not None and broadcastIntent is not None and ecFilePath is not None:
            self.driver.end_test_coverage(broadcastIntent, ecFilePath)

    def lockDevice(self):
        if self.driver is not None:
            self.driver.lock(100)

    # def unLockDevice(self):
    #     if self.driver != None:
    #         self.driver.unlock()

    def toggleLocationService(self):
        if self.driver is not None:
            self.driver.toggle_location_services()

    def pressKey(self, keycode):
        if self.driver is not None:
            self.driver.press_keycode(keycode)

    def longPressKey(self, keycode):
        if self.driver is not None:
            self.driver.long_press_keycode(keycode)

    def openNotificationsOnEmulator(self):
        if self.driver is not None:
            self.driver.open_notifications()
