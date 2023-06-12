from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utitlities.web_ui.base_page import BasePage


class MyDashboard(BasePage):
    __dashboard_page_title = ("Drivewyze (999 999) - Admin - Vehicles")

    def get_dashboard_title(self):
        dashboard_title = self.__dashboard_page_title
        return dashboard_title