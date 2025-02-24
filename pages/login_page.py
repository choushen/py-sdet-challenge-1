from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils import get_test_validation_data, get_environment_data


class LoginPage(BasePage):
    """Page Object for the login page."""
    # Locators
    LOCATOR_LOGIN_LINK: tuple = (By.LINK_TEXT, "Login")
    LOCATOR_LOGIN_USERNAME: tuple = (By.ID, "exampleInputEmail")
    LOCATOR_LOGIN_PASSWORD: tuple = (By.ID, "exampleInputPassword")
    LOCATOR_LOGIN_BUTTON: tuple = (By.CSS_SELECTOR, "button.btn.btn-primary[type='submit']")
    LOCATOR_WELCOME_BANNER: tuple = (By.CSS_SELECTOR, "p.lead")
    LOCATOR_INVALID_CREDENTIALS: tuple = (By.CSS_SELECTOR, "div.invalid-feedback.invalid-email")

    # Properties
    STRING_VERIFICATION_MSG: str = get_test_validation_data()["welcome_message"]

    def navigate_to_login(self) -> None:
        """Navigate to the login page."""
        self.click(self.LOCATOR_LOGIN_LINK)

    def get_welcome_message(self) -> str:
        """Get the welcome message."""
        return self.get_element_text(self.LOCATOR_WELCOME_BANNER)

    def enter_username(self, username: str) -> None:
        """Enter the username."""
        self.send_keys(self.LOCATOR_LOGIN_USERNAME, username)

    def enter_password(self, password: str) -> None:
        """Enter the password."""
        # self.send_keys(*self.PASSWORD_INPUT, password)
        self.send_keys(self.LOCATOR_LOGIN_PASSWORD, password)

    def click_login(self) -> None:
        """Click the login button."""
        self.click(self.LOCATOR_LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        """Perform the login action."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
