from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from features.pages.registration_page import RegistrationPage
from time import sleep

# behave.runner.Context(runner)
# from hamcrest import *

URL = "http://www.newtours.demoaut.com/mercuryregister.php"


@given('I have valid data for registration')
def step_impl(context):
    context.data = {"f_name": "Python",
            "l_name": "3",
            "phone": "31125612",
            "email": "abc@gmail.com",
            "country": "INDIA"
            }


@given('I navigate to registration page')
def step_impl(context):
    context.browser.get(URL)
    print(context.data)


@then('I fill registration form')
def step_impl(context):
    driver = context.browser
    # driver.find_element_by_name("firstName").send_keys("ABC")
    # driver.find_element_by_name("lastName").send_keys("546789")
    # driver.find_element_by_name("phone").send_keys("567890222")
    # driver.find_element_by_id("userName").send_keys("abc@gmail.com")
    driver.find_element_by_name("firstName").send_keys(context.data.get("f_name"))
    driver.find_element_by_name("lastName").send_keys(context.data.get("l_name"))
    driver.find_element_by_name("phone").send_keys(context.data.get("phone"))
    driver.find_element_by_id("userName").send_keys(context.data.get("email"))
    Select(driver.find_element_by_name("country")).select_by_visible_text(context.data.get("country"))
    sleep(3)


@then('I click on submit')
def step_impl(context):
    context.browser.find_element_by_name("register").click()


@then('I fill registration form with pom')
def step_impl(context):
    reg_page = RegistrationPage(context.browser)
    reg_page.fill_first_name("Manish")
    reg_page.fill_last_name("Singh")

    reg_page.select_country("INDIA")
    sleep(2)


