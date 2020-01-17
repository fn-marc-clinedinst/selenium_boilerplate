import pytest

from utilities.wait import wait_for_element_to_be_visible

from selenium.webdriver.common.by import By
from time import sleep

CLICK_HERE_TO_LOG_IN_BUTTON = '.btn-block'

EMAIL_INPUT = {
    'by': By.NAME,
    'value': 'email'
}


@pytest.mark.fiscalnote
def test_fiscalnote(driver):
    driver.get('https://staging.fiscalnote.com/?error=notauthorized')

    click_here_to_log_in_button = driver.find_element_by_css_selector(CLICK_HERE_TO_LOG_IN_BUTTON)
    click_here_to_log_in_button.click()

    username_input = wait_for_element_to_be_visible(driver, EMAIL_INPUT)
    username_input.send_keys('dummy text')

    sleep(5)

