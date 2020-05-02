from behave import *
from selenium.webdriver.common.keys import Keys
# behave.runner.Context(runner)
from hamcrest import *

from features.pages.login_page import LoginPage

# "Constants"

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


# Givens

@given('the DuckDuckGo home page is displayed')
def step_impl(context):
    context.browser.get(DUCKDUCKGO_HOME)

# Whens


@when('the user searches for "{phrase}"')
def step_impl(context, phrase):
    login_page = LoginPage(context.browser)
    login_page.enter_search_input(phrase)
    # search_input = context.browser.find_element_by_id('search_form_input_homepage')
    # search_input.send_keys(phrase + Keys.RETURN)


@when('the user searches for the phrase')
def step_impl(context):
    search_input = context.browser.find_element_by_id('search_form_input_homepage')
    search_input.send_keys(context.text + Keys.RETURN)


# Thens

@then('one of the results contains "{phrase}"')
def step_impl(context, phrase):
    xpath = "//div[@id='links']//*[contains(text(), '%s')]" % phrase
    results = context.browser.find_elements_by_xpath(xpath)
    assert len(results) > 0
    # eq_(context.response['ok'], 1)
    context.execute_steps('''
    #     when I press the big red button
    #      and I duck
    # ''')


@then('results are shown for "{phrase}"')
def step_impl(context, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = context.browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # # Check search phrase
    search_input = context.browser.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == phrase
    # assert_that(2, equal_to(1))
    assert_that(2, equal_to(2))
    # assert_that("manish", contains_string("mn"))
