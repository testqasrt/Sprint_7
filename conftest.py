import pytest
from qa_scooter_client import QAScooterClient
from helpers.courier_data_helper import generate_random_register_data


@pytest.fixture
def delete_courier():
    def _delete_courier(client, user_data):
        id = client.post_login(data=user_data).json().get('id')
        client.delete_courier(id)
    return _delete_courier


@pytest.fixture
def client():
    client = QAScooterClient()
    client.session.headers.update({'Content-Type': 'application/json'})
    return client


@pytest.fixture
def user_data():
    return generate_random_register_data()

