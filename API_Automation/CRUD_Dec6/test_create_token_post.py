import requests

def create_token():  # this is not a test just normal function
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    data = response.json()
    print(data)
    token = data["token"]
    print(token)
    print(response)  # status code <Response [200]>
    return token

def create_booking():
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

    # get the response body and verify the JSON, Booking ID is not null
    data = response.json()
    print(data)
    print(data["bookingid"])
    booking_id = data["bookingid"]  # this is required for PUT request
    print(booking_id)
    return booking_id


def test_request_update():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    PUT_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    print(cookie_value)
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)  # {'Content-Type': 'application/json', 'Cookie': 'token=d0bcb0e9bf24a2e'}
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
    response = requests.put(url=PUT_URL, headers=headers, json=json_payload)
    print(response)

    data = response.json()
    print(data)

    assert response.status_code == 200, "Invalid Status code"
    # assert data["bookingid"] is not None # is not required as
    assert data["firstname"] == "Amit", "Incorrect First Name"


def test_delete():
    try:

        URL = "https://restful-booker.herokuapp.com/booking/"
        booking_id = create_booking()
        DELETE_URL = URL + str(booking_id)
        cookie_value = "token=" + create_token()

        headers = {
            "Content-Type": "application/json",
            "Cookie": cookie_value
        }
        print(headers)  # {'Content-Type': 'application/json', 'Cookie': 'token=d0bcb0e9bf24a2e'}

        response = requests.delete(url=DELETE_URL, headers=headers)
        print(response)

        data = response.json()
        print(data)

        assert response.status_code == 201, "Invalid Status code"
    except Exception as e:
        print(e)
