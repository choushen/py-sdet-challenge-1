from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


""" Test login with valid credentials """
def test_login() -> None:
    driver: webdriver = webdriver.Chrome()
    driver.get("https://sweetshop.netlify.app/sweets")
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "exampleInputEmail").send_keys("")
    driver.find_element(By.ID, "exampleInputPassword").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']").click()

    # Locate the welcome message element
    welcome_message: str = driver.find_element(By.CSS_SELECTOR, "p.lead").text

    # Validate the text in the welcome message
    expected_string: str = ""

    assert welcome_message == expected_string


    