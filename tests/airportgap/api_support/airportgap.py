import os


def airportgap_auth_header():
    token = os.getenv("AIRPORT_GAP_API_TOKEN")
    headers = {'Authorization': f'Bearer token={token}'}
    return headers
