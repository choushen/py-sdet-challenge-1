import pytest
from utils.driver_factory import DriverFactory
from pages.login_page import LoginPage
from utils import get_environment_data

@pytest.fixture(scope="function")
def driver():
    """Starts and cleans up the driver."""
    driver = DriverFactory.get_driver()
    driver.set_window_size(1920, 1080)  # Explicitly set size after launch
    driver.get(get_environment_data()["base_url"])
    yield driver
    driver.quit()

def test_login(driver):
    """Tests the login functionality with valid credentials."""

    login_page = LoginPage(driver)

    login_page.navigate_to_login()

    login_page.login(get_environment_data()["username"], get_environment_data()["password"])


    assert login_page.get_welcome_message() == login_page.STRING_VERIFICATION_MSG, (
        f"Login failed! Expected welcome message '{login_page.STRING_VERIFICATION_MSG}', "
        f"but got '{login_page.get_welcome_message()}'."
    )


def test_login_invalid_creds(driver):
    """Tests the login with invalid password."""
    login_page = LoginPage(driver)

    login_page.navigate_to_login()

    login_page.login(get_environment_data()["username"], "bob")

    assert login_page.get_welcome_message() != login_page.STRING_VERIFICATION_MSG, (
        f"Test failed! Expected welcome message '{login_page.STRING_VERIFICATION_MSG} should not be displayed"
    )