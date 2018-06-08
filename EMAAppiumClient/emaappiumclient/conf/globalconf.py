

from emaappiumclient.util.singletonDecorator import singletonDecorator

@singletonDecorator
class emaconfiguration (object):
    # can be iOS or android
    platform = 'android'
    appium_svr_url = 'http://127.0.0.1:4723/wd/hub'
    iOS_capabilities = {
        #'xcodeOrgId': 'VW379TB6DM',
        'xcodeOrgId': '4H3LPY68H3',
        'xcodeSigningId': 'iPhone Developer',
        'app': 'com.everbridge.mobile.iv.Recipient',
        #'app': 'com.example.apple-samplecode.UICatalog',
        'platformName': 'iOS',
        'platformVersion': '10.1',
        'deviceName': 'iPhone 6 Plus',
        'automationName': 'XCUITest',
        'udid': '15998d525356f11014af48923e7fc52c1a1c27b2'
        #"udid": "15a50f3cbae47b2e714f01746b11a6d878ee7e33"
    }

    android_capabilities = {
        "platformName": 'Android',
        "platformVersion": '7.0',
        "deviceName": 'Android Emulator',
        "appPackage": 'com.everbridge.mobile.iv.recipient',
        "appActivity": '.ui.SplashActivity',
        "unicodeKeyboard": True,
        "resetKeyboard": True

    }

    def __init__(self):
        self.name = "conf->global->configuration"

    def getCapabilities(self):
        if emaconfiguration.platform == 'iOS':
            return self.iOS_capabilities
        elif emaconfiguration.platform == 'android':
            return self.android_capabilities
        return {}

    def getAppiumServerURL(self):
        return emaconfiguration.appium_svr_url

