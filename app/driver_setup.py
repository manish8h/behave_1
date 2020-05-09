# ref https://www.seleniumeasy.com/python/getting-started-selenium-webdriver-using-python
from selenium import webdriver
import time

ff_driver_path = "/Users/manish/PycharmProjects/behave_1/drivers/geckodriver"
ch_driver_path = "/Users/manish/PycharmProjects/behave_1/drivers/chromedriver"

# driver = webdriver.Chrome(ch_driver_path)
# for window: driver = webdriver.Chrome(r'C:\Python\chromedriver.exe')

driver = webdriver.Firefox(executable_path=ff_driver_path)

driver.get("https://www.google.com")


time.sleep(2)
driver.quit()

