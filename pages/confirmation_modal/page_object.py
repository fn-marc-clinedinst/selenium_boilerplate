from . import locators
from pages.base_page import BasePage


class ConfirmationModal(BasePage):
    def click_ok_button(self):
        self.find_visible_element(locators.OK_BUTTON).click()
