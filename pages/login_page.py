from .base_page import BasePage
from .locators import LoginPageLocators
from random_word import RandomWords

import secrets
import string
import random
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url, 'Substring "login" was not found in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not found on the page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Login form is not found on the page'
    

    def register_new_user(self, email, pswd):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(pswd)
        self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(pswd)

        registration_submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registration_submit_button.click()


    def generate_email_and_password(self):
        r = RandomWords()
        email = r.get_random_word() + '@hotmail.com'
        
        letters = string.ascii_letters
        digits = string.digits
        pwd_length = random.randrange(10, 25)
        alphabet = letters + digits

        password = ''
        for _ in range(pwd_length):
            password += ''.join(secrets.choice(alphabet))

        return email, password