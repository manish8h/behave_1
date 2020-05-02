from selenium.webdriver.common.keys import Keys

class LoginPage(object):
    def __init__(self, driver):
        self.search_input_el = driver.find_element_by_id('search_form_input_homepage')

    def enter_search_input(self, text):
        print("I am in login Page")
        self.search_input_el.send_keys(text + Keys.RETURN)
