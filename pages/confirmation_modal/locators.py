from selenium.webdriver.common.by import By

CANCEL_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.modal-dialog--inner .modal-footer .btn-default'
}

CONFIRM_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.modal-dialog--inner .modal-footer .btn-success'
}

OK_BUTTON = {
    'by': By.CSS_SELECTOR,
    'value': '.modal-footer .btn-success'
}
