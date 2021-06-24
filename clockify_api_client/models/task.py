import logging
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class Task(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(Task, self).__init__(api_key=api_key, api_url=api_url)

    def add_task(self, workspace_id, project_id, task_name, request_data=None):
        """Creates new task in Clockify.
        :param workspace_id  Id of workspace.
        :param request_data  Dictionary with request data.
        :param project_id    Id of project.
        :param task_name     Name of new task.
        :return              Dictionary with task object representation.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/projects/' + project_id + '/tasks/'
            payload = {'name': task_name, 'projectId': project_id}
            if request_data:
                payload = {**payload, **request_data}
            return self.post(url, payload)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def update_task(self,  workspace_id, project_id, task_id, request_data=None):
        """Updates task in Clockify.
        :param workspace_id  Id of workspace.
        :param project_id    Id of project.
        :param task_id       Id of task.
        :param request_data  Dictionary with request data.
        :return              Dictionary with task object representation.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/projects/' + project_id + '/tasks/' + task_id
            return self.put(url, request_data)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def get_tasks(self, workspace_id, project_id, params=None):
        """Gets list of tasks from Clockify.
        :param workspace_id  Id of workspace.
        :param project_id    Id of project.
        :param params        Request URL query parameters.
        :return              List with dictionaries with task object representation.
        """
        try:
            if params:
                url_params = urlencode(params)
                url = self.base_url + '/workspaces/' + workspace_id + '/projects/' + project_id + '/tasks?' + url_params
            else:
                url = self.base_url + '/workspaces/' + workspace_id + '/projects/' + project_id + '/tasks/'
            return self.get(url)

        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def get_task(self, workspace_id, project_id, task_id):
        """Gets task from Clockify.
        :param workspace_id  Id of workspace.
        :param project_id    Id of project.
        :param task_id       Request URL query parameters.
        :return              List with dictionaries with task object representation.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/projects/' + project_id + '/tasks/' + task_id
            return self.get(url)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e
