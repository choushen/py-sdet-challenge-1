import logging
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class DriverFactory:
    """A class to create WebDriver instances for different browsers."""

    @staticmethod
    def get_driver(browser: str = "chrome", headless: bool = True) -> WebDriver:
        """Returns a WebDriver based on the specified browser.

        Args:
            browser (str): The browser type ("chrome" or "firefox").
            headless (bool): Whether to run the browser in headless mode.

        Returns:
            WebDriver: The WebDriver instance.
        """
        logger.info(f"Initializing WebDriver for {browser} (headless={headless})")

        if browser.lower() == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")  # Use new headless mode for stability
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")  # Required for Docker
            options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues in Docker

            try:
                service = ChromeService(ChromeDriverManager().install())  # type: ignore
                driver = webdriver.Chrome(service=service, options=options) # type: ignore
                logger.info("WebDriver initialized successfully.")
            except Exception as e:
                logger.error(f"Failed to initialize WebDriver: {e}")
                raise

        else:
            error_msg = f"Unsupported browser: {browser}"
            logger.error(error_msg)
            raise ValueError(error_msg)

        return driver
