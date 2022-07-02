import pytest
import json
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pytest_bdd import given, then, parsers

from commons.path_utils import PathUtils
from pages.base import BasePage
from selenium.webdriver.chrome.options import Options

path_utils = PathUtils()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store")


@pytest.fixture
def config(request, scope='session'):
    BROWSERS = ['Chrome', 'Firefox']

    # Read config file
    config_path = path_utils.get_config_path()
    with open(config_path) as config_file:
        config = json.load(config_file)

    browser = request.config.option.browser
    if browser is not None:
        config['browser'] = browser

    # Assert values are acceptable
    assert config['browser'] in BROWSERS
    assert isinstance(config['headless'], bool)
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Chrome':
        opts = webdriver.ChromeOptions()
        opts.add_argument("--start-maximized")
        #if config['headless']:
            #opts.add_argument('headless')
        caps = {
            "os" : "Windows",
            "os_version" : "11",
            "browser" : "Chrome",
            "browser_version" : "latest-beta",
            "project" : "selenium demo",
            "build" : "jenkins ",
            "name" : "test jenkins browserstack",
            "browserstack.local" : "false",
            "browserstack.selenium_version" : "4.0.0",
            "resolution": "2560x1920",
            # 'browserstack.user': 'rainthe_0K23fG',
            # 'browserstack.key': 'MzukUonFP1FYpDqBq5Nz'
        }
        # for browser test
        b = webdriver.Remote(
            command_executor='https://rainthe_0K23fG:MzukUonFP1FYpDqBq5Nz@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=caps)
        b.maximize_window()
        # b = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
        # b = webdriver.Chrome(driver, options=opts)


    elif config['browser'] == 'Firefox':
        opts = webdriver.FirefoxOptions()
        if config['headless']:
            opts.headless = True
        b = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make call wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield b

    # Quit the WebDriver instance for the teardown
    b.quit()


@pytest.fixture
def datatable():
    return DataTable()


class DataTable(object):

    def __init__(self):
        pass

    def __str__(self):
        dt_str = ''
        for field, value in self.__dict__.items():
            dt_str = f'{dt_str}\n{field} = {value}'
        return dt_str

    def __repr__(self) -> str:
        return self.__str__()


@given(parsers.parse('I have navigated to the \'practice-auto\' "{page_name}" page'), target_fixture='navigate_to')
def navigate_to(browser, page_name):
    url = BasePage.PAGE_URLS.get(page_name.lower())
    browser.get(url)


@then(parsers.parse('a "{text}" banner is displayed in the top-right corner of the page'))
def verify_banner_text(browser, text):
    url = 'https://github.com/tourdedave/the-internet'
    assert text == BasePage(browser).get_github_fork_banner_text()
    assert url == BasePage(browser).get_github_fork_banner_link()
    styleAttrs = BasePage(browser).get_github_fork_banner_position().split(";")
    for attr in styleAttrs:
        if attr.startswith("position"):
            assert "absolute" == attr.split(": ")[1]
        if attr.startswith("top"):
            assert "0px" == attr.split(": ")[1]
        if attr.startswith("right"):
            assert "0px" == attr.split(": ")[1]
        if attr.startswith("border"):
            assert "0px" == attr.split(": ")[1]


@then(parsers.parse('the page has a footer containing "{text}"'))
def verify_footer_text(browser, text):
    assert text == BasePage(browser).get_page_footer_text()


@then(parsers.parse('the link in the page footer goes to "{url}"'))
def verify_footer_link_url(browser, url):
    assert url == BasePage(browser).get_page_footer_link_url()
