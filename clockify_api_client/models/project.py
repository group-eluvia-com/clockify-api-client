import logging
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class Project(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(Project, self).__init__(api_key=api_key, api_url=api_url)

    def get_projects(self, workspace_id, params=None):
        """Returns projects from given workspace with applied params if provided.
        :param workspace_id Id of workspace.
        :param params       Dictionary with request parameters.
        :return             List of projects.
        """
        try:
            if params:
                url_params = urlencode(params, doseq=True)
                url = self.base_url + '/workspaces/' + workspace_id + '/projects?' + url_params
            else:
                url = self.base_url + '/workspaces/' + workspace_id + '/projects/'
            return self.get(url)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def add_project(self, workspace_id, project_name, client_id, billable=False, public=False, color="#16407B"):
        """Add new project into workspace.
        :param workspace_id Id of workspace.
        :param project_name Name of new project.
        :param client_id    Id of client.
        :param billable     Bool flag.
        :return             Dictionary representation of new project.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/projects/'
            data = {
                'name': project_name,
                "clientId": client_id,
                "isPublic": "true" if public else "false",
                "billable": billable
            }
            return self.post(url, data)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e
