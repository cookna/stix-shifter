import argparse
import sys
from stix_shifter.stix_translation import stix_translation
from stix_shifter.stix_transmission import stix_transmission
from flask import Flask, request
from stix_shifter.utils.error_response import ErrorResponder
import json
import time
import requests,json
from stix_shifter.stix_transmission.src.modules.cloudIdentity import CloudIdentity_Token, CloudIdentity_Request
#from stix_shifter.stix_transmission.src.modules.cloudIdentity import CloudIdentity_Request
def main2():

    token = CloudIdentity_Token.getToken()
    CloudIdentity_Request.getAuthenticationTrail(token, "now-240h", "now", 10, "time", "asc")
    #print(token)

main2()