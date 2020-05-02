from selenium.webdriver.support.select import Select


class RegistrationPage(object):
    def __init__(self, driver):
        self.first_name = driver.find_element_by_name("firstName")
        self.last_name = driver.find_element_by_name("lastName")
        self.phone = driver.find_element_by_name("phone")
        self.country = driver.find_element_by_name("country")
        self.submit = driver.find_element_by_name("register")

    def fill_first_name(self, first_name):
        self.first_name.send_keys(first_name)

    def fill_last_name(self, last_name):
        self.last_name.send_keys(last_name)

    def select_country(self, country_name):
        Select(self.country).select_by_visible_text(country_name)

    def click_on_submit(self):
        self.submit.click()
