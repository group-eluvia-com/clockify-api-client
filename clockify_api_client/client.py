from clockify_api_client.factories.project_factory import ProjectFactory
from clockify_api_client.factories.report_factory import ReportFactory
from clockify_api_client.factories.tag_factory import TagFactory
from clockify_api_client.factories.task_factory import TaskFactory
from clockify_api_client.factories.time_entry_factory import TimeEntryFactory
from clockify_api_client.factories.user_factory import UserFactory
from clockify_api_client.factories.workspace_factory import WorkspaceFactory
from clockify_api_client.factories.client_factory import ClientFactory
from clockify_api_client.factories.custom_field_factory import CustomFieldFactory
from clockify_api_client.utils import Singleton


class ClockifyAPIClient(metaclass=Singleton):
    def __init__(self):
        self.workspaces = None
        self.projects = None
        self.tags = None
        self.tasks = None
        self.time_entries = None
        self.users = None
        self.reports = None
        self.clients = None
        self.custom_fields = None

    def build(self, api_key, api_url):
        """Builds services from available factories.
        :param api_key Clockify API key.
        :param api_url Clockify API url.
        """

        self.workspaces = WorkspaceFactory(api_key=api_key, api_url=api_url)
        self.projects = ProjectFactory(api_key=api_key, api_url=api_url)
        self.tags = TagFactory(api_key=api_key, api_url=api_url)
        self.tasks = TaskFactory(api_key=api_key, api_url=api_url)
        self.time_entries = TimeEntryFactory(api_key=api_key, api_url=api_url)
        self.users = UserFactory(api_key=api_key, api_url=api_url)
        self.reports = ReportFactory(api_key=api_key, api_url=api_url)
        self.clients = ClientFactory(api_key=api_key, api_url=api_url)
        self.custom_fields = CustomFieldFactory(api_key=api_key, api_url=api_url)
        return self
