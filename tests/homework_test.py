import pytest

from datetime import datetime
from random import choice
from selenium.webdriver.common.by import By
from time import sleep

from pages.actions_page.page_object import ActionsPage
from pages.action_modal.page_object import ActionModal
from pages.confirmation_modal.page_object import ConfirmationModal
from pages.home_page.page_object import HomePage
from pages.login_page.page_object import LoginPage
from utilities.wait import wait_for_element_to_be_visible


def delete_icon_by_action_summary(action_summary):
    return {
        'by': By.XPATH,
        'value': f'//p[text()="{action_summary}"]//ancestor::tr//i[@class="ion-trash-b"]'
    }


def new_action_summary(summary_text):
    return {
        'by': By.XPATH,
        'value': f'//td[contains(@class, "actions-row__summary-col")]//p[text()="{summary_text}"]'
    }


def get_random_number():
    return choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def get_date():
    date = datetime.now()

    return f'{date.month}/{date.day}/{date.year}'


def get_timestamp():
    date = datetime.now()

    return f'{date.hour}:{date.minute}:{date.second}'


def test_action_counts_for_empty_state(driver):
    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'Bigtwi2020!')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message

    actions_page = ActionsPage(driver)
    actions_page.navigate()

    assert actions_page.total_actions_count == 0
    assert actions_page.actions_this_week_count == 0
    assert actions_page.actions_this_month_count == 0

    assert "No actions yet." in actions_page.empty_state_help_text
    assert "Create one to record meetings, calls, and other actions to share past and future activity with your team." in actions_page.empty_state_help_text

    assert actions_page.empty_state_add_action_button.is_displayed()


@pytest.mark.homework_solution
def test_user_can_open_and_close_actions_modal_with_empty_state_add_action_button(driver):
    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'not_my_real_password')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message

    actions_page = ActionsPage(driver)
    actions_page.navigate()
    actions_page.click_empty_state_add_action_button()

    action_modal = ActionModal(driver)

    assert action_modal.modal_header_text == "Add Action"

    action_modal.enter_start_date('foobar')

    assert action_modal.date_is_valid(action_modal.start_date_value) == True


def test_user_can_create_a_new_action(driver):
    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'not_my_real_password')

    home_page = HomePage(driver)
    assert "Welcome" in home_page.welcome_message

    actions_page = ActionsPage(driver)
    actions_page.navigate()
    actions_page.click_add_action_button()

    action_modal = ActionModal(driver)
    action_modal.enter_start_date('8/14/2019')
    action_modal.enter_start_time('6:00am')
    action_modal.enter_end_date('8/14/2019')
    action_modal.enter_end_time('5:00pm')
    action_modal.set_action_type('Phone Call')
    action_modal.add_linked_item('US HR 1478', 'US - HR 1478')
    action_modal.add_labels(('agriculture', 'Farming', 'welfare'))
    action_modal.add_issue('Agriculture')

    action_summary_text = f'{get_date()} {get_timestamp()} - This is my summary text.'
    action_modal.add_summary(action_summary_text)

    action_modal.click_save_button()

    new_action = wait_for_element_to_be_visible(driver, new_action_summary(action_summary_text))
    assert new_action.is_displayed()

    delete_icon = wait_for_element_to_be_visible(driver, delete_icon_by_action_summary(action_summary_text))
    delete_icon.click()

    confirmation_modal = ConfirmationModal(driver)
    confirmation_modal.click_ok_button()

