import logging
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class Client(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(Client, self).__init__(api_key=api_key, api_url=api_url)

    def get_clients(self, workspace_id, params=None):
        """Returns all clients.
        :param workspace_id Id of workspace to look for clients.
        :param params       URL params of request.
        :return             List of clients(dict objects).
        """
        try:
            if params:
                url_params = urlencode(params, doseq=True)
                url = self.base_url + '/workspaces/' + workspace_id + '/clients&' + url_params
            else:
                url = self.base_url + '/workspaces/' + workspace_id + '/clients/'
            return self.get(url)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def add_client(self, workspace_id, client_name):
        """Add new client into workspace.
        :param workspace_id Id of workspace.
        :param client_name name of client
        :return             Dictionary representation of new project.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/clients/'
            data = {
                'name': client_name
            }
            return self.post(url, data)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e
