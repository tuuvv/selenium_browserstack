from selenium.webdriver.common.by import By
from pages.base import BasePage
import time

SLOW = 10


class FormAuthenticationPage(BasePage):

    @property
    def PAGE_TITLE(self):
        return (By.XPATH, '//*[@id="site-logo"]/a/')

    OPENING_PARAGRAPH = (By.XPATH, '//*[@id="page-36"]/div/div[1]/div/p[2]')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    INPUT_USER_LABEL = (By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[1]/label')
    INPUT_PASS_LABEL = (By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[2]/label')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="customer_login"]/div[1]/form/p[3]/input[3]')
    MESSAGE_BANNER = (By.XPATH, '//*[@id="page-36"]/div/div[1]/ul')
    ADMIN_PAGE_TITLE = (By.XPATH, '//*[@id="wpbody-content"]/div[3]/h1')
    SUBPAGE_LINKS = (By.XPATH, '/html/body/div/div/header/div/nav/ul/li/a')
    LOGOUT_LINKS = (By.XPATH, '/html/body/div/div/div/div/div/div/div/div/p/a')
    LOGIN_TITLE = (By.XPATH, '//*[@id="customer_login"]/div[1]/h2')

    def __init__(self, browser):
        self.browser = browser

    def click_sub_page_link(self, page_name):
        links = self.browser.find_elements(*self.SUBPAGE_LINKS)
        for link in links:
            if link.text.startswith(page_name):
                link.click()
                break

    def get_page_title_text(self):
        return self.browser.find_element(*self.PAGE_TITLE).text

    def get_admin_page_title_text(self):
        return self.browser.find_element(*self.ADMIN_PAGE_TITLE).text

    def get_opening_paragraph_text(self):
        return self.browser.find_element(*self.OPENING_PARAGRAPH).text

    def is_username_input_displayed(self):
        return self.browser.find_element(*self.USERNAME).is_displayed()

    def get_username_input_label_text(self):
        return self.browser.find_element(*self.INPUT_USER_LABEL).text

    def is_password_input_displayed(self):
        return self.browser.find_element(*self.PASSWORD).is_displayed()

    def get_password_input_label_text(self):
        return self.browser.find_element(*self.INPUT_PASS_LABEL).text

    def is_login_button_displayed(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).is_displayed()

    def get_login_button_text(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).get_attribute('value')

    def click_login_button(self):
        time.sleep(SLOW)
        return self.browser.find_element(*self.LOGIN_BUTTON).click()

    def is_message_banner_displayed(self):
        return self.browser.find_element(*self.MESSAGE_BANNER).is_displayed()

    def get_message_banner_colour(self):
        return self.browser.find_element(*self.MESSAGE_BANNER).value_of_css_property('background-color')

    def get_message_banner_text(self):
        # Full text includes 'x' to close the message so need to strip this off
        return self.browser.find_element(*self.MESSAGE_BANNER).text.split('\n')[0]

    def enter_username(self, username):
        self.browser.find_element(*self.USERNAME).send_keys(username)
        time.sleep(SLOW)

    def enter_password(self, password):
        self.browser.find_element(*self.PASSWORD).send_keys(password)
        time.sleep(SLOW)

    def check_password_field(self):
        return self.browser.find_element(*self.PASSWORD).get_attribute('type')
        time.sleep(SLOW)

    def click_logout(self, signout):
        links = self.browser.find_elements(*self.LOGOUT_LINKS)
        for link in links:
            if link.text.startswith(signout):
                link.click()
                time.sleep(SLOW)
                break

    def get_login_page_title_text(self):
        return self.browser.find_element(*self.LOGIN_TITLE).text

    def get_current_url(self):
        return self.browser.current_url
