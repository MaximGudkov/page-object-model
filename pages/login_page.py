from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' should be in url on LoginPage"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASS_REGISTER_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASS_REGISTER_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTER_BUTTON).click()
