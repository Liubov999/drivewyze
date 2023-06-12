from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options


class DriverFactory:
    CHROME = 1
    FIREFOX = 2

    @staticmethod
    def create_driver(driver_id, is_headless):
        if DriverFactory.CHROME == driver_id:
            chrome_options = Options()
            if is_headless:
                chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        elif DriverFactory.FIREFOX == driver_id:
            driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        else:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        return driver
