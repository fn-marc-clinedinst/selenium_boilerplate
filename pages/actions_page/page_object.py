from . import locators
from pages.base_page import BasePage


class ActionsPage(BasePage):
    def click_add_action_button(self):
        add_action_button = self.find_visible_element(locators.ADD_ACTION_BUTTON)
        add_action_button.click()

    def navigate(self):
        self.driver.get('https://staging.fiscalnote.com/actions')
