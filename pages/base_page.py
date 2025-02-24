import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class BasePage:
    """Base class that contains logic for all pages"""

    def __init__(self, driver: WebDriver):
        """Constructor for BasePage class
        
        Args:
            driver (WebDriver): create and initialise the driver
        """
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def wait_for_element(self, locator: tuple[By, str], timeout: int = 10) -> WebElement:
        """Wait for an element to be visible.

        Args:
            locator (tuple[By, str])
            timeout (int): Wait time in seconds. Default is 10.

        Returns:
            WebElement: The visible web element.
        """
        try:
            self.logger.info(f"Waiting for element: {locator}")
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            self.logger.error(f"Timeout waiting for element {locator}: {e}")
            raise

    def send_keys(self, locator: tuple[By, str], text: str) -> None:
        """Send keys to an element.

        Args:
            locator (tuple[By, str])
            text (str): The text to send.
        """
        try:
            element = self.wait_for_element(locator)
            self.logger.info(f"Sending keys '{text}' to {locator}")
            element.clear()
            element.send_keys(text)
        except Exception as e:
            self.logger.error(f"Failed to send keys to {locator}: {e}")
            raise
    
    def click(self, locator: tuple[By, str]) -> None:
        """Click an element.

        Args:
            locator (tuple[By, str])
        """
        try:
            element = self.wait_for_element(locator)
            self.logger.info(f"Clicking element: {locator}")
            element.click()
        except Exception as e:
            self.logger.error(f"Failed to click element {locator}: {e}")
            raise

    def get_element_text(self, locator: tuple[By, str]) -> str:
        """Returns the inner text of an element.

        Args:
            locator (tuple[By, str])

        Returns:
            str: The text of the element.
        """
        try:
            element = self.wait_for_element(locator)
            text = element.text
            self.logger.info(f"Got text '{text}' from {locator}")
            return text
        except Exception as e:
            self.logger.error(f"Failed to get text from {locator}: {e}")
            raise
