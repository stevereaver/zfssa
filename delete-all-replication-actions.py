#!/usr/bin/python
import requests, json, pprint, sys
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser

#
# Get a list of all LUNS


# Set up some variables

headers = {"Content-Type": "application/json"}
url = 'https://10.2.0.195:215/api/storage/v1/replication/actions'

#print url

# Authenticate and get JSON
requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)

#response = requests.get(url, auth=HTTPBasicAuth('admin', 'Wx&M4eEq'),verify=False)
#print response.text
#print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))

nodeRef = json.loads(response.text)

#print nodeRef
#print nodeRef['luns'][1]['canonical_name']


# Grab list of Replication Actions
for action in nodeRef['actions']:
    # Get the target ID and delete it
    aaa = url + '/' + action['id']
    print aaa
    # NOTE: The http request type here is DELETE
    response = requests.delete(aaa, headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
    print response
    
