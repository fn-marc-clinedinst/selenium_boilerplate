from . import locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def click_click_here_to_log_in_button(self):
        click_here_to_log_in_button = self.find_visible_element(locators.CLICK_HERE_TO_LOG_IN_BUTTON)
        click_here_to_log_in_button.click()

    def click_login_button(self):
        login_button = self.find_visible_element(locators.LOGIN_BUTTON)
        login_button.click()

    def enter_email(self, email):
        email_input = self.find_visible_element(locators.EMAIL_INPUT)
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.find_visible_element(locators.PASSWORD_INPUT)
        password_input.send_keys(password)

    def navigate(self):
        self.driver.get('https://staging.fiscalnote.com/?error=notauthorized')

    def login(self, email, password):
        self.navigate()
        self.click_click_here_to_log_in_button()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
