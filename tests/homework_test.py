import pytest

from datetime import datetime
from random import choice
from selenium.webdriver.common.by import By

from pages.actions_page.page_object import ActionsPage
from pages.login_page.page_object import LoginPage
from utilities.wait import wait_for_element_to_be_visible


CONFIRMATION_MODAL_OKAY_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.modal-footer .btn-success'
}

WELCOME_MESSAGE = {
    'by': By.CSS_SELECTOR,
    'value': 'h1'
}


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


@pytest.mark.homework_solution
def test_user_can_create_a_new_action(driver):
    login_page = LoginPage(driver)
    login_page.login('selenium.course@fiscalnote.com', 'not_my_real_password')

    actions_page = ActionsPage(driver)

    actions_page.navigate()
    actions_page.click_add_action_button()
    actions_page.enter_start_date('8/14/2019')
    actions_page.enter_start_time('6:00am')
    actions_page.enter_end_date('8/14/2019')
    actions_page.enter_end_time('5:00pm')
    actions_page.set_action_type('Phone Call')
    actions_page.add_linked_item('US HR 1478', 'US - HR 1478')
    actions_page.add_labels(('agriculture', 'Farming', 'welfare'))
    actions_page.add_issue('Agriculture')

    action_summary_text = f'{get_date()} {get_timestamp()} - This is my summary text.'
    actions_page.add_summary(action_summary_text)

    actions_page.click_save_button()

    new_action = wait_for_element_to_be_visible(driver, new_action_summary(action_summary_text))
    assert new_action.is_displayed()

    delete_icon = wait_for_element_to_be_visible(driver, delete_icon_by_action_summary(action_summary_text))
    delete_icon.click()

    confirmation_modal_ok_button = wait_for_element_to_be_visible(driver, CONFIRMATION_MODAL_OKAY_BUTTON)
    confirmation_modal_ok_button.click()
