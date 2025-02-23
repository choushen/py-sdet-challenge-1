from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import platform

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
        driver: WebDriver  # Type hint for clarity

        if browser.lower() == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")  # Use new headless mode for stability
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")  # Required for Docker
            options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues in Docker

            # Handle ChromeDriver path based on the OS
            if platform.system() == "Windows":
                service = ChromeService()  # type: ignore
            else:
                service = ChromeService("/usr/local/bin/chromedriver")  # Set the path for Docker

            driver = webdriver.Chrome(service=service, options=options) # type: ignore

        else:
            raise ValueError(f"Unsupported browser: {browser}")

        return driver