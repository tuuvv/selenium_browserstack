import time

from pytest_bdd import scenarios, when, then, parsers
from pages.home import HomePage
from pages.base import BasePage
from sttable import parse_str_table

scenarios('../features/home_page.feature')


@when(parsers.parse("I click on the '{subpage}' link"))
def click_sub_page_link(browser, subpage):
    print("step click_sub_page_link")
    HomePage(browser).click_sub_page_link(subpage)


@then(parsers.parse("the '{subpage}' page opens"))
def verify_sub_page_opens(browser, subpage):
    print("step verify_sub_page_opens")
    assert HomePage(browser).get_current_url() == BasePage.PAGE_URLS.get(subpage.lower())


@then(parsers.parse("the '{page}' page opens"))
def verify_sub_page_opens(browser, page):
    print("step verify_sub_page_opens")
    assert HomePage(browser).get_current_url() == BasePage.PAGE_URLS.get(page.lower())


@then(parsers.parse("I click Home button"))
def click_home_button(browser):
    print("step click_home_button")
    HomePage(browser).click_home_button()


@then("Total imgs of slider must be three")
def verify_total_imgs_of_slider(browser):
    print("step verify_total_imgs_of_slider")
    assert 3 == HomePage(browser).count_number_of_slider()


@then("Total arrivals must be three")
def verify_total_of_arrivals(browser):
    assert 3 == HomePage(browser).count_number_of_arrivals()


@then("I click on the images of arrival")
def click_on_the_image_of_arrivals(browser):
    print("step click_on_the_image_of_arrivals")
    HomePage(browser).click_on_the_image_of_arrivals()


@then("I click on the Description tab")
def click_on_the_description_tab(browser):
    print("step click_on_the_description_tab")
    HomePage(browser).click_on_the_description_tab()


@then("description regarding that book the user clicked on")
def verify_the_description_title(browser):
    print("description_title:", HomePage(browser).verify_the_description_title())
    assert HomePage(browser).verify_the_description_title() == 'display: block;'


@then("I click on the Reviews tab")
def click_on_the_review_tab(browser):
    HomePage(browser).click_on_the_reviews_tab()


@then("Reviews regarding that book the user clicked on")
def verify_the_review_title(browser):
    print("review_title:", HomePage(browser).verify_the_reviews_title())
    assert HomePage(browser).verify_the_reviews_title() == 'display: block;'


@then("the product page opens")
def verify_if_product_page_is_open(browser):
    print("step verify_if_product_page_is_open")
    assert "/product/" in HomePage(browser).get_current_url()


@then("I click on the product add btn")
def click_product_add_btn(browser):
    HomePage(browser).click_product_add_btn()


@then("fill in total product input value 7653 and click product add btn")
def click_product_add_btn_more(browser):
    HomePage(browser).click_product_add_btn_in_product_page()


@then(parsers.parse('a "{message}" message banner is displayed'))
def verify_message_text_error(browser, config, message):
    assert True == HomePage(browser).is_message_banner_displayed()
    assert message == HomePage(browser).get_message_banner_text()


@then("the product must added to basket")
def verify_if_item_added(browser):
    print("step the product must added to basket:", "1 Item" == HomePage(browser).verify_product_item_added())
    assert "1 Item" == HomePage(browser).verify_product_item_added()


@then("I click on the item menu")
def click_item_menu(browser):
    HomePage(browser).click_menu_item()


@then("basket page must be open")
def verify_if_basket_page_is_open(browser):
    print("step verify_if_basket_page_is_open")
    assert "/basket/" in HomePage(browser).get_current_url()


@then("I click on proceed to checkout btn")
def click_product_add_btn(browser):
    HomePage(browser).click_checkout_btn()


@then("checkout page must be open")
def verify_if_checkout_page_is_open(browser):
    print("step verify_if_checkout_page_is_open")
    assert "/checkout/" in HomePage(browser).get_current_url()
