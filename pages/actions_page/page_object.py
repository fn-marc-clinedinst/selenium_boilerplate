from . import locators
from pages.base_page import BasePage


class ActionsPage(BasePage):
    @property
    def actions_this_month_count(self):
        return int(self.find_visible_element(locators.action_count_by_description('This Month')).text)

    @property
    def actions_this_week_count(self):
        return int(self.find_visible_element(locators.action_count_by_description('This Week')).text)

    @property
    def empty_state_add_action_button(self):
        return self.find_visible_element(locators.EMPTY_STATE_ADD_ACTION_BUTTON)

    @property
    def empty_state_help_text(self):
        return self.find_visible_element(locators.EMPTY_STATE_HELP_TEXT).text

    @property
    def total_actions_count(self):
        return int(self.find_visible_element(locators.action_count_by_description('Total')).text)

    def click_add_action_button(self):
        add_action_button = self.find_visible_element(locators.ADD_ACTION_BUTTON)
        add_action_button.click()

    def click_empty_state_add_action_button(self):
        self.empty_state_add_action_button.click()

    def navigate(self):
        self.driver.get('https://staging.fiscalnote.com/actions')
