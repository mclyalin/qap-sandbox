from tests.utils import auth_user, request_auth_form


def test_user_auth(driver_init):
    email = "xalax48121@xegge.com"
    password = "KivAknZcs5yep"
    form = request_auth_form(driver_init)
    auth_user(form, email, password)

    expected_url = "https://petfriends.skillfactory.ru/all_pets"
    assert driver_init.current_url == expected_url, "login error"
