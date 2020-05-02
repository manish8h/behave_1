from selenium import webdriver
import time
driver = webdriver.Chrome()

url = "https://www.google.com/"
window_url = "https://the-internet.herokuapp.com/windows"

# driver.get(window_url)
driver.get(url)

#will till 10sec to load the page
driver.set_page_load_timeout(10)


# driver.find_element_by_link_text("Click Here").click()

time.sleep(3)
driver.quit()
