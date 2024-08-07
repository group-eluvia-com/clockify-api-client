import logging
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class Project(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(Project, self).__init__(api_key=api_key, api_url=api_url)

    async def get_projects(self, workspace_id, params=None):
        """Returns projects from given workspace with applied params if provided.
        :param workspace_id Id of workspace.
        :param params       Dictionary with request parameters.
        :return             List of projects.
        """
        # TODO: Pagination should not be implemented in this way. It should be done in
        #  the abstract class so that all methods can use it.
        try:
            page = 1
            all_projects = []
            while True:
                params = params or {}
                params.update({"page": page, "page-size": 50})
                url_params = urlencode(params, doseq=True)
                url = self.base_url + '/workspaces/' + workspace_id + '/projects?' + url_params
                response = await self.get(url)
                if not response:  # No more projects
                    break
                all_projects.extend(response)
                page += 1
            return all_projects
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    async def add_project(self, workspace_id, project_name, client_id, billable=False, public=False, color="#16407B"):
        """Add new project into workspace.
        :param workspace_id Id of workspace.
        :param project_name Name of new project.
        :param client_id    Id of client.
        :param billable     Bool flag. Indicates whether project is billable or not.
        :param public       Bool flag. Indicates whether project is public or not.
        :param color        Color code starting with # followed by 6 hex digits.
        :return             Dictionary representation of new project.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/projects/'
            data = {
                "name": project_name,
                "clientId": client_id,
                "isPublic": "true" if public else "false",
                "billable": billable
            }
            return await self.post(url, data)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    async def add_project_from_dict(self, workspace_id, project_dict):
        """Add new project into workspace, built from a dictionary.
        :param workspace_id ID of workspace.
        :param project_dict Dictionary containing all the project details.
        :return             Dictionary representation of new project.
        """
        
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/projects/'
            return await self.post(url, project_dict)
        except Exception as e:
            logging.error('API error:{0}'.format(e))
            raise e

