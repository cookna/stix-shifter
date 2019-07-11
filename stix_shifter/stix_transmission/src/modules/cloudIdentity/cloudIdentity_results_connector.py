from ..base.base_results_connector import BaseResultsConnector
import json
from .....utils.error_response import ErrorResponder


class CloudIdentityResultsConnector(BaseQueryConnector):
    def __init__(self, api_client):
        self.api_client = api_client

    def create_results_connector(self):
        