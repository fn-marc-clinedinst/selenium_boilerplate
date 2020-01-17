from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from . import locators
from pages.base_page import BasePage


class ActionsPage(BasePage):
    def add_label(self, desired_label):
        label_input = self.find_visible_element(locators.LABEL_INPUT)
        label_input.send_keys(desired_label)

        label = self.find_visible_element(locators.label_by_label_text(desired_label))
        label.click()

    def add_labels(self, labels):
        for label in labels:
            self.add_label(label)

    def add_linked_item(self, query_text, desired_linked_item):
        linked_item_input = self.find_visible_element(locators.LINKED_ITEM_INPUT)
        linked_item_input.send_keys(query_text)

        linked_item = self.find_visible_element(locators.linked_item_by_linked_item_text(desired_linked_item))
        linked_item.click()

    def click_add_action_button(self):
        add_action_button = self.find_visible_element(locators.ADD_ACTION_BUTTON)
        add_action_button.click()

    def enter_end_date(self, desired_end_date):
        end_date = self.find_visible_element(locators.END_DATE)
        end_date.send_keys(Keys.ENTER)
        end_date.send_keys(desired_end_date)

    def enter_end_time(self, desired_end_time):
        end_time = self.find_visible_element(locators.END_TIME)
        end_time.clear()
        end_time.send_keys(desired_end_time)
        end_time.send_keys(Keys.ENTER)

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

    def set_action_type(self, desired_action_type):
        select_action_type = Select(self.find_visible_element(locators.SELECT_ACTION_TYPE))
        select_action_type.select_by_visible_text(desired_action_type)
