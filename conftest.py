import pytest
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.My_Dashboard import MyDashboard
from page_objects.login_page import LoginPage
from utitlities.web_ui.driver_factory import DriverFactory

from page_objects.home_page import HomePage
from utitlities.web_ui.driver_factory import DriverFactory
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=1, is_headless=False)
    driver.get('https://drivewyze.com/')
    driver.maximize_window()
    WebDriverWait(driver, 3).until(EC.title_is('Drivewyze: The Driver-Centric Safety and Compliance Ecosystem'))
    yield driver
    driver.quit()


@pytest.fixture()
def get_home_page(create_driver):
    return HomePage(create_driver)


@pytest.fixture()
def get_login_page(create_driver):
    return LoginPage(create_driver)


@pytest.fixture()
def get_dashboard_page(create_driver):
    return MyDashboard(create_driver)