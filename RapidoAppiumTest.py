import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
keycodes = {
    'a': 29, 'b': 30, 'c': 31, 'd': 32, 'e': 33, 'f': 34, 'g': 35, 'h': 36,
    'i': 37, 'j': 38, 'k': 39, 'l': 40, 'm': 41, 'n': 42, 'o': 43, 'p': 44,
    'q': 45, 'r': 46, 's': 47, 't': 48, 'u': 49, 'v': 50, 'w': 51, 'x': 52,
    'y': 53, 'z': 54, 'A': 29, 'B': 30, 'C': 31, 'D': 32, 'E': 33, 'F': 34,
    'G': 35, 'H': 36, 'I': 37, 'J': 38, 'K': 39, 'L': 40, 'M': 41, 'N': 42,
    'O': 43, 'P': 44, 'Q': 45, 'R': 46, 'S': 47, 'T': 48, 'U': 49, 'V': 50,
    'W': 51, 'X': 52, 'Y': 53, 'Z': 54, '0': 7, '1': 8, '2': 9, '3': 10,
    '4': 11, '5': 12, '6': 13, '7': 14, '8': 15, '9': 16, ' ': 62  # space
}




class TestRapido(unittest.TestCase):
    def setUp(self) -> None:
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "6ef16885"
        options.app_package = "com.rapido.passenger"
        options.no_reset = True
        options.auto_grant_permissions = True
        
        options.set_capability("waitForIdleTimeout", 0)
        
        try:
            self.driver = webdriver.Remote(
                command_executor="http://localhost:4723",
                options=options
            )
            
            
        except Exception as e:
            self.fail(f"Failed to initialize WebDriver: {e}")

    def tearDown(self) -> None:
        if hasattr(self, "driver") and self.driver:
            self.driver.quit()

    def type_text_using_keycodes(self,text):
        for char in text:
            if char in keycodes:
                self.driver.press_keycode(keycodes[char])  # Press the key for each character
            else:
                print(f"Keycode not found for: {char}")

    def test_rapido_flow(self) -> None:
        try:
        
            search_field = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("search_field")')
            search_field.click()
            time.sleep(2)

            
            drop_text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Double tap to enter Drop Location. Enter at least 3 characters to get suggestions below")
            drop_text.click()
            
            self.type_text_using_keycodes("Majestic Bus Stand")

            time.sleep(2)
            drop_location = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                               'new UiSelector().className("android.view.View").instance(7)')
            

            drop_location.click() 

            time.sleep(5)

            auto_select = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                               'new UiSelector().descriptionMatches("Get Auto.*")')
            auto_select.click()  # Tap on the element

             

            
          
            book_button = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                               'new UiSelector().description("Double tap to book Auto")')
            book_button.click()

            time.sleep(3)
            confirm_pickup = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("base_select_from_map_confirm_button")')
            self.assertTrue(confirm_pickup.is_displayed(), "Confirm Pickup text is not displayed")
            
            

        except Exception as e:
            # Print page source for debugging
            print("\n=== PAGE SOURCE ===")
            print("==================\n")
            self.fail(f"Test failed: {e}")

if __name__ == "__main__":
    unittest.main()