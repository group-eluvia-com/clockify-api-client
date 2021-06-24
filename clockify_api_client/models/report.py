import logging

from clockify_api_client.abstract_clockify import AbstractClockify


class Report(AbstractClockify):
    def __init__(self, api_key, api_url):
        super(Report, self).__init__(api_key=api_key, api_url=api_url)
        self.base_url = f'https://reports.{api_url}'.strip('/')

    def get_summary_report(self, workspace_id, payload):
        """Calls Clockify API for summary report. Returns summary report object(Dictionary)
        :param workspace_id Id of workspace for report.
        :param payload      Body of request for summary report.
        :return             Dictionary with summary report.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/reports/summary/'
            return self.post(url, payload)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def get_detailed_report(self, workspace_id, payload):
        """Calls Clockify API for detailed report. Returns detailed report object(Dictionary)
        :param workspace_id Id of workspace for report.
        :param payload      Body of request for detailed report.
        :return             Dictionary with detailed report.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/reports/detailed/'
            return self.post(url, payload)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def get_weekly_report(self, workspace_id, payload):
        """Calls Clockify API for weekly report. Returns weekly report object(Dictionary)
        :param workspace_id Id of workspace for report.
        :param payload      Body of request for weekly report.
        :return             Dictionary with weekly report.
        """
        try:
            url = self.base_url + '/workspaces/' + workspace_id + '/reports/weekly/'
            return self.post(url, payload)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e
