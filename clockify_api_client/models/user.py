import logging
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class User(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(User, self).__init__(api_key=api_key, api_url=api_url)

    def get_user(self, user_id):
        """Get user by ID.
        :param user_id  ID of user.
        :return         User dictionary representation."""
        try:
            url = self.base_url + '/users/' + str(user_id)
            return self.get(url)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def get_all_workspace_users(self, workspace_id, params=None):
        """Returns list of all users in given workspace.
        :param workspace_id Id of workspace.
        :param params       Request URL query params.
        :return             List of Users dictionary representation."""
        try:
            if params:
                params = urlencode(params, doseq=True)
                url = self.base_url + '/workspaces/' + workspace_id + '/users?' + params
            else:
                url = self.base_url + '/workspaces/' + workspace_id + '/users/'
            return self.get(url)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def add_new_user(self, workspace_id, email):
        """Adds new user into workspace.
        :param workspace_id Id of workspace.
        :param email        Email of new user.
        :return             Dictionary representation of user."""
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/users'
            emails = list()
            emails.append(email)
            data = {'emails': emails}
            return self.post(url, data)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e
