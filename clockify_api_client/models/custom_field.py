import logging
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify


class CustomField(AbstractClockify):

    def __init__(self, api_key, api_url):
        super(CustomField, self).__init__(api_key=api_key, api_url=api_url)


    #def add_client(self, workspace_id, name=None, note=None):
        #"""Adds new client.
        #:param workspace_id Id of workspace to look for clients.
        #:param name         Name of the new client.
        #:param note         Description of client
        #:return             Dictionary representation of new client.
        #"""
        #try:
            #assert name
            #data = {
                #'name': name,
                #'note' : note
            #}
            #url = self.base_url + '/workspaces/' + workspace_id + '/clients/'
            #return self.post(url, payload=data)
        #except Exception as e:
            #logging.error("API error: {0}".format(e))
            #raise e

    #def get_clients(self, workspace_id, params=None):
        #"""Returns all clients.
        #:param workspace_id Id of workspace to look for clients.
        #:param params       URL params of request.
        #:return             List of clients(dict objects).
        #"""
        #try:
            #if params:
                #url_params = urlencode(params, doseq=True)
                #url = self.base_url + '/workspaces/' + workspace_id + '/clients?' + url_params
            #else:
                #url = self.base_url + '/workspaces/' + workspace_id + '/clients/'
            #return self.get(url)
        #except Exception as e:
            #logging.error("API error: {0}".format(e))
            #raise e

    def get_custom_fields(self, workspace_id, params=None):
        """Returns all custom fields in the workspace.
        :param workspace_id Id of workspace to look for custom fields.
        :param params       URL params of request.
        :return             List of custom fields(dict objects).
        """
        try:
            if params:
                url_params = urlencode(params, doseq=True)
                url = self.base_url + '/workspaces/' + workspace_id + '/custom-fields?' + url_params
            else:
                url = self.base_url + '/workspaces/' + workspace_id + '/custom-fields/'
            return self.get(url)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e

    def get_project_custom_fields(self, workspace_id, project_id, params={'status': 'VISIBLE',}):
        url_params = urlencode(params, doseq=True)
        url = self.base_url + '/workspaces/' + workspace_id + '/projects/' + project_id + '/custom-fields?' + url_params

        print(url)

        try:
            return self.get(url)
        except Exception as e:
            logging.error('API error: {0}'.format(e))
            raise e

    def update_project_custom_field(self, workspace_id, project_id, custom_field_id, value, isVisible=True):
        """Returns all custom fields in the workspace.
        :param workspace_id Id of workspace.
        :param project_id Id of project.
        :param value Value to set
        :param isVisible Boolean to set visiblity
        """
        try:
            if isVisible:
                status = "VISIBLE"
            else:
                status = "INVISIBLE"

            custom_field_details = {'defaultValue': value,
                                    'status': status}

            url = self.base_url + '/workspace/' + workspace_id + '/projects/' + project_id + '/custom-fields/' + custom_field_id

            return self.patch(url, custom_field_details)
        except Exception as e:
            logging.error("API error: {0}".format(e))
            raise e
