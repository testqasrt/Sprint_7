from http import HTTPStatus

import allure
import pytest

from helpers.response_messages_helper import (CREATE_ERROR_FIELD_MESSAGE,
                                              DUPLICATE_COURIER_MESSAGE)


class TestCreateCourier:
    @pytest.fixture
    def user_data_without_login(self, user_data):
        user_data.pop('login')
        return user_data

    @pytest.fixture
    def user_data_without_password(self, user_data):
        user_data.pop('password')
        return user_data

    @pytest.fixture
    def user_data_without_firstName(self, user_data):
        user_data.pop('firstName')
        return user_data

    @allure.title('Успешная регистрация курьера')
    @pytest.mark.parametrize(
        'data',
        ('user_data', 'user_data_without_firstName')
    )
    def test_create_courier_success(self, request, client, data, delete_courier):
        data = request.getfixturevalue(data)
        response = client.post_courier(data=data)
        response_json = response.json()
        delete_courier(client, data)
        assert response.status_code == HTTPStatus.CREATED
        assert 'ok' in response.json()
        assert response_json.get('ok') is True


    @allure.title('Регистрация существующего курьера')
    def test_create_duplicate_courier(self, client, user_data, delete_courier):
        client.post_courier(data=user_data)
        response = client.post_courier(data=user_data)
        assert response.status_code == HTTPStatus.CONFLICT
        assert response.json().get('message') == DUPLICATE_COURIER_MESSAGE
        delete_courier(client, user_data)

    @allure.title('Создание курьера без обязательных ключей в теле запроса')
    @pytest.mark.parametrize(
        'data',
        ('user_data_without_login', 'user_data_without_password'),
    )
    def test_create_courier_without_required_key(self, request, client, data):
        response = client.post_courier(data=request.getfixturevalue(data))
        assert response.status_code == HTTPStatus.BAD_REQUEST
        assert response.json().get('message') == CREATE_ERROR_FIELD_MESSAGE
