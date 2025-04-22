"""
Reads json file to load test region values - allowing tests to be run
against multiple test environments - controlled by TEST_REGION
environment variable (currently set in the Dockerfile).
"""
import json


class ApiEnv:

    def __init__(self, test_region):
        self.test_region = test_region

    def read_value(self, key):
        full_filename = f'/src/tests/airportgap/api_support/api_env.json'

        with open(full_filename, 'r') as file:
            data = file.read()

        json_data = json.loads(data)

        return json_data[self.test_region][key]
