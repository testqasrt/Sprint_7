import json

import allure
from requests.exceptions import RequestException
from requests.sessions import Session


class QAScooterClient:
    URL = "https://qa-scooter.praktikum-services.ru/api/"
    TIMEOUT = 100

    def __init__(self):
        self.session = Session()

    def _request(self, method, url, params=None, data=None):
        if data is None:
            data = dict()
        try:
            response = self.session.request(
                method, self.URL + url, params, json.dumps(data), timeout=self.TIMEOUT
            )
        except RequestException:
            raise ConnectionError("Ошибка соединения")
        return response

    @allure.step("Вызвать метод POST v1/courier")
    def post_courier(self, params=None, data=None):
        return self._request(method="POST", url="v1/courier", params=params, data=data)

    @allure.step("Вызвать метод DELETE v1/courier/{id}")
    def delete_courier(self, id, params=None, data=None):
        return self._request(
            method="DELETE", url=f"v1/courier/{id}", params=params, data=data
        )

    @allure.step("Вызвать метод POST v1/courier/login")
    def post_login(self, params=None, data=None):
        return self._request(
            method="POST", url="v1/courier/login", params=params, data=data
        )

    @allure.step("Вызвать метод POST v1/orders")
    def post_orders(self, params=None, data=None):
        return self._request(method="POST", url="v1/orders", params=params, data=data)

    @allure.step("Вызвать метод GET v1/orders")
    def get_orders(self, params=None, data=None):
        return self._request(method="GET", url="v1/orders", params=params, data=data)

    def __del__(self):
        self.session.close()
