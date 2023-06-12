from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.login_page import LoginPage
from utitlities.web_ui.base_page import BasePage


class HomePage(BasePage):

    __next_button = (By.XPATH, '//input[@value="Next"]')
    __select_i_want = (By.XPATH, '//select[@name="input_36"]')
    __email_input = (By.XPATH, '//input[@type="email"]')
    __current_title = ("Drivewyze: The Driver-Ce5ntric Safety and Compliance Ecosystem")
    __sign_in_button = (By.XPATH, '//a[@class="header__link"]')

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_sign_in_button(self):
        self.click(self.__sign_in_button)
        #return LoginPage(self.__driver)

    def click_on_next_button(self):
        self.click(self.__next_button)

















