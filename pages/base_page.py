from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import (
    invisibility_of_element,
    presence_of_element_located,
    presence_of_all_elements_located,
    visibility_of_all_elements_located,
    visibility_of_element_located
)
from selenium.webdriver.support.wait import WebDriverWait

BASE_TIMEOUT = 15


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_present_element(self, locator, timeout=BASE_TIMEOUT):
        try:
            wait = WebDriverWait(self.driver, timeout)

            return wait.until(presence_of_element_located((locator['by'], locator['value'])))
        except TimeoutException:
            return None

    def find_present_elements(self, locator, timeout=BASE_TIMEOUT):
        try:
            wait = WebDriverWait(self.driver, timeout)

            return wait.until(presence_of_all_elements_located((locator['by'], locator['value'])))
        except TimeoutException:
            return []

    def find_visible_element(self, locator, timeout=BASE_TIMEOUT):
        try:
            wait = WebDriverWait(self.driver, timeout)

            return wait.until(visibility_of_element_located((locator['by'], locator['value'])))
        except TimeoutException:
            return None

    def find_visible_elements(self, locator, timeout=BASE_TIMEOUT):
        try:
            wait = WebDriverWait(self.driver, timeout)

            return wait.until(visibility_of_all_elements_located((locator['by'], locator['value'])))
        except TimeoutException:
            return []

    def is_not_visible(self, locator, timeout=BASE_TIMEOUT):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(invisibility_of_element((locator['by'], locator['value'])))

            return True
        except TimeoutException:
            return False

    def is_visible(self, locator, timeout=BASE_TIMEOUT):
        return self.find_visible_element(locator, timeout=timeout) is not None
