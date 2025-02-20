from ..base.base_connector import BaseConnector
from .api_client import APIClient
from ..base.base_status_connector import Status
from json import loads
import pprint
from enum import Enum
from . import CloudIdentity_Request, CloudIdentity_Token
#from CloudIdentity_Token import init



class DatasourceStatus(Enum):
    # WAIT, EXECUTE, SORTING, COMPLETED, CANCELED, ERROR
    WAIT = 'WAIT'
    EXECUTE = 'EXECUTE'
    SORTING = 'SORTING'
    COMPLETED = 'COMPLETED'
    CANCELED = 'CANCELED'
    ERROR = 'ERROR'

class Connector(BaseConnector):
    def __init__(self, connection, configuration):
        return
    def ping(self):
        try:
            response = self.api_client.ping_data_source()
            return response
        except Exception as err:
            print('error when pinging datasource {}:'.format(err))
            raise

    def create_query_connection(self, query):
        token = CloudIdentity_Token.getToken()
        request = query.split(' ')
        print(request)
        #response = self.callApi(token, request[3])
        #print(query.split(' = '))

        try:
            #response = CloudIdentity_Request.getAdminActivity(token, "now-240h", "now", 10, "time","asc")

            return 
        except Exception as err:
            print('error when creating search: {}'.format(err))
            raise

    def callApi(self, token, call, id=None, FROM=None, TO=None, SIZE=None, SORT_BY=None, SORT_ORDER=None):
        if(call == "getUser"):
            return CloudIdentity_Request.getUser(token, id)
        elif(call == "getUsers"):
            return CloudIdentity_Request.getUsers(token)
        elif(call == "getAdminActivity"):
            return CloudIdentity_Request.getAdminActivity(token, FROM, TO, SIZE, SORT_BY, SORT_ORDER)
        else:
            print("Invalid Request")
            return

    def getParams(self, query):
        for val in query:
            if val == "CIFun":
                 
            

    # Map data source status to connector status
    def __getStatus(self, status):
        switcher = {
            DatasourceStatus.WAIT.value: Status.RUNNING,
            DatasourceStatus.EXECUTE.value: Status.RUNNING,
            DatasourceStatus.SORTING.value: Status.RUNNING,
            DatasourceStatus.COMPLETED.value: Status.COMPLETED,
            DatasourceStatus.CANCELED.value: Status.CANCELED,
            DatasourceStatus.ERROR.value: Status.ERROR
        }
        return switcher.get(status).value

    def create_status_connection(self, search_id):
        try:
            response = self.api_client.get_search_status(search_id)
            # Based on the response
            # return_obj['success'] = True or False
            # return_obj['status'] = One of the statuses as defined in the Status class:
            # Status.RUNNING, Status.COMPLETED, Status.CANCELED, Status.ERROR
            # return_obj['progress'] = Some progress code if returned from the API
            # Construct a response object
            response_code = response["code"]
            return_obj = dict()

            if response_code == 200:
                return_obj['success'] = True
                return_obj['status'] = self.__getStatus(response["status"])
            else:
                return_obj['success'] = False
                return_obj['error'] = response['message']
            return return_obj
        except Exception as err:
            print('error when getting search status: {}'.format(err))
            raise

    def create_results_connection(self, search_id, offset, length):
        try:
            min_range = offset
            max_range = offset + length
            # Grab the response, extract the response code, and convert it to readable json
            response = self.api_client.get_search_results(search_id, min_range, max_range)
            response_code = response["code"]

            # Construct a response object
            return_obj = dict()
            if response_code == 200:
                return_obj['success'] = True
                return_obj['data'] = response['data']
            else:
                return_obj['success'] = False
                return_obj['error'] = response['message']
            return return_obj
        except Exception as err:
            print('error when getting search results: {}'.format(err))
            raise

    def delete_query_connection(self, search_id):
        try:
            response = self.api_client.delete_search(search_id)
            return response
        except Exception as err:
            print('error when deleting search {}:'.format(err))
            raise
