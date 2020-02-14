from . import locators
from pages.base_page import BasePage


class ActionsPage(BasePage):
    @property
    def actions_this_month_count(self):
        return self.find_visible_element(locators.action_count_by_description('Actions This Month')).text

    @property
    def actions_this_week_count(self):
        return self.find_visible_element(locators.action_count_by_description('Actions This Month')).text

    @property
    def total_actions_count(self):
        return self.find_visible_element(locators.action_count_by_description('Total Actions')).text

    def click_add_action_button(self):
        add_action_button = self.find_visible_element(locators.ADD_ACTION_BUTTON)
        add_action_button.click()

    def navigate(self):
        self.driver.get('https://staging.fiscalnote.com/actions')
