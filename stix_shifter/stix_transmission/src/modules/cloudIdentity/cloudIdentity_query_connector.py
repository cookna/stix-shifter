from ..base.base_query_connector import BaseQueryConnector
import json
from .....utils.error_response import ErrorResponder
from .qradar_error_mapper import ErrorMapper


class CloudIdentityQueryConnector(BaseQueryConnector): 
    def __init__(self, api_client):
        self.api_client = api_client

    def create_query_connector(self, query):

        