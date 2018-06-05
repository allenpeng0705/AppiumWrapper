import os
import time
import shutil
import base64
from appium import webdriver
from selenium.webdriver import TouchActions
from appium.webdriver.common.multi_action import MultiAction
from emaappiumclient.conf.globalconf import emaconfiguration

class driver (object):

    def __init__(self):
        self.name = "EMA appium client"
        self.driver = None

    def quit(self):
        if self.driver is not None:
            self.driver.quit()

    def capabilities(self):
        if self.driver is not None:
            return self.driver.desired_capabilities()
        return None

    def takeScreenshotAsBase64String(self):
        if self.driver is not None:
            return self.driver.get_screenshot_as_base64()
        return None

    def takeScreenshotAsPNGData(self):
        if self.driver is not None:
            return self.driver.get_screenshot_as_png()
        return None

    def takeScreenshotAsPNGFile(self, filename):
        if self.driver is not None:
            if filename is not None:
                return self.driver.get_screenshot_as_file(filename)
            else:
                return False
        return False

    def takeScreenshotAsPNGFileByPath(self, filepath):
        if self.driver is not None and filepath is not None:
            png_data = self.takeScreenshotAsPNGData()
            if png_data is not None:
                isabspath = os.path.isabs(filepath)
                abs_path = filepath
                if not isabspath:
                    abs_path = os.path.abspath(filepath)
                dir_name = os.path.split(abs_path)
                path = dir_name[0]
                name = dir_name[1]

                if os.path.exists(path) == False:
                    os.mkdir(path)

                path = path + "/screenshots"
                if os.path.exists(path) == False:
                    os.mkdir(path)

                if emaconfiguration.platform == 'iOS':
                    path = path + "/iOS"
                elif emaconfiguration.platform == 'android':
                    path = path + "/android"

                if os.path.exists(path) == True:
                    file_path = path + "/" + name
                    if os.path.exists(file_path):
                        os.remove(file_path)
                else:
                    os.mkdir(path)

                workspace = os.getcwd()
                os.chdir(path)

                png_file = open(name, 'wb')
                png_file.write(png_data)
                png_file.close()
                os.chdir(workspace)
                return True
        return False

    def page_base64(self, filePath, pageName):
        platform = emaconfiguration.platform
        path = filePath + "/images/" + platform + "/" + pageName + ".png"
        with open(path, 'rb') as file:
            data = file.read()
            if data is None:
                return None
            return base64.b64encode(data)


    def screenshot_base64(self, filePath, screenshotName):
        platform = emaconfiguration.platform
        path = filePath + "/screenshots/" + platform + "/" + screenshotName + ".png"
        with open(path, 'rb') as file:
            data = file.read()
            if data is None:
                return None
            return base64.b64encode(data)

    def setPageLoadingTimeout(self, millsencondsTimeout):
        if self.driver is not None:
            self.driver.set_page_load_timeout(millsencondsTimeout)
            return True
        return False

    def setSearchingElementTimeout(self, millsencondsTimeout):
        if self.driver is not None:
            self.driver.implicitly_wait(millsencondsTimeout)
            return True
        return False

    def getCurrentOrientation(self):
        if self.driver is not None:
            return self.driver.orientation()
        return None

    def setCurrentOrientation(self, orientation):
        if self.driver is not None:
            self.driver.orientation = orientation
            return True
        return False

    def getCurrentLocation(self):
        if self.driver is not None:
            return self.driver.location()
        return None

    def setCurrentLocation(self, latitude, longitude, altitude):
        if self.driver is not None:
            self.driver.setLocation(latitude, longitude, altitude)
            return True
        return False

    def getLogType(self):
        if self.driver is not None:
            return self.driver.log_types()
        return None

    def getLogsByType(self, type):
        if self.driver is not None and type is not None:
            return self.driver.get_log(type)
        return None

    def installApp(self, appPath):
        if self.driver is not None and appPath is not None:
            self.driver.install_app(appPath)

    def uninstallApp(self, appPath):
        if self.driver is not None and appPath is not None:
            self.driver.remove_app(appPath)

    def isAppInstalled(self, appBundleID):
        if self.driver is not None and appBundleID is not None:
            return self.driver.install_app(appBundleID)
        return False

    def lanuchAppOrBringToForeground(self):
        if self.driver is not None:
            self.driver.launch_app()

    def sendAppToBackground(self, secondsDuration):
        if self.driver is not None:
            self.driver.background_app(secondsDuration)

    def killApp(self):
        if self.driver is not None:
            self.driver.close_app()

    def reset(self):
        if self.driver is not None:
            self.driver.reset()

    def appStrings(self, language, strFilePath):
        if self.driver is not None:
            return self.driver.app_strings(language, strFilePath)
        return None

    def createFileWithData(self, filePath, base64Data):
        if self.driver is not None and filePath is not None and base64Data is not None:
            self.driver.push_file(filePath, base64Data)

    def retrieveBase64DataFromFile(self, filePath):
        if self.driver is not None and filePath is not None:
            return self.driver.pull_file(filePath)
        return None

    def retrieveBase64DataFromFolderAsZip(self, folderPath):
        if self.driver is not None and folderPath is not None:
            return self.driver.pull_folder(folderPath)
        return None

    def vibrateDevice(self):
        if self.driver is not None:
            self.driver.shake()

    def hideKeyboard(self):
        if self.driver is not None:
            self.driver.hide_keyboard()

    def getCurrentTime(self):
        if self.driver is not None:
            return self.driver.device_time()
        return None

    """
    The unified interface for looking for UI elements on both iOS and android. You can search the view
    via AccessibilityID, ClassName, id, XPath, name, coordinates.
    We use one dictionary to encapsulate these parameters.
    {
        Platform: 'iOS' or 'android'
        DeviceModel: 'iPhone7', 'iPhoneX', 'Android8'  -- Optional
        Type: 'ClassName', 'AndroidResourceID', 'XPath', 'AccessbilityID', 'AndroidUIAutomator', 'iOSPredicateString', 'iOSClassChain'
        #############################################################################################################################################################################
        # ClassName: Available on both iOS and Android.
        # Eg. iOS: "XCUIElementTypeButton"
        #
        # AndroidResourceID: > Android 4.3    Recommended    ---> find_element_by_id
        # Eg. "package.name:id/android"
        #
        # XPath: Available on both Android and iOS. But not recommended on iOS. (too slow via XCTest). It's ok on Android
        # Eg.
        # Abs path: "className/className/className/className"
        # Relative path: "//className"
        # UI element index: "//className[index]"
        # UI element attribute: "//className[@label='more info']"
        # "//className[@label='more info'][@isVisible='1']"
        # "//className[contains(@label,'more')]"

        # AccessbilityID: Available on both Android and iOS    Recommended
        # Android: Using "content-desc" attribute
        # iOS: Using "accessbilityID", "label" or "name" attribute
        #
        # AndroidUIAutomator: > Android 4.2  Strongly recommended on Android
        # One or more attributes
        # Eg.  "new UiSelector().text(\"send\")", "new UiSelector().text(\"sending\").clickable(true)"
        #
        # iOSPredicateString  > iOS 10  Strongly recommended on iOS
        # One or more attributes
        # Eg. "type == 'XCUIElementTypeButton'",  "type == 'XCUIElementTypeButton' AND label == 'more info'"
        #
        # iOSClassChain   > iOS 10    Not mature
        # Implemented by https://github.com/appium/appium-xcuitest-driver/pull/391 for replacing XPath on > iOS10
        # Eg. 'XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeNavigationBar[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[2]'
        #
        # Recommended Chain: Android:AndroidUIAutomator > className = id = AccessibilityId > xpath iOS:iOSNsPredicateString > className = AccessibilityId
        #############################################################################################################################################################################

        QueryString: 'xxxxxx',    -- Value based on the above Type
        xPos:'',
        yPos:'',
    }
    """
    def findView(self, queryParameters):
        if self.driver is not None and queryParameters is not None:
            platform = ''
            deviceModel = ''
            type = ''
            queryString = ''
            if queryParameters.get('Platform'):
                platform = queryParameters['Platform']

            # DevicModel is optional
            if queryParameters.get('DeviceModel'):
                deviceModel = queryParameters['DeviceModel']

            if queryParameters.get('Type'):
                type = queryParameters['Type']

            if queryParameters.get('QueryString'):
                queryString = queryParameters['QueryString']

            if queryString == '' or queryString is None:
                return None

            if platform == 'iOS':
                if type not in ['ClassName', 'XPath', 'AccessbilityID', 'iOSPredicateString', 'iOSClassChain']:
                    return None

                if type == 'iOSPredicateString':
                    return self.driver.find_element_by_ios_predicate(queryString)

                if type == 'iOSClassChain':
                    return self.driver.find_element_by_ios_class_chain(queryString)

            elif platform == 'android':
                if type not in ['ClassName', 'XPath', 'AccessbilityID', 'AndroidResourceID', 'AndroidUIAutomator']:
                    return None

                if type == 'AndroidResourceID':
                    return self.driver.find_element_by_id(queryString)

                if type == 'AndroidUIAutomator':
                    return self.driver.find_element_by_android_uiautomator(queryString)
            else:
                return None

            if type == 'ClassName':
                return self.driver.find_element_by_class_name(queryString)

            if type == 'XPath':
                return self.driver.find_element_by_xpath(queryString)

            if type == 'AccessbilityID':
                return self.driver.find_element_by_accessibility_id(queryString)


        return None


    """
    The unified interface for looking for UI elements on both iOS and android. You can search the view
    via AccessibilityID, ClassName, id, XPath, name, coordinates.
    We use one dictionary to encapsulate these parameters.
    {
        Platform: 'iOS' or 'android'
        DeviceModel: 'iPhone7', 'iPhoneX', 'Android8'  -- Optional
        Type: 'ClassName', 'AndroidResourceID', 'XPath', 'AccessbilityID', 'AndroidUIAutomator', 'iOSPredicateString', 'iOSClassChain'
        #############################################################################################################################################################################
        # ClassName: Available on both iOS and Android.
        # Eg. iOS: "XCUIElementTypeButton"
        #
        # AndroidResourceID: > Android 4.3    Recommended    ---> find_element_by_id
        # Eg. "package.name:id/android"
        #
        # XPath: Available on both Android and iOS. But not recommended on iOS. (too slow via XCTest). It's ok on Android
        # Eg.
        # Abs path: "className/className/className/className"
        # Relative path: "//className"
        # UI element index: "//className[index]"
        # UI element attribute: "//className[@label='more info']"
        # "//className[@label='more info'][@isVisible='1']"
        # "//className[contains(@label,'more')]"

        # AccessbilityID: Available on both Android and iOS    Recommended
        # Android: Using "content-desc" attribute
        # iOS: Using "accessbilityID", "label" or "name" attribute
        #
        # AndroidUIAutomator: > Android 4.2  Strongly recommended on Android
        # One or more attributes
        # Eg.  "new UiSelector().text(\"send\")", "new UiSelector().text(\"sending\").clickable(true)"
        #
        # iOSPredicateString  > iOS 10  Strongly recommended on iOS
        # One or more attributes
        # Eg. "type == 'XCUIElementTypeButton'",  "type == 'XCUIElementTypeButton' AND label == 'more info'"
        #
        # iOSClassChain   > iOS 10    Not mature
        # Implemented by https://github.com/appium/appium-xcuitest-driver/pull/391 for replacing XPath on > iOS10
        # Eg. 'XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeNavigationBar[1]/XCUIElementTypeOther[1]/XCUIElementTypeButton[2]'
        #
        # Recommended Chain:Android:AndroidUIAutomator > className = id = AccessibilityId > xpath iOS:iOSNsPredicateString > className = AccessibilityId
        #############################################################################################################################################################################

        QueryString: 'xxxxxx',    -- Value based on the above Type

    }
    """
    def findViews(self, queryParameters):
        if self.driver is not None and queryParameters is not None:
            platform = ''
            deviceModel = ''
            type = ''
            queryString = ''
            if queryParameters.get('Platform'):
                platform = queryParameters['Platform']

            # DevicModel is optional
            if queryParameters.get('DeviceModel'):
                deviceModel = queryParameters['DeviceModel']

            if queryParameters.get('Type'):
                type = queryParameters['Type']

            if queryParameters.get('QueryString'):
                queryString = queryParameters['QueryString']

            if queryString == '' or queryString is None:
                return None

            if platform == 'iOS':
                if type not in ['ClassName', 'XPath', 'AccessbilityID', 'iOSPredicateString', 'iOSClassChain']:
                    return None

                if type == 'iOSPredicateString':
                    return self.driver.find_elements_by_ios_predicate(queryString)

                if type == 'iOSClassChain':
                    return self.driver.find_elements_by_ios_class_chain(queryString)

            elif platform == 'android':
                if type not in ['ClassName', 'XPath', 'AccessbilityID', 'AndroidResourceID', 'AndroidUIAutomator']:
                    return None

                if type == 'AndroidResourceID':
                    return self.driver.find_elements_by_id(queryString)

                if type == 'AndroidUIAutomator':
                    return self.driver.find_elements_by_android_uiautomator(queryString)
            else:
                return None

            if type == 'ClassName':
                return self.driver.find_elements_by_class_name(queryString)

            if type == 'XPath':
                return self.driver.find_elements_by_xpath(queryString)

            if type == 'AccessbilityID':
                return self.driver.find_elements_by_accessibility_id(queryString)

        return None

    def clickOnView(self, view):
        if view is not None:
            view.click()

    def sendText(self, view, text):
        if view is not None and text is not None:
            view.send_keys(text)

    def clearText(self, view):
        if view is not None:
            view.clear()

    def getText(self, view):
        if view is not None:
            return view.text
        return None

    def getName(self, view):
        if view is not None:
            return view.tag_name
        return None

    def getAttribute(self, view, attribute):
        if view is not None and attribute is not None:
            return view.get_attribute(attribute)
        return None

    def isSelected(self, view):
        if view is not None:
            return view.is_selected()
        return False

    def isEnabled(self, view):
        if view is not None:
            return view.is_enabled()
        return False

    def isDisplayed(self, view):
        if view is not None:
            return view.is_displayed()
        return False

    def locationOfView(self, view):
        if view is not None:
            return view.location
        return None

    def sizeOfView(self, view):
        if view is not None:
            return view.size
        return None

    def getWebElementCSSValue(self, view, cssKey):
        if view is not None and cssKey is not None:
            return view.getCssValue(cssKey)
        return None

    def getCurrentContext(self):
        return self.driver.current_context

    def getAllContexts(self):
        return self.driver.contexts

    def switchToContext(self, contextName):
        if contextName is not None:
            self.driver.switch_to.context(contextName)

    def tapOnView(self, view, touchActions = None, delayPerform = False):
        if view is not None:
            action = None
            if touchActions is None:
                action = TouchActions(self.driver)
            else:
                action = touchActions
            action.tap(view)
            if delayPerform == False:
                action.perform()
            return action
        return None

    def doubleTapOnView(self, view, touchActions = None, delayPerform = False):
        if view is not None:
            action = None
            if touchActions is None:
                action = TouchActions(self.driver)
            else:
                action = touchActions
            action.double_tap(view)
            if delayPerform == False:
                action.perform()
            return action
        return None

    def longPressOnView(self, view, touchActions = None, delayPerform = False):
        if view is not None:
            action = None
            if touchActions is None:
                action = TouchActions(self.driver)
            else:
                action = touchActions
            action.long_press(view)
            if delayPerform == False:
                action.perform()
            return action
        return None

    def swipeOnView(self, view, xOffset, yOffset, speed, touchActions = None, delayPerform = False):
        if view is not None:
            action = None
            if touchActions is None:
                action = TouchActions(self.driver)
            else:
                action = touchActions
            action.flick_element(view, xOffset, yOffset, speed)
            if delayPerform == False:
                action.perform()
            return action
        return None

    def touchDown(self, xPos, yPos, touchActions = None, delayPerform = False):
        action = None
        if touchActions is None:
            action = TouchActions(self.driver)
        else:
            action = touchActions
        action.tap_and_hold(xPos, yPos)
        if delayPerform == False:
            action.perform()
            return action
        return None

    def touchUp(self, xPos, yPos, touchActions = None, delayPerform = False):
        action = None
        if touchActions is None:
            action = TouchActions(self.driver)
        else:
            action = touchActions
        action.release(xPos, yPos)
        if delayPerform == False:
            action.perform()
            return action
        return None

    def moveTo(self, xPos, yPos, touchActions = None, delayPerform = False):
        action = None
        if touchActions is None:
            action = TouchActions(self.driver)
        else:
            action = touchActions
        action.move(xPos, yPos)
        if delayPerform == False:
            action.perform()
            return action
        return None

    def scroolOnView(self, view, xOffset, yOffset, touchActions = None, delayPerform = False):
        action = None
        if touchActions is None:
            action = TouchActions(self.driver)
        else:
            action = touchActions
        action.scroll_from_element(view, xOffset, yOffset)
        if delayPerform == False:
            action.perform()
            return action
        return None

    def scroolTo(self, xOffset, yOffset, touchActions = None, delayPerform = False):
        action = None
        if touchActions is None:
            action = TouchActions(self.driver)
        else:
            action = touchActions
        action.scroll(xOffset, yOffset)
        if delayPerform == False:
            action.perform()
            return action
        return None

    def multiTouchPerform(self, *touchs):
        ma = MultiAction(self.driver)
        for touch in touchs:
            ma.add(touch)
        ma.perform()

    def waitForSeconds(self, seconds):
        time.sleep(seconds)
