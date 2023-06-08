from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find_element_by_id(self, id):
        try:
            self.wait.until(EC.presence_of_element_located((MobileBy.ID, id)))
            elem = self.driver.find_element(AppiumBy.ID, id)
            return elem
        except TimeoutException:
            raise TimeoutException("There isn't such element")
    
    def find_element_by_text(self, text):
        try:
            self.wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')))
            elem = self.driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value=f'new UiSelector().text("{text}")')        
            return elem
        except TimeoutException:
            raise Exception("There ins't such element")
        
    def find_element_by_resource_id(self, resource_Id):
        try:                     
            elem = self.wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("{resource_Id}")')))        
            return elem
        except TimeoutException:
            raise Exception("There ins't such element")

    def click_element(self, elem):
        elem.click()
    
    def fill_field(self, elem, data):
        elem.send_keys(data)