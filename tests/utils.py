from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_of_element_located(xpath, driver, time=5):
    element = WebDriverWait(driver, time).until(EC.presence_of_element_located((By.XPATH, xpath)))
    return element


def is_invisible(element):
    return EC.invisibility_of_element(element)


def is_visible(element):
    return EC.visibility_of(element)


def is_clickable(element):
    return EC.element_to_be_clickable(element)


def request_auth_form(driver):
    register_button = wait_of_element_located(
        xpath="//button[@onclick=\"document.location='/new_user';\"]",
        driver=driver,
    )
    register_button.click()

    auth_form_link = wait_of_element_located(xpath="//a[@href='/login']", driver=driver)
    auth_form_link.click()

    auth_form = wait_of_element_located(xpath='//form[@action="/login"]', driver=driver)
    return auth_form


def toggle_navbar_visible(driver):
    navbar = wait_of_element_located(xpath='//*[@id="navbarNav"]', driver=driver)
    if is_invisible(navbar):
        nav_burger = wait_of_element_located(
            xpath='//*[@class="navbar-toggler"][@data-target="#navbarNav"]', driver=driver
        )
        nav_burger.click()
    return navbar


def auth_user(auth_form, email, password):
    input_email = auth_form.find_element(By.ID, "email")
    input_email.clear()
    input_email.send_keys(email)

    input_password = auth_form.find_element(By.ID, "pass")
    input_password.clear()
    input_password.send_keys(password)

    auth_form.submit()
