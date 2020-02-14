from selenium.webdriver.common.by import By

ADD_ACTION_BUTTON = {
    'by': By.XPATH,
    'value': '//button[text()="+ Add"]'
}


def action_count_by_description(description):
    return {
        'by': By.XPATH,
        'value': f'//figcaption[contains(string(), "{description}")]//preceding-sibling::figure'
    }
