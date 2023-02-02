from selenium.webdriver.common.by import By

from tests.utils import (
    auth_user,
    request_auth_form,
    toggle_navbar_visible,
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

    toggle_navbar_visible(driver)

    user_pets_link = wait_of_element_located(xpath='//a[@href="/my_pets"]', driver=driver)
    user_pets_link.click()

    expected_url = "https://petfriends.skillfactory.ru/my_pets"
    assert driver.current_url == expected_url

    user_stats_container = wait_of_element_located(xpath="//h2/parent::div", driver=driver)
    assert is_visible(user_stats_container)

    user_stats_lines = user_stats_container.text.splitlines()
    pets_count_line = list(filter((lambda e: (e.startswith("Питомцев"))), user_stats_lines))[0]
    pets_count = int(pets_count_line.split(":")[-1].strip())
    assert pets_count

    pets_table = wait_of_element_located(xpath="//div[@id='all_my_pets']/table", driver=driver)

    driver.implicitly_wait(1)

    rows = pets_table.find_elements(By.XPATH, "//tbody/tr")
    pets_list = []
    pets_names = []
    for row in rows:
        name, breed, age, _ = row.find_elements(By.TAG_NAME, "td")
        name = name.text.strip().lower()
        breed = breed.text.strip().lower()
        age = int(age.text)

        assert name not in pets_names, f"Повторяющееся имя: {name}"
        pets_names.append(name)

        pet_data = (name, breed, age)
        assert pet_data not in pets_list, f"Есть повторяющиеся питомцы: {pet_data}"
        pets_list.append(pet_data)
