from abc import ABC

import requests


class AbstractClockify(ABC):
    def __init__(self, api_key, api_url):

        self.base_url = f'https://global.{api_url}'.strip('/')
        self.api_key = api_key
        self.header = {'X-Api-Key': self.api_key}

    def get(self, url):
        response = requests.get(url, headers=self.header)
        if response.status_code in [200, 201, 202]:
            return response.json()
        raise Exception(response.json())

    def post(self, url, payload):
        response = requests.post(url, headers=self.header, json=payload)
        if response.status_code in [200, 201, 202]:
            return response.json()
        raise Exception(response.json())

    def put(self, url, payload):
        response = requests.put(url, headers=self.header, json=payload)
        if response.status_code in [200, 201, 202]:
            return response.json()
        raise Exception(response.json())

    def delete(self, url):
        response = requests.delete(url, headers=self.header)
        if response.status_code in [200, 201, 202, 204]:
            return response.json()
        raise Exception(response.json())
