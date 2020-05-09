# https://the-internet.herokuapp.com/download
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

download_path = os.getcwd()
url = "https://the-internet.herokuapp.com/download"

options = Options()
options.add_experimental_option("prefs", {
  "download.default_directory": fr"{download_path}",
  "download.prompt_for_download": False
})

driver = webdriver.Chrome(options = options)
driver.get(url)

# click on link to download file
driver.find_element_by_link_text("some-file.txt").click()


time.sleep(3)
driver.quit()

