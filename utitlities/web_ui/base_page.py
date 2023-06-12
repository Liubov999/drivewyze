from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.__driver = driver
        self.__wait = WebDriverWait(self.__driver, 10)

    def wait_until_element_located(self, locator):
        return WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait_until_element_located(locator)
        element.click()

    def get_text(self, locator):
        return locator.text

    def send_keys(self, locator, value):
        element = self.wait_until_element_located(locator)
        element.send_keys(value)




