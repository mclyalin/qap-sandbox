from selenium.webdriver.common.by import By

from tests.utils import (
    auth_user,
    request_auth_form,
    is_invisible,
    is_visible,
    wait_of_element_located,
)


def request_user_page_link(driver):
    user_pets_link = wait_of_element_located(xpath='//a[@href="/my_pets"]', driver=driver)
    if is_invisible(user_pets_link):
        nav_burger = wait_of_element_located(
            xpath='//*[@class="navbar-toggler"][@data-target="#navbarNav"]', driver=driver
        )
        nav_burger.click()
    return user_pets_link


def test_user_pets(driver_init):
    driver = driver_init

    email = "xalax48121@xegge.com"
    password = "KivAknZcs5yep"
    form = request_auth_form(driver)
    auth_user(form, email, password)

    user_pets_link = wait_of_element_located(xpath='//a[@href="/my_pets"]', driver=driver)
    user_pets_link.click()

    expected_url = "https://petfriends.skillfactory.ru/my_pets"
    assert driver.current_url == expected_url

    user_stats_container = wait_of_element_located(xpath="//h2/parent::div", driver=driver)
    assert is_visible(user_stats_container)

    user_stats_lines = user_stats_container.text.splitlines()
    pets_count_line = list(filter((lambda e: (e.startswith("Питомцев"))), user_stats_lines))[0]
    pets_count = int(pets_count_line.split(":")[-1].strip())

    pets_table = wait_of_element_located(xpath="//div[@id='all_my_pets']/table", driver=driver)

    driver.implicitly_wait(1)

    rows = pets_table.find_elements(By.XPATH, "//tbody/tr")
    assert len(rows) == pets_count

    pets = []
    for row in rows:
        name, breed, age, _ = row.find_elements(By.TAG_NAME, "td")
        photo = row.find_element(By.TAG_NAME, "img")
        pet = {
          'name': name.text.strip().lower(),
          'breed': breed.text.strip().lower(),
          'age': int(age.text),
          'photo': photo.get_attribute('src')
        }

        assert pet['name'] and pet['breed'] and pet['age'], f"Неполные данные у питомца: {pet}"
        pets.append(pet)

    unique_pets_count = len(set([str(p.values()) for p in pets]))
    unique_pet_names_count = len(set([p['name'] for p in pets]))
    pets_with_photo_count = len(set([p['photo'] for p in pets]))

    assert unique_pets_count == pets_count, "Есть повторяющиеся питомцы."
    assert unique_pet_names_count == pets_count, "Есть повторяющиеся имена."
    assert pets_with_photo_count >= int(pets_count / 2), "У более половины питомцев нет фото."
