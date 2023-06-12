from selene.core import locator

from test_data.data import UserInfo


def test_redirect_to_login_page(get_home_page, get_login_page):
    home_page = get_home_page
    home_page.click_on_sign_in_button()
    login_page = get_login_page
    login_title = get_login_page.get_login_title()
    assert login_title == login_page.get_login_title(), f'\nActual:{login_title}\nExpected:{login_page.get_login_title()} '


def test_user_login(get_home_page, get_login_page, get_dashboard_page):
    home_page = get_home_page
    home_page.click_on_sign_in_button()
    login_page = get_login_page
    login_page.set_user_email(UserInfo.DEFAULT_LOGIN)
    login_page.set_user_password(UserInfo.DEFAULT_PASSWORD)
    login_page.click_login_button()
    dashboard_page = get_dashboard_page
    dasboard_title = dashboard_page.get_dashboard_title()
    assert dasboard_title == dashboard_page.get_dashboard_title(), f'\nActual:{dasboard_title}\nExpected:{dashboard_page.get_dashboard_title()} '


