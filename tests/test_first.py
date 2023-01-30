from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


# Функция ожидания элементов
def wait_of_element_located(xpath, driver_init):
    element = WebDriverWait(driver_init, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


def auth_user(email, password, driver_init):
    register_button = wait_of_element_located(
        xpath="//button[@onclick=\"document.location='/new_user';\"]", driver_init=driver_init
    )
    register_button.click()

    login_button = wait_of_element_located(
        xpath="//a[@href='/login']", driver_init=driver_init
    )
    login_button.click()

    login_form = wait_of_element_located(
        xpath='//form[@action="/login"]', driver_init=driver_init
    )

    input_email = login_form.find_element(By.ID, 'email')
    input_email.clear()
    input_email.send_keys(email)

    input_password = login_form.find_element(By.ID, 'pass')
    input_password.clear()
    input_password.send_keys(password)

    login_form.submit()


def test_petfriends(driver_init):
    auth_user('xalax48121@xegge.com', 'KivAknZcs5yep', driver_init=driver_init)

    assert driver_init.current_url == 'https://petfriends.skillfactory.ru/all_pets', 'login error'

    # WebDriverWait(driver, 5).until(
    #     EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))
    # ).click()
    # email = WebDriverWait(driver, 5).until(
    #     lambda d: d.find_element()
    # )
    # email.clear()
    # email.send_keys('xalax48121@xegge.com')

    # password = driver.find_element(By.ID, 'pass')
    # password.clear()
    # password.send_keys('KivAknZcs5yep')

    # form = driver.find_element(By.XPATH, '//form[@action="/login"]')
    # form.submit()

    # assert driver.current_url == 'https://petfriends.skillfactory.ru/all_pets', 'login error'

    # driver.save_screenshot('result.png')
