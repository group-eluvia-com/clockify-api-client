from clockify_api_client.factories.abstract_factory import AbstractFactory
from clockify_api_client.models.user import User


class UserFactory(AbstractFactory):
    class Meta:
        model = User

    api_key = None
