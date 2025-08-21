from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators Elements
    LOCATOR_USERNAME_FIELD = (By.XPATH, "//*[@id='user-name']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "//*[@id='password']")
    LOCATOR_LOGIN_BUTTON = (By.XPATH, "//*[@id='login-button']")

    # Login URL
    URL = "https://www.saucedemo.com"

    def __init__(self, driver):
        super().__init__(driver)
        self.open_login_page()

    def open_login_page(self):
        self.driver.get(self.URL)

    def enter_username(self, username):
        self.fill_element(self.LOCATOR_USERNAME_FIELD, username)


    def enter_password(self, password):
        self.fill_element(self.LOCATOR_PASSWORD_FIELD, password)


    def click_login_button(self):
        self.click_element(self.LOCATOR_LOGIN_BUTTON)


    def login_as_standard_user(self):
        self.enter_username("standard_user")
        self.enter_password("secret_sauce")
        self.click_login_button()





