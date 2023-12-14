import configuration
import data
import requests


# Здор Андрей, 11 когорта - Финальный проект, Инженер по тестированию плюс
def test_create_order():
    response_create_order = requests.post(configuration.BASE_URL + configuration.CREATE_ORDER_PATH,
                                          json=data.order,
                                          headers=data.headers)
    global order_track_number
    order_track_number = response_create_order.json().get("track")
    assert response_create_order.status_code == 201


def test_get_order_by_track():
    response_get_order_by_track = requests.get(configuration.BASE_URL + configuration.GET_ORDER_BY_TRACK_PATH,
                                               params={"t": order_track_number}, headers=data.headers)

    assert response_get_order_by_track.status_code == 200
