from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class Client(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(Client, self).__init__(api_key=api_key, api_url=api_url)

    def get_clients(self, workspace_id, params=None):
        """Returns all unarchived clients.
        :param workspace_id Id of workspace to look for clients.
        :param params       URL params of request.
        :return             List of clients(dict objects)."""
        if params is None:
            params = {}
        params['archived'] = str(False).lower()
        url_params = urlencode(params, doseq=True)
        url = self.base_url + '/workspaces/' + workspace_id + '/clients?archived=false&' + url_params
        return self.get(url)
