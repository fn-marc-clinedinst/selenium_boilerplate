from selenium.webdriver.common.keys import Keys

from . import locators
from pages.base_page import BasePage


class ActionsPage(BasePage):
    def click_add_action_button(self):
        add_action_button = self.find_visible_element(locators.ADD_ACTION_BUTTON)
        add_action_button.click()

    def enter_start_date(self, desired_start_date):
        start_date = self.find_visible_element(locators.START_DATE)
        start_date.send_keys(Keys.ENTER)
        start_date.send_keys(desired_start_date)

    def enter_start_time(self, desired_start_time):
        start_time = self.find_visible_element(locators.START_TIME)
        start_time.clear()
        start_time.send_keys(desired_start_time)
        start_time.send_keys(Keys.ENTER)

    def navigate(self):
        self.driver.get('https://staging.fiscalnote.com/actions')
