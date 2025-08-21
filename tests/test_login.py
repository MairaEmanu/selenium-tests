from selenium import webdriver
import pytest
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.click_login_button()
    login_page.login_as_standard_user()

    assert "inventory" in driver.current_url
