from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from utils import get_test_validation_data, get_environment_data
from utils.driver_factory import DriverFactory


""" Test login with valid credentials """
def test_login() -> None:
    
    driver: WebDriver = DriverFactory.get_driver(headless=False)

    driver.get("https://sweetshop.netlify.app/sweets")

    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "exampleInputEmail").send_keys(get_environment_data()["username"])
    driver.find_element(By.ID, "exampleInputPassword").send_keys(get_environment_data()["password"])
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']").click()

    # Locate the welcome message element
    welcome_message: str = driver.find_element(By.CSS_SELECTOR, "p.lead").text

    # Validate the text in the welcome message
    expected_string: str = get_test_validation_data()["welcome_message"]

    assert welcome_message == expected_string



    