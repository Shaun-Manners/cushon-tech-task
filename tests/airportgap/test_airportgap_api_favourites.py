import requests
from api_support.airportgap import airportgap_auth_header


def test_favourites_post():
    base_url = "https://airportgap.com/api"
    endpoint = "/favorites"
    full_url = f'{base_url}{endpoint}'
    data = {"airport_id": 'YBL', "note": 'A great airport'}

    response = requests.post(full_url,
                             headers=airportgap_auth_header(),
                             data=data)

    assert response.status_code == 201


def test_favourites_get():
    base_url = "https://airportgap.com/api"
    endpoint = "/favorites"
    full_url = f'{base_url}{endpoint}'

    response = requests.get(full_url, headers=airportgap_auth_header())

    print(response.text)

    assert response.status_code == 200


def test_favourites_clear_all():
    base_url = "https://airportgap.com/api"
    endpoint = "/favorites/clear_all"
    full_url = f'{base_url}{endpoint}'

    response = requests.delete(full_url, headers=airportgap_auth_header())

    print(response.text)

    assert response.status_code == 204
