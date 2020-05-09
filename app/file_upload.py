from selenium import webdriver
import time

url = "https://the-internet.herokuapp.com/upload"
text_file = "/Users/manish/PycharmProjects/behave_1/app/test_upload.txt"

driver = webdriver.Chrome()

driver.get(url)

driver.find_element_by_id("file-upload").send_keys(text_file)
driver.find_element_by_id("file-submit").click()


time.sleep(3)
driver.quit()