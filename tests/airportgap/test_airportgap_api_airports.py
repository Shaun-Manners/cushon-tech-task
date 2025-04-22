import requests
import os
import logging
from api_support.airportgap import airportgap_auth_header
from api_support.api_env import ApiEnv


def test_get_all_airports():
    env = ApiEnv(os.getenv("TEST_REGION"))
    base_url = env.read_value('airportgap_api_base_url')
    endpoint = "/airports"
    full_url = f'{base_url}{endpoint}'

    response = requests.get(full_url)
    logging.debug(response.text)

    assert response.status_code == 200
