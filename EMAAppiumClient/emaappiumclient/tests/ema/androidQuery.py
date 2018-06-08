from emaappiumclient.tests.ema.query import query

class androidQuery(query):
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
    def app_permission_allow(self):
        return {
            'Platform': 'android',
            'Type': 'AndroidResourceID',
            'QueryString': 'com.android.packageinstaller:id/permission_allow_button'
        }

    def login_welcome_loginBtn(self):
        return {
            'Platform': 'android',
            'Type': 'AndroidResourceID',
            'QueryString': "com.everbridge.mobile.iv.recipient:id/tv_login"
        }

    def login_welcome_startUsingBtn(self):
        pass

    def login_login_SSOBtn(self):
        return {
            'Platform': 'android',
            'Type': 'AndroidResourceID',
            'QueryString': "com.everbridge.mobile.iv.recipient:id/enter_sso_tv"
        }

    def login_login_backBtn(self):
        return {
            'Platform': 'android',
            'Type': 'AndroidResourceID',
            'QueryString': "com.everbridge.mobile.iv.recipient:id/top_left_action_tv"
        }
    
    def login_sso_backBtn(self):
        return {
            'Platform': 'android',
            'Type': 'AndroidResourceID',
            'QueryString': "com.everbridge.mobile.iv.recipient:id/top_left_action_tv"
        }

    def login_login_username(self):
        return {
            'Platform': 'android',
            'Type': 'AndroidResourceID',
            'QueryString': "com.everbridge.mobile.iv.recipient:id/edt_username"
        }

    def login_login_pwd(self):
        return {
            'Platform': 'android',
            'Type': 'AndroidResourceID',
            'QueryString': "com.everbridge.mobile.iv.recipient:id/edt_password"
        }





