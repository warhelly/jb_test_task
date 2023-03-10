import credentials
from src.ui.pages.main_page import AuthHelper
from src.ui.pages.registration_page import RegistrationHelper


def test_check_elements(browser):
    login_page = AuthHelper(browser)
    login_page.go_to_site()
    login_page.check_login_page_text()
    login_page.check_login_placeholder()
    login_page.check_password_placeholder()
    login_page.check_header_text()
    login_page.check_create_account_text()
    login_page.check_description_text()
    login_page.check_landing_subtitle_text()


def test_login(browser):
    jb_login_page = AuthHelper(browser)
    jb_login_page.go_to_site()
    jb_login_page.input_login(credentials.LOGIN)
    jb_login_page.input_password(credentials.PASSWORD)
    jb_login_page.click_login_button()


def test_registration(browser):
    jb_login_page = AuthHelper(browser)
    jb_registration_page = RegistrationHelper(browser)
    jb_login_page.go_to_site()
    jb_login_page.click_registration_button()
    jb_registration_page.input_login("test@test.com")
    jb_registration_page.input_password("Test123!!!")
    jb_registration_page.click_create_account_button()
