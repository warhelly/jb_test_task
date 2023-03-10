from src.ui.utils.helpers import Actions
from selenium.webdriver.common.by import By


class RegistrationPageLocators:

    LOGIN_FIELD = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "._wt-button_1b4x9rv_1._wt-button_mode_primary_1b4x9rv_180")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, ".wt-text-2.wt-text-2_theme_dark > button")
    REGISTRATION_PAGE_TEXT = (By.CSS_SELECTOR, ".wt-h2")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".wt-offset-top-24 > button")
    REGISTRATION_ALERT = (By.CSS_SELECTOR, ".alert_content")


class RegistrationHelper(Actions):

    def input_login(self, text):
        search_field = self.find_element(RegistrationPageLocators.LOGIN_FIELD)
        search_field.click()
        search_field.send_keys(text)
        return search_field

    def input_password(self, text):
        password_field = self.find_element(RegistrationPageLocators.PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(text)
        return password_field

    def click_create_account_button(self):
        return self.find_element(RegistrationPageLocators.CREATE_ACCOUNT_BUTTON,time=2).click()

    def check_registration_page_text(self):
        text = self.find_element(RegistrationPageLocators.REGISTRATION_PAGE_TEXT, time=2).text
        return text

    def check_registration_alert_text(self, text):
        text = self.check_text(RegistrationPageLocators.REGISTRATION_ALERT, text, time=5).text
        return text
