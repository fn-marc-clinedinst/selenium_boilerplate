from selenium.webdriver.common.by import By

END_DATE = {
    'by': By.ID,
    'value': 'create-action-modal-end-date'
}

END_TIME = {
    'by': By.ID,
    'value': 'create-action-modal-end-time'
}

ISSUE_INPUT = {
    'by': By.CSS_SELECTOR,
    'value': '.project-selection__wrapper input'
}

LABEL_INPUT = {
    'by': By.CSS_SELECTOR,
    'value': '.label-selection__wrapper input'
}

LINKED_ITEM_INPUT = {
    'by': By.ID,
    'value': 'linked-items-selectize-selectized'
}

MODAL_HEADER = {
    'by': By.CLASS_NAME,
    'value': 'modal-title'
}

SAVE_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.actions-modal__footer button[type="submit"]'
}

SELECT_ACTION_TYPE = {
    'by': By.CSS_SELECTOR,
    'value': 'select.action-type'
}

START_DATE = {
    'by': By.ID,
    'value': 'create-action-modal-start-date'
}

START_TIME = {
    'by': By.ID,
    'value': 'create-action-modal-start-time'
}

SUMMARY_SECTION = {
    'by': By.CSS_SELECTOR,
    'value': '.summary'
}


def issue_by_issue_text(issue_text):
    return {
        'by': By.XPATH,
        'value': f'//div[contains(@class, "project-selection__wrapper")]//li//a[contains(string(), "{issue_text}")]'
    }


def label_by_label_text(label_text):
    return {
        'by': By.XPATH,
        'value': f'//div[@class="label-selection__wrapper"]//li//a[contains(string(), "{label_text}")]'
    }


def linked_item_by_linked_item_text(linked_item_text):
    return {
        'by': By.XPATH,
        'value': f'//div[contains(@class, "option") and contains(string(), "{linked_item_text}")]'
    }
