from clockify_api_client.factories.abstract_factory import AbstractFactory
from clockify_api_client.models.workspace import Workspace


class WorkspaceFactory(AbstractFactory):
    class Meta:
        model = Workspace

    api_key = None
