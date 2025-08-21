from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome() # > Test login file
URL = "https://www.saucedemo.com" # Test login file

driver.find_element()

username_x_path = "//*[@id='user-name']"
username = "standard_user"

password_x_path = "//*[@id='password']"
password = "secret_sauce"

login_button_x_path = "//*[@id='login-button']"


driver.get(URL)
try:
    username_field = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,username_x_path)))
    password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, password_x_path)))
    login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, login_button_x_path)))
except TimeoutException:
    print("couldn't find one of the elements")
else:
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

finally:
    driver.quit()

