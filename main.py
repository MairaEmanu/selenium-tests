from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
URL = "https://www.saucedemo.com"
username_id ="user-name"
username = "standard_user"

password_id = "password"
password = "secret_sauce"

login_button_id = "login-button"

inventory_page_id = "inventory_container"

driver.get(URL)

username_field = driver.find_element(By.ID,username_id)
username_field.send_keys(username)
password_field = driver.find_element(By.ID, password_id)
password_field.send_keys(password)

login_button = driver.find_element(By.ID, login_button_id)
login_button.click()


assert driver.find_element(By.ID, inventory_page_id)
assert "Products" in driver.page_source





driver.quit()

