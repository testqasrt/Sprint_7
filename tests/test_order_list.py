from http import HTTPStatus

import allure


class TestOrderList:
    LIMIT = 10
    PAGE = 1

    @allure.title('Отображение списка заказов')
    def test_order_list(self, client):
        response = client.get_orders(
            params=dict(limit=self.LIMIT, page=self.PAGE)
        )
        response_json = response.json()
        assert response.status_code == HTTPStatus.OK
        assert 'orders' in response_json
        assert isinstance(response_json['orders'], list)
