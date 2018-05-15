#!/usr/bin/python
import requests, json, pprint, sys
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser

headers = {"Content-Type": "application/json"}
url = 'https://10.2.0.195:215/api/storage/v1/replication/actions'
#url = 'https://10.2.0.191:215/api/storage/v1/replication/actions'

requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
nodeRef = json.loads(response.text)

# Grab list of luns
for action in nodeRef['actions']:
    print action['replication_of'] + '\t' + action['last_sync'] + '\t' + action['last_result'] + '\t' + action['id']