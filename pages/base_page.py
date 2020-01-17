from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import (
    visibility_of_element_located
)
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_visible_element(self, locator, timeout=15):
        try:
            wait = WebDriverWait(self.driver, timeout)

            return wait.until(visibility_of_element_located((locator['by'], locator['value'])))
        except TimeoutException:
            return None
