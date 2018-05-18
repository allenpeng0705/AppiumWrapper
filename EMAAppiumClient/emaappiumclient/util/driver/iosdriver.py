from emaappiumclient.util.driver.driver import driver
from emaappiumclient.conf.globalconf import emaconfiguration
from appium import webdriver

class iosdriver (driver):
        
    def __init__(self):
        self.name = "EMA iOS driver"
        conf = emaconfiguration()
        desired_caps = conf.getCapabilities()
        url = conf.getAppiumServerURL()
        self.driver = webdriver.Remote(url, desired_caps)

    def performTouchIDOnSimulator(self, okOrFail):
        if self.driver is not None:
            self.driver.touch_id(okOrFail)

    def toggleTouchIDEnrollmentOnSimulator(self):
        if self.driver is not None:
            self.driver.toggle_touch_id_enrollment()

    
    


