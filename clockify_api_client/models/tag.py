import logging
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class Tag(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(Tag, self).__init__(api_key=api_key, api_url=api_url)

    async def get_tags(self, workspace_id, params=None):
        """Gets list of tags from Clockify.
        :param workspace_id  Id of workspace.
        :param params        Request URL query parameters.
        :return              List with dictionaries with tag object representation.
        """
        try:
            if params:
                url_params = urlencode(params)
                url = self.base_url + '/workspaces/' + workspace_id + '/tags?' + url_params
            else:
                url = self.base_url + '/workspaces/' + workspace_id + '/tags/'
            return await self.get(url)

        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e
