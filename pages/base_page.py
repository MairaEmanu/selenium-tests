from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver


    def is_element_present(self, locator):
        return WebDriverWait(self.driver,self.TIMEOUT).until(EC.presence_of_element_located(locator))


    def wait_for_element_to_be_clickable(self, locator):
        return WebDriverWait(self.driver,self.TIMEOUT).until(EC.element_to_be_clickable(locator))


    def quit_browser(self):
        self.driver.quit()


    def fill_element(self,locator_element, text):
        try:
            element = self.wait_for_element_to_be_clickable(locator_element)
        except TimeoutException as e:
            raise TimeoutException(f"An {e} occurred with Element: locator {locator_element}. Couldn't fill in element")
        else:
            element.clear()
            element.send_keys(text)


    def click_element(self, locator_element):
        try:
            element = self.wait_for_element_to_be_clickable(locator_element)
        except TimeoutException as e:
            raise TimeoutException(f"An {e} occurred with Element: locator {locator_element}. Couldn't click element")
        else:
            element.click()
