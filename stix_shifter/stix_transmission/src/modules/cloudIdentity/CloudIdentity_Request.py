from ..utils.RestApiClient import RestApiClient
import requests, json
from . import util
from . import CloudIdentity_Token

def authUser(id, pwd, token):
    body = {
        "username": id,
        "password": pwd
    }
    print(token)
    url = util.getUri()+"/v1.0/authnmethods/password/"+util.getRegistry()
    options = {
        'uri': util.getUri()+"/v1.0/authnmethods/password/"+util.getRegistry(),
        'method': "POST",
        'json': 'true',
        'headers': { "Accept": "application/json", "Content-Type": "application/json", "authorization": "Bearer "+token},
        'body': body
    }
    

    resp = requests.post(url, json=options)
    if resp != 200:
        #refreshing token and try again
        authUser(id, pwd, CloudIdentity_Token.getToken())
    print(resp)


def getUsers(token):
    url = util.getUri()+"/v2.0/Users"

    headers = { "Accept": "application/json, text/plain, */*","authorization": "Bearer "+token}
    resp = requests.get(url, headers=headers)

    #print(json.loads(resp.text))
    json_data = resp.json()
    print(json_data)
#Last time user name logged in
