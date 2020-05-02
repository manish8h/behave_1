"""
This module contains environment controls:
http://behave.readthedocs.io/en/latest/api.html#environment-file-functions
The functions handle Selenium WebDriver setup and cleanup.
(Alternatively, fixtures could be used:
http://behave.readthedocs.io/en/latest/fixtures.html)
"""

from selenium import webdriver


def before_scenario(context, scenario):
    if 'web' in context.tags:
        context.browser = webdriver.Chrome()
        context.browser.implicitly_wait(10)


def after_scenario(context, scenario):
    print(context.failed)
    if 'web' in context.tags:
        context.browser.quit()
