from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://google.com')
input_search = driver.find_element(By.NAME, 'q')
input_search.send_keys('first test')
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@class="aajZCb"]/descendant::input[@name="btnK"]'))
).click()
driver.save_screenshot('result.png')
