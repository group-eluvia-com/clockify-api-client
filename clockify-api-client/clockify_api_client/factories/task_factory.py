from clockify_api_client.factories.abstract_factory import AbstractFactory
from clockify_api_client.models.task import Task


class TaskFactory(AbstractFactory):
    class Meta:
        model = Task

    api_key = None
