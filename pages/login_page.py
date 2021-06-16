#thirdparty
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("login")

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Cannot find login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Cannot find register form"
    
    def register_new_user(self, email, password):
        # have to implement manually
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_FIELD)
        password_field_first = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_FIRST)
        password_field_second = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD_SECOND)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        
        email_field.send_keys(email)
        password_field_first.send_keys(password)
        password_field_second.send_keys(password)
        register_button.click()
