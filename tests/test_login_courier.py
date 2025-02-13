from http import HTTPStatus

import allure
import pytest

from helpers.courier_data_helper import REGISTERED_USER_DATA
from helpers.response_messages_helper import (
    LOGIN_ERROR_FIELD_MESSAGE, LOGIN_ERROR_USER_NOT_FOUND_MESSAGE)


class TestLoginCourier:
    @pytest.fixture
    def user_data(self):
        return REGISTERED_USER_DATA.copy()

    @pytest.fixture
    def success_user_data(self, user_data):
        user_data.pop("firstName")
        id = user_data.pop("id")
        return user_data, id

    @pytest.fixture
    def user_data_without_password(self, user_data):
        user_data.pop("firstName")
        user_data.pop("id")
        user_data.pop("password")
        return user_data

    @pytest.fixture
    def user_data_without_login(self, user_data):
        user_data.pop("firstName")
        user_data.pop("id")
        user_data.pop("login")
        return user_data

    @pytest.fixture
    def user_data_incorrect_password(self, user_data):
        user_data["password"] = user_data["password"] + "_incorrect"
        return user_data

    @pytest.fixture
    def user_data_incorrect_login(self, user_data):
        user_data["login"] = user_data["login"] + "_incorrect"
        return user_data

    @allure.title("Успешный логин курьера")
    def test_login_success(self, client, success_user_data):
        data, id = success_user_data
        response = client.post_login(data=data)
        response_json = response.json()
        assert response.status_code == HTTPStatus.OK
        assert "id" in response_json
        assert response_json.get("id") == id

    @allure.title("Логин курьера без обязательных ключей в теле запроса")
    @pytest.mark.parametrize(
        "data", ("user_data_without_password", "user_data_without_login")
    )
    def test_login_without_required_key(self, request, client, data):
        response = client.post_login(data=request.getfixturevalue(data))
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json().get("message") == LOGIN_ERROR_FIELD_MESSAGE

    @allure.title("Логин курьера с некорректным значением ключа")
    @pytest.mark.parametrize(
        "data", ("user_data_incorrect_password", "user_data_incorrect_login")
    )
    def test_login_with_incorrect_key(self, request, client, data):
        response = client.post_login(data=request.getfixturevalue(data))
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert response.json().get("message") == LOGIN_ERROR_USER_NOT_FOUND_MESSAGE
