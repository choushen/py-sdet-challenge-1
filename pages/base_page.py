from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:
    """Base class that contains logic for all pages"""


    def __init__(self, driver: WebDriver):
        """Constructor for BasePage class
        
        Args:
            driver (WebDriver): create and initialise the driver
        """
        self.driver = driver

    def wait_for_element(self, locator: tuple[By, str], timeout: int = 10) -> WebElement:
        """Wait for an element to be visible.

        Args:
            locator (tuple[By, str])
            timeout (int): Wait time in seconds. Default is 10.

        Returns:
            WebElement: The visible web element.
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def send_keys(self, locator: tuple[By, str], text: str) -> None:
        """Send keys to an element.

        Args:
            by (By): The locating strategy.
            value (str): The locator value.
            keys (str): The keys to send.
        """
        self.wait_for_element(locator).send_keys(text)
    
    def click(self, locator: tuple[By, str]) -> None:
        """Click an element.

        Args:
            by (By): The locating strategy.
            value (str): The locator value.
        """
        self.wait_for_element(locator).click()

    def get_element_text(self, locator: tuple[By, str]) -> str:
        """Returns the inner text of an element.

        Args:
            by (By): The locating strategy.
            value (str): The locator value.

        Returns:
            str: The text of the element.
        """
        return self.wait_for_element(locator).text