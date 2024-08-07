import logging
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class CustomField(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(CustomField, self).__init__(api_key=api_key, api_url=api_url)

    async def get_custom_fields(self, workspace_id, params=None):
        """Returns all custom fields in the workspace.
        :param workspace_id Id of workspace to look for custom fields.
        :param params       URL params of request.
        :return             List of custom fields (dict objects).
        """
        try:
            if params:
                url_params = urlencode(params, doseq=True)
                url = self.base_url + '/workspaces/' + workspace_id + '/custom-fields?' + url_params
            else:
                url = self.base_url + '/workspaces/' + workspace_id + '/custom-fields/'
            return await self.get(url)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    async def get_project_custom_fields(self, workspace_id, project_id, params={'status': 'VISIBLE',}):
        """Return the custom fields for a specific project.
        :param workspace_id Id of workspace containing the project.
        :param project_id   Id of project to look for custom fields.
        :param params       URL params of request.
        :return             List of custom fields (dict objects).
        """
        try:
            url_params = urlencode(params, doseq=True)
            url = self.base_url + '/workspaces/' + workspace_id + '/projects/' + project_id + '/custom-fields?' + url_params
            return await self.get(url)
        except Exception as e:
            logging.error('API error: {0}'.format(e))
            raise e

    async def update_project_custom_field(self, workspace_id, project_id, custom_field_id, value, isVisible=True):
        """Update specified custom field in the project.
        :param workspace_id    Id of workspace.
        :param project_id      Id of project.
        :param custom_field_id Id of custom field.
        :param value           Value to set the custom field to.
        :param isVisible       Boolean to set visibilty of the custom field.
        :return                Dictionary of updated custom field.
        """
        try:
            if isVisible:
                status = "VISIBLE"
            else:
                status = "INVISIBLE"

            custom_field_details = {'defaultValue': value,
                                    'status': status}

            url = self.base_url + '/workspace/' + workspace_id + '/projects/' + project_id + '/custom-fields/' + custom_field_id

            return await self.patch(url, custom_field_details)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e
