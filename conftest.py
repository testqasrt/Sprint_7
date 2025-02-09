import pytest

from helpers.courier_data_helper import generate_random_register_data
from qa_scooter_client import QAScooterClient


@pytest.fixture
def delete_courier_list(client):
    courier_list = []
    yield courier_list
    for courier_data in courier_list:
        try:
            client.delete_courier(
                client.post_login(data=courier_data).json().get("id")
            )
        except Exception:
            # При возникновении ошибок при попытке удаления курьера
            # всегда будет происходить запись данных в файл,
            # который можно использовать для анализа после прохождения тестов
            with open('couriers_to_delete.txt', 'w') as f:
                f.write(str(courier_data) + "\n")


@pytest.fixture
def client():
    client = QAScooterClient()
    client.session.headers.update({"Content-Type": "application/json"})
    return client


@pytest.fixture
def user_data():
    return generate_random_register_data()
