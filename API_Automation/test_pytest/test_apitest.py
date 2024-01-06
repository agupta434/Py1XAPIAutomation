import pytest
import requests

def test_sample1():
    assert 4 == 4

def test_sample2():
    assert 4 == 10

def test_get_request():
    id = 1245
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + str(id)
    print(full_url)
    response_body = requests.get(full_url)

    # with invalid id assertion will give error because sc != 200
    assert response_body.status_code == 200

    data = response_body.json()
    print(type(data))

    # verification of key
    assert 'firstname' in data, "firstname not present"
    assert 'lastname' in data, "lastname not present"

    # verification of data
    assert data["firstname"] == "Amit", "Incorrect firstname"
    assert data["lastname"] == "Gupta", "Incorrect lastname"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "Incorrect dates"


# if __name__ == "__main__":
#     main()