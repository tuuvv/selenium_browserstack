from pytest_bdd import scenarios, when, then, parsers
from pages.base import BasePage
from pages.home import HomePage
from pages.form_registration import FormRegitrationPage

scenarios('../features/form_registration_page.feature')


# Scenario1


@when(parsers.parse("I click on the '{page}' link"))
def click_sub_page_link(browser, page):
    FormRegitrationPage(browser).click_sub_page_link(page)


@then(parsers.parse("the '{page}' page opens"))
def verify_page_opens(browser, page):
    assert BasePage.PAGE_URLS.get(page.lower()) == FormRegitrationPage(browser).get_current_url()


@then(parsers.parse("a '{input_type}' input is displayed with label is '{label}'"))
def verify_input_displayed(browser, input_type, label):
    assert input_type in ["vuvantuu@gmail.com", "Vvtu_1z3"]
    print("$test:", FormRegitrationPage(browser).is_username_input_displayed())
    print("$test:", FormRegitrationPage(browser).get_username_input_label_text())
    print("$test:", FormRegitrationPage(browser).is_password_input_displayed())
    print("$test:", FormRegitrationPage(browser).get_password_input_label_text())

    if input_type == "vuvantuu@gmail.com":
        assert FormRegitrationPage(browser).is_username_input_displayed() == bool(True)
        assert FormRegitrationPage(browser).get_username_input_label_text() == label
    else:
        assert FormRegitrationPage(browser).is_password_input_displayed() == bool(True)
        assert FormRegitrationPage(browser).get_password_input_label_text() == label


@then("a Register button is displayed")
def verify_REG_BUTTON_displayed(browser):
    print("$btntxt:", FormRegitrationPage(browser).get_REG_BUTTON_text())
    assert FormRegitrationPage(browser).is_REG_BUTTON_displayed() == bool(True)
    assert FormRegitrationPage(browser).get_REG_BUTTON_text() == "Register"


# Scenario2
@then(parsers.parse("I enter a username of '{username}'"))
def enter_username(browser, username):
    FormRegitrationPage(browser).enter_username(username)


@then(parsers.parse("I enter a password of '{password}'"))
def enter_password(browser, password):
    FormRegitrationPage(browser).enter_password(password)


@then("I click the Register button")
def click_REG_BUTTON(browser):
    FormRegitrationPage(browser).click_REG_BUTTON()


@then("password field should display the characters in asterisks or bullets")
def verify_password_field(browser):
    print("typeofinput:", FormRegitrationPage(browser).check_password_field())
    assert FormRegitrationPage(browser).check_password_field() == "password"


@then(parsers.parse('the opening paragraph text is\n{paragraph}'))
def verify_opening_paragraph_text(browser, paragraph):
    assert paragraph.replace('\n', ' ') == FormRegitrationPage(
        browser).get_opening_paragraph_text()


@then(parsers.parse('a "{message}" message banner is displayed'))
def verify_message_text_and_colour(browser, config, message):
    assert True == FormRegitrationPage(browser).is_message_banner_displayed()
    assert message == FormRegitrationPage(browser).get_message_banner_text()


@then(parsers.parse('the admin page title is "{title}"'))
def verify_admin_page_title(browser, title):
    print("verify_admin_page_title:", FormRegitrationPage(browser).get_admin_page_title_text(), title)
    assert title == FormRegitrationPage(browser).get_admin_page_title_text()


@then(parsers.parse("I click on the '{signout}' link"))
def click_logout(browser, signout):
    FormRegitrationPage(browser).click_logout(signout)


@then(parsers.parse('the "{page}" page opens'))
def verify_page_opens(browser, page):
    assert FormRegitrationPage(browser).get_current_url() == BasePage.PAGE_URLS.get(page.lower())


@then(parsers.parse('the page has a footer containing "{text}"'))
def verify_footer_text(browser, text):
    assert BasePage(browser).get_admin_page_footer_text() == text


@then(parsers.parse('the link in the page footer goes to "{url}"'))
def verify_footer_link_url(browser, url):
    assert url == BasePage(browser).get_admin_page_footer_link_url()


@then("the title login text is correct")
def get_login_page_title_text(browser):
    assert FormRegitrationPage(browser).get_login_page_title_text() == "Register"
