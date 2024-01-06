import requests

def main():
    # def get(url, params=None, **kwargs):
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/7891")
    print(response_body.text)
    print(response_body.status_code)
    print(response_body.json())
    if response_body.status_code == 200:
        print("TC#1 - GET request is successful")
    else:
        print("TC#1 - GET request is NOT successful")


if __name__ == "__main__":
    main()