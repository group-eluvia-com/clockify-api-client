from .factories.project_factory import ProjectFactory
from .factories.report_factory import ReportFactory
from .factories.task_factory import TaskFactory
from .factories.time_entry_factory import TimeEntryFactory
from .factories.user_factory import UserFactory
from .factories.workspace_factory import WorkspaceFactory
from .utils import Singleton


class ClockifyAPIClient(metaclass=Singleton):
    def __init__(self):
        self.workspaces = None
        self.projects = None
        self.tasks = None
        self.time_entries = None
        self.users = None
        self.reports = None

    def build(self, api_key, api_url):
        """Builds services from available factories."""

        self.workspaces = WorkspaceFactory(api_key=api_key, api_url=api_url)
        self.projects = ProjectFactory(api_key=api_key, api_url=api_url)
        self.tasks = TaskFactory(api_key=api_key, api_url=api_url)
        self.time_entries = TimeEntryFactory(api_key=api_key, api_url=api_url)
        self.users = UserFactory(api_key=api_key, api_url=api_url)
        self.reports = ReportFactory(api_key=api_key, api_url=api_url)
        return self
