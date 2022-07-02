from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from pages.base import BasePage
import time

SLOW = 10


class ShopPage(BasePage):

    @property
    def PAGE_TITLE(self):
        return (By.TAG_NAME, 'h1')

    SUBHEADER = (By.TAG_NAME, 'h2')
    SUBPAGE_LINKS = (By.XPATH, '//*[@id="menu-item-40"]/a')
    SLIDER_RANGE = (By.XPATH, '//div[@id="woocommerce_price_filter-2"]//div//div[1]//div[1]')
    SLIDER = (By.XPATH, '//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[2]')
    FILTER_BTN = (By.XPATH, '//*[@id="woocommerce_price_filter-2"]/form/div/div[2]/button')
    PRICE_SHOP_ITEM = (By.XPATH, '//div[@id="content"]/ul[1]/li/a/span/span/..')
    DROPDOWN_LIST = (By.TAG_NAME, 'select')

    def click_sub_page_link(self, page_name):
        links = self.browser.find_elements(*self.SUBPAGE_LINKS)
        for link in links:
            if link.text.startswith(page_name):
                link.click()
                break

    def get_current_url(self):
        return self.browser.current_url

    def adjust_the_filter_by_price(self):
        mainSlider = self.browser.find_elements(*self.SLIDER_RANGE)
        for sl in mainSlider:
            location = sl.location
            size = sl.size
            w, h = size['width'], size['height']
            w = w * (14.4) / 100
            print(location)
            print(size)
            print(w, h)
        slider = self.browser.find_element_by_xpath('//*[@id="woocommerce_price_filter-2"]/form/div/div[1]/span[2]')
        ActionChains(self.browser).drag_and_drop_by_offset(slider, -w, 0).perform()
        # ActionChains(self.browser).click_and_hold(slider).move_by_offset(-w, 0).release().perform() //cach 2
        time.sleep(10)

    def click_filter_btn(self):
        links = self.browser.find_elements(*self.FILTER_BTN)
        for link in links:
            link.click()
            time.sleep(10)
            break

    def verify_that_all_item_in_range_150_to_450(self):
        items = self.browser.find_elements(*self.PRICE_SHOP_ITEM)
        check = bool(True)
        for item in items:
            print(item.text.split('₹')[1])
            if float(item.text.split('₹')[1]) > 450:
                self.check = bool(False)
        return check

    def select_option_by_text(self, text):
        dropdown = Select(self.browser.find_element(*self.DROPDOWN_LIST))
        dropdown.select_by_visible_text(text)

    def get_current_dropdown_value(self):
        dropdown = Select(self.browser.find_element(*self.DROPDOWN_LIST))
        return dropdown.first_selected_option.text
