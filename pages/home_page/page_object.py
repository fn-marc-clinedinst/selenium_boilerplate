from pages.base_page import BasePage


class HomePage(BasePage):
    @property
    def welcome_message(self):
        return 'Welcome, Marc'

    def get_welcome_message(self):
        return 'Welcome, Marc'
