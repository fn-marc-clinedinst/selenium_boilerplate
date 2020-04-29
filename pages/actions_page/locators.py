from selenium.webdriver.common.by import By

ADD_ACTION_BUTTON = {
    'by': By.XPATH,
    'value': '//button[text()="+ Add"]'
}

EMPTY_STATE_ADD_ACTION_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.actions-search__empty-content button'
}

EMPTY_STATE_HELP_TEXT = {
    'by': By.CSS_SELECTOR,
    'value': '.actions-search__empty-content h5'
}


def action_attendees_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'(//tr[contains(@class, "actions-row__info")])[{position}]//td[contains(@class, "actions-row__attendees-col")]//div[contains(@class, "trunk8-original")]'
    }


def action_count_by_description(description):
    return {
        'by': By.XPATH,
        'value': f'//figcaption[contains(string(), "{description}")]//preceding-sibling::figure'
    }


def action_creator_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'(//tr[contains(@class, "actions-row__info")])[{position}]//td[contains(@class, "actions-row__creator-col")]//div[contains(@class, "trunk8-original")]'
    }


def action_end_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'//tr[contains(@class, "actions-row__info")][{position}]//td[contains(@class, "actions-row__date-col")][2]'
    }


def action_issues_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'(//tr[contains(@class, "actions-row__info")])[{position}]//td[contains(@class, "actions-row__projects-col")]//div[contains(@class, "trunk8-original")]//span'
    }


def action_start_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'//tr[contains(@class, "actions-row__info")][{position}]//td[contains(@class, "actions-row__date-col")][1]'
    }


def action_summary_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'(//tr[contains(@class, "actions-row__info")])[{position}]//td[contains(@class, "actions-row__summary-col")]//div[contains(@class, "trunk8-original")]'
    }


def delete_action_icon_by_position(position):
    return {
        'by': By.XPATH,
        'value': f'(//i[contains(@class, "ion-trash-b")])[{position}]'
    }
