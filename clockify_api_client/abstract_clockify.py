from abc import ABC

import httpx


class AbstractClockify(ABC):
    def __init__(self, api_key, api_url):

        # Current API docs don't contain the "global" and the response time
        # seems faster without it (although it works fine)
        # self.base_url = f'https://global.{api_url}'.strip('/')
        self.base_url = f'https://{api_url}'.strip('/')
        self.api_key = api_key
        self.header = {'X-Api-Key': self.api_key}

    async def get(self, url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.header)
        if response.status_code in [200, 201, 202]:
            return response.json()
        raise Exception(response.json())

    async def post(self, url, payload):
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=self.header, json=payload)
        if response.status_code in [200, 201, 202]:
            return response.json()
        raise Exception(response.json())

    async def put(self, url, payload):
        async with httpx.AsyncClient() as client:
            response = await client.put(url, headers=self.header, json=payload)
        if response.status_code in [200, 201, 202]:
            return response.json()
        raise Exception(response.json())

    async def delete(self, url):
        async with httpx.AsyncClient() as client:
            response = await client.delete(url, headers=self.header)
        if response.status_code in [200, 201, 202, 204]:
            return response.json()
        raise Exception(response.json())

    async def patch(self, url, payload):
        async with httpx.AsyncClient() as client:
            response = await client.patch(url, headers=self.header, json=payload)
        if response.status_code in [200, 201, 202, 204]:
            return response.json()
        raise Exception(response.json())
