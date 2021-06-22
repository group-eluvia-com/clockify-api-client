from clockify_api_client.factories.abstract_factory import AbstractFactory
from clockify_api_client.models.client import Client


class ClientFactory(AbstractFactory):
    class Meta:
        model = Client
