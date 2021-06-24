import logging
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class User(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(User, self).__init__(api_key=api_key, api_url=api_url)

    def get_current_user(self):
        """Get user by paired with API key.
        :return User dictionary representation.
        """
        try:
            url = self.base_url + '/user/'
            return self.get(url)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def get_users(self, workspace_id, params=None):
        """Returns list of all users in given workspace.
        :param workspace_id Id of workspace.
        :param params       Request URL query params.
        :return             List of Users dictionary representation.
        """
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

    def add_user(self, workspace_id, email):
        """Adds new user into workspace.
        :param workspace_id Id of workspace.
        :param email        Email of new user.
        :return             Dictionary representation of user."""
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/users/'
            emails = list()
            emails.append(email)
            data = {'emails': emails}
            return self.post(url, data)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def update_user(self, workspace_id, user_id, payload):
        """Adds new user into workspace.
        :param workspace_id Id of workspace.
        :param user_id      User Id.
        :param payload      User data to update.
        :return             Dictionary representation of user.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/users/' + user_id
            return self.put(url, payload)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def remove_user(self, workspace_id, user_id):
        """Removes user from workspace.
        :param workspace_id Id of workspace.
        :param user_id      User Id.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/users/' + user_id
            return self.delete(url)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e
