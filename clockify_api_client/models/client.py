import logging
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class Client(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(Client, self).__init__(api_key=api_key, api_url=api_url)


    async def add_client(self, workspace_id, name=None, note=None):
        """Adds new client.
        :param workspace_id Id of workspace to look for clients.
        :param name         Name of the new client.
        :param note         Description of client
        :return             Dictionary representation of new client.
        """
        try:
            assert name
            data = {
                'name': name,
                'note' : note
            }
            url = self.base_url + '/workspaces/' + workspace_id + '/clients/'
            return await self.post(url, payload=data)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    async def get_clients(self, workspace_id, params=None):
        """Returns all clients.
        :param workspace_id Id of workspace to look for clients.
        :param params       URL params of request.
        :return             List of clients(dict objects).
        """
        try:
            if params:
                url_params = urlencode(params, doseq=True)
                url = self.base_url + '/workspaces/' + workspace_id + '/clients?' + url_params
            else:
                url = self.base_url + '/workspaces/' + workspace_id + '/clients/'
            return await self.get(url)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e
