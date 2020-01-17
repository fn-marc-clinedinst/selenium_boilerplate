import pytest

FLASH_MESSAGE_ID = 'flash'
LOG_OUT_BUTTON_CLASS_NAME = 'radius'
LOG_IN_BUTTON_CLASS_NAME = 'radius'
PASSWORD_FIELD_ID = 'password'
USERNAME_FIELD_ID = 'username'


@pytest.mark.new_login
def test_user_can_log_in(driver):
    driver.get('https://the-internet.herokuapp.com/login')

    username_field = driver.find_element_by_id(USERNAME_FIELD_ID)
    username_field.send_keys('tomsmith')

    password_field = driver.find_element_by_id(PASSWORD_FIELD_ID)
    password_field.send_keys('SuperSecretPassword!')

    log_in_button = driver.find_element_by_class_name(LOG_IN_BUTTON_CLASS_NAME)
    log_in_button.click()

    flash_message = driver.find_element_by_id(FLASH_MESSAGE_ID)
    assert 'You logged into a secure area!' in flash_message.text

    log_out_button = driver.find_element_by_class_name(LOG_OUT_BUTTON_CLASS_NAME)
    log_out_button.click()

    flash_message = driver.find_element_by_id(FLASH_MESSAGE_ID)
    assert 'You logged out of the secure area!' in flash_message.text


@pytest.mark.new_login
def test_fiscalnote(driver):
    driver.get('https://staging.fiscalnote.com/?error=notauthorized')
