from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Basedriver:
    def __init__(self, driver):
        self.driver = driver
        
    def wait_until_element_is_visible(self, locator):
        wait = WebDriverWait(self.driver, timeout= 10)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element
    
    def click_on_element(self, locator):
        element = self.wait_until_element_is_visible(locator)
        element.click
        
    def send_keys(self, locator, input_text):
        element = self.wait_until_element_is_visible(locator)
        element.clear()
        element.send_keys(input_text)
        
    