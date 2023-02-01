from selenium.webdriver.common.by import By

from tests.utils import auth_user, request_auth_form


def test_main_page(driver_init):
    driver = driver_init
    form = request_auth_form(driver)

    email = "xalax48121@xegge.com"
    password = "KivAknZcs5yep"
    auth_user(form, email, password)

    expected_url = "https://petfriends.skillfactory.ru/all_pets"
    assert driver.current_url == expected_url, "login error"
    assert driver.title == "PetFriends: My Pets"

    header = driver.find_element(By.XPATH, '//div[@id="navbarNav"]/..')
    nav_burger = header.find_element(By.CSS_SELECTOR, 'button[data-target="#navbarNav"]')
    nav_burger.click()

    brand_link = header.find_element(By.CSS_SELECTOR, 'a[href="/"]')
    assert brand_link.text == "PetFriends"

    user_pets_link = header.find_element(By.CSS_SELECTOR, 'a[href="/my_pets"]')
    assert user_pets_link.text == "Мои питомцы"

    all_pets_link = header.find_element(By.CSS_SELECTOR, 'a[href="/all_pets"]')
    assert all_pets_link.text == "Все питомцы"

    logout_button = header.find_element(
        By.CSS_SELECTOR, "button[onclick=\"document.location='/logout';\"]"
    )
    assert logout_button.text == "Выйти"

    cards = driver.find_elements(By.CSS_SELECTOR, ".card-deck>.card")
    assert len(cards) > 0
