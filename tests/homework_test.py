import pytest

from datetime import datetime
from random import choice
from selenium.webdriver.common.by import By

from pages.actions_page.helpers import (
    add_issue,
    add_summary,
    click_save_button,
)
from utilities.wait import wait_for_element_to_be_visible


CLICK_HERE_TO_LOG_IN_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.sign-in-form button'
}

CONFIRMATION_MODAL_OKAY_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.modal-footer .btn-success'
}

EMAIL_INPUT = {
    'by': By.NAME,
    'value': 'email'
}

LOGIN_BUTTON = {
    'by': By.CLASS_NAME,
    'value': 'auth0-lock-submit'
}

PASSWORD_INPUT = {
    'by': By.NAME,
    'value': 'password'
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


from pages.actions_page.page_object import ActionsPage


@pytest.mark.homework_solution
def test_user_can_create_a_new_action(driver):
    driver.get('https://staging.fiscalnote.com/?error=notauthorized')

    click_here_to_log_in_button = wait_for_element_to_be_visible(driver, CLICK_HERE_TO_LOG_IN_BUTTON)
    click_here_to_log_in_button.click()

    email_input = wait_for_element_to_be_visible(driver, EMAIL_INPUT)
    email_input.send_keys('marc.clinedinst+segmentation@fiscalnote.com')

    password_input = wait_for_element_to_be_visible(driver, PASSWORD_INPUT)
    password_input.send_keys('not_my_real_password')

    login_button = wait_for_element_to_be_visible(driver, LOGIN_BUTTON)
    login_button.click()

    welcome_message = wait_for_element_to_be_visible(driver, WELCOME_MESSAGE)
    assert 'Welcome' in welcome_message.text

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

    add_issue(driver, 'Agriculture')

    action_summary_text = f'{get_date()} {get_timestamp()} - This is my summary text.'
    add_summary(driver, action_summary_text)

    click_save_button(driver)

    new_action = wait_for_element_to_be_visible(driver, new_action_summary(action_summary_text))
    assert new_action.is_displayed()

    delete_icon = wait_for_element_to_be_visible(driver, delete_icon_by_action_summary(action_summary_text))
    delete_icon.click()

    confirmation_modal_ok_button = wait_for_element_to_be_visible(driver, CONFIRMATION_MODAL_OKAY_BUTTON)
    confirmation_modal_ok_button.click()
