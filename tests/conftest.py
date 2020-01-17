import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from tests import config


def pytest_addoption(parser):
    parser.addoption(
        '--baseurl',
        action='store',
        default='https://www.google.com',
        help='base URL for the application under test'
    )

    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='browser used for testing'
    )

    parser.addoption(
        "--environment",
        action="store",
        default="staging",
        help="environment under test"
    )


def get_driver(desired_browser):
    SELENIUM_GRID_IP_ADDRESS = '206.189.181.225'

    if desired_browser == 'chrome':
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
    elif desired_browser == 'firefox':
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
    elif desired_browser == 'chrome-remote':
        driver = webdriver.Remote(
            command_executor=f'http://{SELENIUM_GRID_IP_ADDRESS}:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
    elif desired_browser == 'firefox-remote':
        driver = webdriver.Remote(
            command_executor=f'http://{SELENIUM_GRID_IP_ADDRESS}:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
    else:
        raise Exception('Something really terrible has happened!')

    return driver


@pytest.fixture(scope='session')
def driver(request):
    config.baseurl = request.config.getoption('--baseurl')
    config.browser = request.config.getoption('--browser')
    config.environment = request.config.getoption('--environment')

    _driver = get_driver(config.browser)

    def _quit():
        _driver.quit()

    request.addfinalizer(_quit)

    return _driver
