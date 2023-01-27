import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# def document_initialised(driver):
#     return driver.execute_script("return initialised")


# def test():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.get('https://google.com')
#     # search_input = WebDriverWait(driver, timeout=10).until(
#     #     lambda d: d.find_element(By.XPATH, '//*[name="q"]')
#     # )
#     time.sleep(5)
#     search_input = driver.find_element(By.XPATH, '//*[name="q"]')
#     search_input.clear()
#     search_input.send_keys('first test')
#     search_input.send_keys(Keys.ENTER)
#     # submit_button = driver.find_element(
#     #   By.XPATH, '//div[@class="aajZCb"]/descendant::input[@name="btnK"]'
#     # )
#     WebDriverWait(driver, timeout=5).until(
#         lambda d: d.save_screenshot('result.png')
#     )

def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """

    # Open google search page:
    selenium.get('https://google.com')

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for search text input:
    search_input = selenium.find_element(By.NAME, "q")

    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('first test')

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search:
    search_button = selenium.find_element(By.NAME, 'btnK')
    search_button.submit()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    selenium.save_screenshot('result.png')