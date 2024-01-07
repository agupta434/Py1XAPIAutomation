# create boking
# URL, Headers, Body(payload),
# verify booking ID and Booking Information JSON
import pytest
import requests

@pytest.mark.positive
def test_create_booking_positive():
    print("Create booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Amit",
        "lastname": "Gupta",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    assert response.status_code == 200, "Invalid Status code"

    # get the response body and verify the JSON, Booking ID is not null
    data = response.json()
    print(data)
    print(data["bookingid"])
    booking_id = data["bookingid"] # this is required for PUT request
    print(booking_id)
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "Amit", "Incorrect First Name"
@pytest.mark.negative
def test_create_booking_negative():
    print("Create booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    assert response.status_code == 500, "Invalid Status code"


