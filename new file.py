import configuration
import data
import requests
#Здор Андрей, 11 когорта - Финальный проект, Инженер по тестированию плюс
response_create_order = requests.post(configuration.BASE_URL + configuration.CREATE_ORDER_PATH, json=data.order,
                                      headers=data.headers)
order_track_number = response_create_order.json().get("track")
print(order_track_number)

assert response_create_order.status_code == 201, f"Failed to create order. Response: {response_create_order.text}"

response_get_order_by_track = requests.get(configuration.BASE_URL + configuration.GET_ORDER_BY_TRACK_PATH,
                                           params={"t": order_track_number}, headers=data.headers)

assert response_get_order_by_track.status_code == 200, f"Failed to get order by track. Response: {response_get_order_by_track.text}"

print(order_track_number)
print(response_get_order_by_track.status_code)
