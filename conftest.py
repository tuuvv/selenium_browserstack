import pytest
import json
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pytest_bdd import given, then, parsers

from commons.path_utils import PathUtils
from pages.base import BasePage

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
        desired_cap = {
            "os": "Windows",
            "os_version": "11",
            "browser": "Chrome",
            "browser_version": "latest-beta",
            "browserstack.local": "false",
            "browserstack.selenium_version": "3.14.0"
        }
        # b = webdriver.Chrome(desired_cap, options=opts)
        b = webdriver.Chrome(ChromeDriverManager().install(), options=opts)


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
    
# import pytest
# import os
# import browser_platform_conf

# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# @pytest.fixture
# def browser():
#     "pytest fixture for browser"
#     return pytest.config.getoption("-B")


# @pytest.fixture
# def browserstack_flag():
#     "pytest fixture for browserstack flag"
#     return pytest.config.getoption("-M")


# @pytest.fixture
# def browser_version():
#     "pytest fixture for browser version"
#     return pytest.config.getoption("-V")


# @pytest.fixture
# def platform():
#     "pytest fixture for platform"
#     return pytest.config.getoption("-P")


# @pytest.fixture
# def os_version():
#     "pytest fixture for os version"
#     return pytest.config.getoption("-O")


# def pytest_generate_tests(metafunc):
#     "test generator function to run tests across different parameters"
#     if 'browser' in metafunc.fixturenames:
#         if metafunc.config.getoption("-M").lower() == 'y':
#             if metafunc.config.getoption("-B") == ["all"]:
#                 metafunc.parametrize("browser,browser_version,platform,os_version",
#                                      browser_platform_conf.py.cross_browser_cross_platform_config)


# def pytest_addoption(parser):
#     parser.addoption("-B", "--browser",
#                      dest="browser",
#                      action="append",
#                      default=[],
#                      help="Browser. Valid options are firefox, ie and chrome")
#     parser.addoption("-M", "--browserstack_flag",
#                      dest="browserstack_flag",
#                      default="N",
#                      help="Run the test in Browserstack: Y or N")
#     parser.addoption("-O", "--os_version",
#                      dest="os_version",
#                      action="append",
#                      help="The operating system: xp, 7",
#                      default=[])
#     parser.addoption("-V", "--ver",
#                      dest="browser_version",
#                      action="append",
#                      help="The version of the browser: a whole number",
#                      default=[])
#     parser.addoption("-P", "--platform",
#                      dest="platform",
#                      action="append",
#                      help="The operating system: Windows 7, Linux",
#                      default=[])


# def get_webdriver(browser, browser_version, platform, os_version):
#     "Run the test in browser stack browser stack flag is 'Y'"
#     USERNAME = 'rainthe_0K23fG' # We fetch values from a conf file in our framework we use on our clients
#     PASSWORD = 'MzukUonFP1FYpDqBq5Nz'
#     if browser.lower() == 'firefox':
#         desired_capabilities = DesiredCapabilities.FIREFOX
#     if browser.lower() == 'chrome':
#         desired_capabilities = DesiredCapabilities.CHROME
#     desired_capabilities['os'] = platform
#     desired_capabilities['os_version'] = os_version
#     desired_capabilities['browser_version'] = browser_version

#     return webdriver.Remote(command_executor='http://%s:%s@hub.browserstack.com:80/wd/hub' % (USERNAME, PASSWORD),
#                             desired_capabilities=desired_capabilities)