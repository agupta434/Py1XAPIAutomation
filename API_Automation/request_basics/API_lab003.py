import requests

# def get(url, params=None, **kwargs):
response_body = requests.get("https://restful-booker.herokuapp.com/booking/7891")
print(response_body.text)
print(response_body.status_code)
print(response_body.headers)
    