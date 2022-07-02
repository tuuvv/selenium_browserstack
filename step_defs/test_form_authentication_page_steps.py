from pytest_bdd import scenarios, when, then, parsers
from pages.base import BasePage
from pages.home import HomePage
from pages.form_authentication import FormAuthenticationPage

scenarios('../features/form_authentication_page.feature')


# Scenario1
# @then(parsers.parse("the page title is '{title}'"))
# def verify_page_title(browser, title):
#     print("verify_page_title:", FormAuthenticationPage(browser).get_page_title_text(), title)
#     assert title == FormAuthenticationPage(browser).get_page_title_text()

@when(parsers.parse("I click on the '{page}' link"))
def click_sub_page_link(browser, page):
    FormAuthenticationPage(browser).click_sub_page_link(page)


@then(parsers.parse("the '{page}' page opens"))
def verify_page_opens(browser, page):
    assert BasePage.PAGE_URLS.get(page.lower()) == FormAuthenticationPage(browser).get_current_url()


@then(parsers.parse("a '{input_type}' input is displayed with label is '{label}'"))
def verify_input_displayed(browser, input_type, label):
    assert input_type in ["tuuvv.uit", "Vvtu_1z3"]
    print("$test:", FormAuthenticationPage(browser).is_username_input_displayed())
    print("$test:", FormAuthenticationPage(browser).get_username_input_label_text())
    print("$test:", FormAuthenticationPage(browser).is_password_input_displayed())
    print("$test:", FormAuthenticationPage(browser).get_password_input_label_text())

    if input_type == "tuuvv.uit":
        assert FormAuthenticationPage(browser).is_username_input_displayed() == bool(True)
        assert FormAuthenticationPage(browser).get_username_input_label_text() == label
    else:
        assert FormAuthenticationPage(browser).is_password_input_displayed() == bool(True)
        assert FormAuthenticationPage(browser).get_password_input_label_text() == label


@then("a Login button is displayed")
def verify_login_button_displayed(browser):
    print("$btntxt:", FormAuthenticationPage(browser).get_login_button_text())
    assert FormAuthenticationPage(browser).is_login_button_displayed() == bool(True)
    assert FormAuthenticationPage(browser).get_login_button_text() == "Login"


# Scenario2
@then(parsers.parse("I enter a username of '{username}'"))
def enter_username(browser, username):
    FormAuthenticationPage(browser).enter_username(username)


@then(parsers.parse("I enter a password of '{password}'"))
def enter_password(browser, password):
    FormAuthenticationPage(browser).enter_password(password)


@then("I click the Login button")
def click_login_button(browser):
    FormAuthenticationPage(browser).click_login_button()


@then("password field should display the characters in asterisks or bullets")
def verify_password_field(browser):
    print("typeofinput:", FormAuthenticationPage(browser).check_password_field())
    assert FormAuthenticationPage(browser).check_password_field() == "password"


@then(parsers.parse('the opening paragraph text is\n{paragraph}'))
def verify_opening_paragraph_text(browser, paragraph):
    assert paragraph.replace('\n', ' ') == FormAuthenticationPage(
        browser).get_opening_paragraph_text()


@then(parsers.parse('a "{message}" message banner is displayed'))
def verify_message_text_and_colour(browser, config, message):
    assert True == FormAuthenticationPage(browser).is_message_banner_displayed()
    assert message == FormAuthenticationPage(browser).get_message_banner_text()


@then(parsers.parse('the admin page title is "{title}"'))
def verify_admin_page_title(browser, title):
    print("verify_admin_page_title:", FormAuthenticationPage(browser).get_admin_page_title_text(), title)
    assert title == FormAuthenticationPage(browser).get_admin_page_title_text()


@then(parsers.parse("I click on the '{signout}' link"))
def click_logout(browser, signout):
    FormAuthenticationPage(browser).click_logout(signout)


@then(parsers.parse('the "{page}" page opens'))
def verify_page_opens(browser, page):
    assert FormAuthenticationPage(browser).get_current_url() == BasePage.PAGE_URLS.get(page.lower())


@then(parsers.parse('the page has a footer containing "{text}"'))
def verify_footer_text(browser, text):
    assert BasePage(browser).get_admin_page_footer_text() == text


@then(parsers.parse('the link in the page footer goes to "{url}"'))
def verify_footer_link_url(browser, url):
    assert url == BasePage(browser).get_admin_page_footer_link_url()


@then("the title login text is correct")
def get_login_page_title_text(browser):
    assert FormAuthenticationPage(browser).get_login_page_title_text() == "Login"
