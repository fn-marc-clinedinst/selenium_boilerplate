from selenium.webdriver.common.keys import Keys


from .locators import (
    ADD_ACTION_BUTTON,
    END_DATE,
    END_TIME,
    issue_by_issue_text,
    ISSUE_INPUT,
    LABEL_INPUT,
    label_by_label_text,
    LINKED_ITEM_INPUT,
    linked_item_by_linked_item_text,
    SAVE_BUTTON,
    SELECT_ACTION_TYPE,
    START_DATE,
    START_TIME,
    SUMMARY_SECTION
)
from utilities.wait import wait_for_element_to_be_visible


def add_issue(driver, desired_issue):
    issue_input = wait_for_element_to_be_visible(driver, ISSUE_INPUT)
    issue_input.send_keys(desired_issue)

    issue = wait_for_element_to_be_visible(driver, issue_by_issue_text('Agriculture'))
    issue.click()







def add_summary(driver, desired_summary):
    summary_section = wait_for_element_to_be_visible(driver, SUMMARY_SECTION)
    summary_section.clear()
    summary_section.send_keys(desired_summary)


def click_add_action_button(driver):
    add_action_button = wait_for_element_to_be_visible(driver, ADD_ACTION_BUTTON)
    add_action_button.click()


def click_save_button(driver):
    save_button = wait_for_element_to_be_visible(driver, SAVE_BUTTON)
    save_button.click()







def enter_start_date(driver, desired_start_date):
    start_date = wait_for_element_to_be_visible(driver, START_DATE)
    start_date.send_keys(Keys.ENTER)
    start_date.send_keys(desired_start_date)


def enter_start_time(driver, desired_start_time):
    start_time = wait_for_element_to_be_visible(driver, START_TIME)
    start_time.clear()
    start_time.send_keys(desired_start_time)
    start_time.send_keys(Keys.ENTER)


