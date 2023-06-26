from clockify_api_client.factories.abstract_factory import AbstractFactory
from clockify_api_client.models.custom_field import CustomField


class CustomFieldFactory(AbstractFactory):
    class Meta:
        model = CustomField
