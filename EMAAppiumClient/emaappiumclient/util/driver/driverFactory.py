from emaappiumclient.util.driver.driver import driver
from emaappiumclient.util.driver.iosdriver import iosdriver
from emaappiumclient.util.driver.androiddriver import androiddriver
from emaappiumclient.conf.globalconf import emaconfiguration


class driverFactory (object):
    _instance = None
    _init_flag = False
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(driverFactory, cls).__new__(cls, *args, **kw)  
        return cls._instance 

    def __init__(self):
        if self._init_flag == False:
            self.name = "EMA driver factory"
            # Appium device driver
            self.currentDriver = None
            self._init_flag = True

    def createDriver(self):
        self.stopDriver()
        if emaconfiguration.platform == 'iOS':
            self.currentDriver = iosdriver()
        elif emaconfiguration.platform == 'android':
            self.currentDriver = androiddriver()
        return self.currentDriver

    def getCurrentDriver(self):
        return self.currentDriver

    def stopDriver(self):
        if self.currentDriver is not None:
            self.currentDriver.quit()
            del self.currentDriver
            self.currentDriver = None
    
    


    

