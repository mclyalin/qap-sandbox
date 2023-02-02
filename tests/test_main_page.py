from selenium.webdriver.common.by import By

from tests.utils import (
    auth_user,
    request_auth_form,
    toggle_navbar_visible,
    is_visible,
    is_clickable,
)


def test_main_page(driver_init):
    driver = driver_init

    email = "xalax48121@xegge.com"
    password = "KivAknZcs5yep"
    form = request_auth_form(driver)
    auth_user(form, email, password)

    expected_url = "https://petfriends.skillfactory.ru/all_pets"
    assert driver.current_url == expected_url, "login error"
    assert driver.title == "PetFriends: My Pets"

    header = driver.find_element(By.XPATH, '//div[@id="navbarNav"]/..')

    brand_link = header.find_element(By.CSS_SELECTOR, 'a[href="/"]')
    assert is_clickable(brand_link)
    assert brand_link.text == "PetFriends"

    logout_button = header.find_element(
        By.CSS_SELECTOR, "button[onclick=\"document.location='/logout';\"]"
    )
    assert is_clickable(logout_button)
    assert logout_button.text == "Выйти"

    navbar = toggle_navbar_visible(driver)

    user_pets_link = navbar.find_element(By.CSS_SELECTOR, '[href="/my_pets"]')
    assert is_clickable(user_pets_link)
    assert user_pets_link.text == "Мои питомцы"

    all_pets_link = navbar.find_element(By.CSS_SELECTOR, '[href="/all_pets"]')
    assert is_clickable(all_pets_link)
    assert all_pets_link.text == "Все питомцы"

    cards = driver.find_elements(By.CSS_SELECTOR, ".card-deck>.card")
    assert len(cards) > 0

    for card in cards:
        photo = card.find_element(By.CSS_SELECTOR, "img.card-img-top")
        title = card.find_element(By.CSS_SELECTOR, "h5.card-title")
        text = card.find_element(By.CSS_SELECTOR, "p.card-text")

        assert is_visible(card)
        assert is_visible(photo)
        assert is_visible(title)
        assert is_visible(text)
