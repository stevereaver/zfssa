#!/usr/bin/python
import requests, json, pprint, sys
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser

requests.packages.urllib3.disable_warnings()

HOST = 'https://10.2.0.191:215/'

# Set ALL replication actions to continuous
url = HOST+'api/storage/v1/replication/actions'
print url
headers = {'Authorization': 'Basic xx'}
response = requests.get(url, headers=headers,verify=False)
nodeRef = json.loads(response.text)
#print nodeRef
for action in nodeRef['actions']:
    data= {'continuous':'true'}  
    url = HOST+action['href']
    print url
    response = requests.put(url, data=json.dumps(data), headers=headers, verify=False)
    print "Set continuous replication for " + action['project'], response
    if response.status_code != 202:
        print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))
