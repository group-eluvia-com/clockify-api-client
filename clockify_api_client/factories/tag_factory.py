from clockify_api_client.factories.abstract_factory import AbstractFactory
from clockify_api_client.models.tag import Tag


class TagFactory(AbstractFactory):
    class Meta:
        model = Tag

    api_key = None