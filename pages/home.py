from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base import BasePage
import time

SLOW = 10


class HomePage(BasePage):

    @property
    def PAGE_TITLE(self):
        return (By.TAG_NAME, 'h1')

    SUBHEADER = (By.TAG_NAME, 'h2')
    SUBPAGE_LINKS = (By.XPATH, '//*[@id="menu-item-40"]/a')
    HOMEPAGE_LINKS = (By.XPATH, '//*[@id="content"]/nav/a')
    HOME_BUTTON = (By.XPATH, '//*[@id="site-logo"]/a')
    SLIDER_IMG = (By.XPATH, '//*[@id="n2-ss-6"]/div/div/div/div/div/img')
    ARRIVAL = (By.XPATH, '//*[@id="themify_builder_content-22"]/div[2]/div/div/div/div/div[2]/div')
    ARRIVAL_IMG = (
        By.XPATH,
        '//body/div[@id="pagewrap"]/div[@id="body"]/div[@id="layout"]/div[@id="content"]/ul[1]/li[2]/a[1]/img[1]')
    PRODUCT_TAB = (By.XPATH, '//*[@id="product-163"]/div[3]/ul/li/a')
    PRODUCT_DETAIL = (By.ID, 'tab-description')
    REVIEW_TAB = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[3]/ul/li[2]/a')
    REVIEW_DETAIL = (By.ID, 'tab-reviews')
    PRODUCT_ADD_BTN = (By.XPATH, '//*[@id="content"]/ul/li[2]/a[2]')
    QUANTITY_INPUT = (By.XPATH, '//input[@title="Qty"]')
    PRODUCT_ADD_BTN_PAGE = (By.XPATH, '//button[normalize-space()="Add to basket"]')
    PRODUCT_ITEM = (By.XPATH, '//*[@id="wpmenucartli"]/a/span[1]')
    MESSAGE_BANNER = (By.XPATH, '/html/body/div[1]/div[2]/div/div/ul/li/..')
    MENU_ITEM = (By.XPATH, '/html/body/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a')
    CHECKOUT_BTN = (By.XPATH, '//*[@id="page-34"]/div/div[1]/div/div/div/a')

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

    def get_subheader_text(self):
        return self.browser.find_element(*self.SUBHEADER).text

    def get_subpage_list(self):
        links = self.browser.find_elements(*self.SUBPAGE_LINKS)
        titles = [link.text.split(" (")[0] for link in links]
        return titles

    def get_current_url(self):
        return self.browser.current_url

    def click_home_button(self):
        links = self.browser.find_elements(*self.HOME_BUTTON)
        for link in links:
            if link.get_attribute('title') == 'Automation Practice Site':
                link.click()
                break

    def count_number_of_slider(self):
        imgs = self.browser.find_elements(*self.SLIDER_IMG)
        return len(imgs)

    def count_number_of_arrivals(self):
        items = self.browser.find_elements(*self.ARRIVAL)
        return len(items)

    def click_on_the_image_of_arrivals(self):
        time.sleep(10)
        imgs = self.browser.find_elements(*self.ARRIVAL_IMG)
        for img in imgs:
            img.click()
            break

    def click_on_the_description_tab(self):
        links = self.browser.find_elements(*self.PRODUCT_TAB)
        for link in links:
            link.click()
            break

    def verify_the_description_title(self):
        titles = self.browser.find_elements(*self.PRODUCT_DETAIL)
        for title in titles:
            return title.get_attribute('style')

    def click_on_the_reviews_tab(self):
        links = self.browser.find_elements(*self.REVIEW_TAB)
        for link in links:
            link.click()
            time.sleep(SLOW)
            break

    def verify_the_reviews_title(self):
        titles = self.browser.find_elements(*self.REVIEW_DETAIL)
        for title in titles:
            return title.get_attribute('style')

    def click_product_add_btn(self):
        time.sleep(60)
        # items = self.browser.find_elements_by_xpath('//div[@id="content"]/ul/li[2]/a[2]')
        items = self.browser.find_elements(*self.PRODUCT_ADD_BTN)
        for item in items:
            item.click()
            time.sleep(20)
            break

    def click_product_add_btn_more(self):
        time.sleep(10)
        items = self.browser.findElement(By.xpath("//button[normalize-space()='Add to basket']"))
        for item in items:
            for i in range(7654):
                item.click()
            time.sleep(20)
            break

    def click_product_add_btn_in_product_page(self):
        self.browser.find_element(*self.QUANTITY_INPUT).clear()
        self.browser.find_element(*self.QUANTITY_INPUT).send_keys(7653)
        time.sleep(10)
        items = self.browser.find_elements(*self.PRODUCT_ADD_BTN_PAGE)
        for item in items:
            item.click()
            time.sleep(20)
        items = self.browser.find_elements(*self.PRODUCT_ADD_BTN_PAGE)
        for item in items:
            item.click()
            time.sleep(20)
            break

    def verify_product_item_added(self):
        lists = self.browser.find_elements(*self.PRODUCT_ITEM)
        for list in lists:
            print("list.text:", list.text)
        return list.text

    def is_message_banner_displayed(self):

        return self.browser.find_element(*self.MESSAGE_BANNER).is_displayed()

    def get_message_banner_text(self):
        time.sleep(10)
        return self.browser.find_element(*self.MESSAGE_BANNER).text.split('\n')[1]

    def click_menu_item(self):
        items = self.browser.find_elements(*self.MENU_ITEM)
        for item in items:
            item.click()
            time.sleep(20)

    def click_checkout_btn(self):
        items = self.browser.find_elements(*self.CHECKOUT_BTN)
        for item in items:
            item.click()
            time.sleep(20)
