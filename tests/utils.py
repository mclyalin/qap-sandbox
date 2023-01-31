from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_of_element_located(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )
    return element


def request_auth_form(driver):
    register_button = wait_of_element_located(
        xpath="//button[@onclick=\"document.location='/new_user';\"]",
        driver=driver,
    )
    register_button.click()

    auth_form_link = wait_of_element_located(
        xpath="//a[@href='/login']", driver=driver
    )
    auth_form_link.click()

    result = wait_of_element_located(
        xpath='//form[@action="/login"]', driver=driver
    )
    return result


def auth_user(auth_form, email, password):
    input_email = auth_form.find_element(By.ID, "email")
    input_email.clear()
    input_email.send_keys(email)

    input_password = auth_form.find_element(By.ID, "pass")
    input_password.clear()
    input_password.send_keys(password)

    auth_form.submit()
