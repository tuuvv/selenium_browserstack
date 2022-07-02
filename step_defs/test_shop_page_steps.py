import time

from pytest_bdd import scenarios, when, then, parsers
from pages.shop import ShopPage
from pages.base import BasePage
from sttable import parse_str_table

scenarios('../features/shop_page.feature')


@when(parsers.parse("I click on the '{subpage}' link"))
def click_sub_page_link(browser, subpage):
    print("step click_sub_page_link")
    ShopPage(browser).click_sub_page_link(subpage)


@then(parsers.parse("the '{subpage}' page opens"))
def verify_sub_page_opens(browser, subpage):
    print("step verify_sub_page_opens")
    assert ShopPage(browser).get_current_url() == BasePage.PAGE_URLS.get(subpage.lower())


@then(parsers.parse("I click on the Filter btn"))
def click_on_the_Filter_btn(browser):
    print("step click_filter_button")
    ShopPage(browser).click_filter_button()


@then(parsers.parse("Adjust the filter by price between 150 to 450 rps"))
def adjust_the_filter_by_price(browser):
    print("adjust_the_filter_by_price")
    ShopPage(browser).adjust_the_filter_by_price()

@then("I click on the Filter btn")
def click_filter_btn(browser):
    print("click on the Filter btn")
    ShopPage(browser).click_filter_btn()

@then("all books only between 150 to 450 rps price")
def verify_that_all_item_in_range_150_to_450(browser):
    print("test da loc duoc chua:", ShopPage(browser).verify_that_all_item_in_range_150_to_450())
    assert ShopPage(browser).verify_that_all_item_in_range_150_to_450() == bool(True)

@then(parsers.parse("I select '{option_text}' from the dropdown list"))
def select_dropdown_option_by_text(browser, option_text):
    ShopPage(browser).select_option_by_text(option_text)


@then(parsers.parse("the dropdown value is '{option_text}'"))
def verify_selected_option(browser, option_text):
    assert option_text == ShopPage(browser).get_current_dropdown_value()