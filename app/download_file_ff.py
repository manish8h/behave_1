# https://the-internet.herokuapp.com/download
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import time

download_path = os.getcwd()
ff_driver_path = "/Users/manish/PycharmProjects/behave_1/drivers/geckodriver"
url = "https://the-internet.herokuapp.com/download"

options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", download_path)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream,application/vnd.ms-excel")

driver = webdriver.Firefox(executable_path=ff_driver_path, options=options)

driver.get(url)
# click on link to download file
driver.find_element_by_link_text("some-file.txt").click()

time.sleep(3)
driver.quit()
