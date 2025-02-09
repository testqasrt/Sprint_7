from http import HTTPStatus

import allure
import pytest

from helpers.order_data_helper import ORDER_DATA_STUB


class TestOrderCreate:
    @allure.title("Создание заказа со значением ключа color")
    @pytest.mark.parametrize(
        "color_data", (("GREY",), ("BLACK",), ("GREY", "BLACK"), ())
    )
    def test_order_create_success_with_color(self, client, color_data):
        order_data = ORDER_DATA_STUB.copy()
        order_data["color"] = [*color_data]
        response = client.post_orders(data=order_data)
        assert response.status_code == HTTPStatus.CREATED
        assert "track" in response.json()
