from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    LINK = "https://scrapingclub.com/exercise/basic_login/"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert self.url == self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def login_user(self, name: str, password: str):
        name_field = self.browser.find_element(
            *LoginPageLocators.NAME_FIELD)
        password_field = self.browser.find_element(
            *LoginPageLocators.PASSWORD_FIELD)

        name_field.send_keys(name)
        password_field.send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    def should_be_success_message(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_SUCCESS_MESSAGE
        ), 'User was not login'
