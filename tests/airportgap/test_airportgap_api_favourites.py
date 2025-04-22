import requests
import os
import logging
from api_support.airportgap import airportgap_auth_header
from api_support.api_env import ApiEnv


def test_favourites_post():
    env = ApiEnv(os.getenv("TEST_REGION"))
    base_url = env.read_value('airportgap_api_base_url')
    endpoint = "/favorites"
    full_url = f'{base_url}{endpoint}'
    data = {"airport_id": 'YBL', "note": 'A great airport'}

    response = requests.post(full_url,
                             headers=airportgap_auth_header(),
                             data=data)

    assert response.status_code == 201


def test_favourites_get():
    env = ApiEnv(os.getenv("TEST_REGION"))
    base_url = env.read_value('airportgap_api_base_url')
    endpoint = "/favorites"
    full_url = f'{base_url}{endpoint}'

    response = requests.get(full_url, headers=airportgap_auth_header())

    logging.debug(response.text)

    assert response.status_code == 200


def test_favourites_clear_all():
    env = ApiEnv(os.getenv("TEST_REGION"))
    base_url = env.read_value('airportgap_api_base_url')
    endpoint = "/favorites/clear_all"
    full_url = f'{base_url}{endpoint}'

    response = requests.delete(full_url, headers=airportgap_auth_header())
    logging.debug(response.text)

    assert response.status_code == 204
