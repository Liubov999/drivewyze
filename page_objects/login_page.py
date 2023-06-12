from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utitlities.web_ui.base_page import BasePage


class LoginPage(BasePage):

    __login_page_title = ("Drivewyze  - Login")
    __email_input = (By.XPATH, '//input[@id="username"]')
    __password_input = (By.XPATH, '//input[@id="password"]')
    __login_button = (By.XPATH, '// div[ @class ="sc-bdvvaa sc-gsDJrp jhtTCG jXLjZO"]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_login_title(self):
        login_title = self.__login_page_title
        return login_title

    def set_user_email(self, email):
        self.send_keys(self.__email_input, email)

    def set_user_password(self, password):
        self.send_keys(self.__password_input, password)

    def click_login_button(self):
        self.click(self.__login_button)
