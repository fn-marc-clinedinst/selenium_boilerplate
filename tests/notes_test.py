import pytest

from selenium.webdriver.common.by import By
from time import sleep

from utilities.wait import wait_for_element_to_be_visible


CLICK_HERE_TO_LOG_IN_BUTTON = {
    'by': By.CLASS_NAME,
    'value': 'btn-primary'
}

EMAIL_INPUT = {
    'by': By.XPATH,
    'value': '//input[@name="email"]'
}

PASSWORD_INPUT = {
    'by': By.XPATH,
    'value': '//input[@name="password"]'
}

LOG_IN_BUTTON = {
    'by': By.CLASS_NAME,
    'value': 'auth0-lock-submit'
}

WELCOME_MESSAGE = {
    'by': By.CSS_SELECTOR,
    'value': 'h1'
}


@pytest.mark.notes
def test_notes(driver):
    driver.get('https://staging.fiscalnote.com/?error=notauthorized')

    click_here_to_log_in_button = wait_for_element_to_be_visible(driver, CLICK_HERE_TO_LOG_IN_BUTTON)
    click_here_to_log_in_button.click()

    email_input = wait_for_element_to_be_visible(driver, EMAIL_INPUT)
    email_input.send_keys('fiscalnote.aft.premium@gmail.com')

    password_input = wait_for_element_to_be_visible(driver, PASSWORD_INPUT)
    password_input.send_keys('not_my_real_password')

    login_button = wait_for_element_to_be_visible(driver, LOG_IN_BUTTON)
    login_button.click()

    welcome_message = wait_for_element_to_be_visible(driver, WELCOME_MESSAGE)
    assert 'Welcome, FiscalNote' in welcome_message.text

    driver.get('https://staging.fiscalnote.com/notes')

    sleep(5)
