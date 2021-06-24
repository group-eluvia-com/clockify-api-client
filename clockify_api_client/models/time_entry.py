import logging
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class TimeEntry(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(TimeEntry, self).__init__(api_key=api_key, api_url=api_url)

    def get_time_entries(self, workspace_id, user_id, params=None):
        """Returns user time entries.
        :param workspace_id Id of workspace.
        :param user_id      Id of user.
        :param params       Request URL query params.
        :return             List with dictionary representation of time entries from clockify.
        """
        try:
            if params:
                url_params = urlencode(params, doseq=True)
                url = self.base_url + '/workspaces/' + workspace_id + '/user/' + user_id + '/time-entries?' + url_params
            else:
                url = self.base_url + '/workspaces/' + workspace_id + '/user/' + user_id + '/time-entries/'
            time_entries_list = self.get(url)
            return time_entries_list
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def get_time_entry(self, workspace_id, time_entry_id):
        """Gets specific time entry.
        :param workspace_id  Id of workspace.
        :param time_entry_id Id of time entry
        :return              Dictionary representation of time entry.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/time-entries/' + time_entry_id
            return self.get(url)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def update_time_entry(self, workspace_id, entry_id, payload):
        """Updates time entry in Clockify with provided payload data.
        :param workspace_id Id of workspace.
        :param entry_id     Id of time entry.
        :param payload      Dictionary with payload data for update.
        :return             Updated time entry.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/time-entries/' + entry_id
            time_entry = self.put(url, payload)
            return time_entry
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def add_time_entry(self, workspace_id, user_id, payload):
        """Adds time entry in Clockify with provided payload data.
        Paid feature, workspace need to have active paid subscription.
        :param workspace_id Id of workspace.
        :param user_id      Id of workspace.
        :param payload      Dictionary with payload data for update.
        :return             Updated time entry.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/user/' + user_id + '/time-entries/'
            time_entry = self.post(url, payload)
            return time_entry
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e
