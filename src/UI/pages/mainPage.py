from src.UI.utils.Helpers import Actions
from selenium.webdriver.common.by import By


class LandingPageLocators:

    LOCATOR_BY_ID = (By.ID, "ID")
    LOCATOR_BY_CLASS = (By.CLASS_NAME, "CLASS")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOGIN_FIELD = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "._wt-button_1b4x9rv_1._wt-button_mode_primary_1b4x9rv_180")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".wt-text-2.wt-text-2_theme_dark > button")
    LOGIN_TEXT = (By.CSS_SELECTOR, ".wt-h2")
    CREATE_ACCOUNT_TEXT = (By.CSS_SELECTOR, ".wt-text-2")
    HEADER_TEXT = (By.CSS_SELECTOR, ".new-wtu-page-header__title")
    DESCRIPTION_TEXT = (By.CSS_SELECTOR, ".wt-h1")
    LANDING_SUBTITLE = (By.CSS_SELECTOR, ".wt-h2.landing__subtitle")
    FORGOT_PASSWORD = (By.CSS_SELECTOR, ".wt-text-2.wt-text-2_hardness_hard.wt-offset-top-12 > button")


class AuthHelper(Actions):

    def input_login(self, text):
        search_field = self.find_element(LandingPageLocators.LOGIN_FIELD)
        search_field.click()
        search_field.send_keys(text)
        return search_field

    def input_password(self, text):
        password_field = self.find_element(LandingPageLocators.PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(text)
        return password_field

    def click_login_button(self):
        return self.find_element(LandingPageLocators.LOGIN_BUTTON,time=2).click

    def click_registration_button(self):
        return self.find_element(LandingPageLocators.REGISTRATION_BUTTON,time=2).click

    def login_button(self):
        return self.find_element(LandingPageLocators.LOGIN_BUTTON,time=2)

    def registration_button(self):
        return self.find_element(LandingPageLocators.REGISTRATION_BUTTON,time=2)

    def check_login_page_text(self):
        text = self.find_element(LandingPageLocators.LOGIN_TEXT, time=2).text
        assert "Log in" in text

    def check_login_placeholder(self):
        text = self.find_element(LandingPageLocators.LOGIN_FIELD, time=2).get_attribute('placeholder')
        assert "Email" in text

    def check_password_placeholder(self):
        text = self.find_element(LandingPageLocators.PASSWORD_FIELD, time=2).get_attribute('placeholder')
        assert "Password" in text

    def password_field(self):
        password_field = self.find_element(LandingPageLocators.PASSWORD_FIELD, time=2)
        return password_field

    def check_create_account_text(self):
        text = self.find_element(LandingPageLocators.CREATE_ACCOUNT_TEXT, time=2).text
        assert "Not signed up yet? " in text

    def check_header_text(self):
        text = self.find_element(LandingPageLocators.HEADER_TEXT, time=2).text
        assert "Datalore" in text

    def check_description_text(self):
        text = self.find_element(LandingPageLocators.DESCRIPTION_TEXT, time=2).text
        print(text)
        assert "is a collaborative\ndata science\nplatform" in text

    def check_landing_subtitle_text(self):
        text = self.find_element(LandingPageLocators.LANDING_SUBTITLE, time=2).text
        assert "Get support" in text

    def check_forgot_password_text(self):
        text = self.find_element(LandingPageLocators.FORGOT_PASSWORD, time=2).text
        assert "Forgot your password?" in text
