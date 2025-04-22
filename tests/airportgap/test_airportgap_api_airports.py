import requests
from api_support.airportgap import airportgap_auth_header


def test_get_all_airports():
    base_url = "https://airportgap.com/api"
    endpoint = "/airports"
    full_url = f'{base_url}{endpoint}'

    response = requests.get(full_url)

    print(response.text)

    assert response.status_code == 200
