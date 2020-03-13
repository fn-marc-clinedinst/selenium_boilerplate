from . import locators
from pages.base_page import BasePage


class ConfirmationModal(BasePage):
    @property
    def cancel_button(self):
        return self.find_visible_element(locators.CANCEL_BUTTON)

    @property
    def confirm_button(self):
        return self.find_visible_element(locators.CONFIRM_BUTTON)

    @property
    def ok_button(self):
        return self.find_visible_element(locators.OK_BUTTON)

    def click_cancel_button(self):
        self.cancel_button.click()

    def click_confirm_button(self):
        self.confirm_button.click()

    def click_ok_button(self):
        self.ok_button.click()

