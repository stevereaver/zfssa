#!/usr/bin/python
import requests, json, pprint, sys
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser

requests.packages.urllib3.disable_warnings()

# NOTE: This needs to be run on the replica side, that is where the reversing is done.
# This will also set the replication to continuous

HOST = 'https://10.2.0.191:215/'

#Get source target ID
url = HOST+'api/storage/v1/replication/sources'
response = requests.get(url, headers={'Authorization': 'Basic xx'},verify=False)
nodeRef = json.loads(response.text)
# We assume only one source, which should always be the case in our environment
SOURCE = nodeRef['sources'][0]['name']

# Get a list of the replication packages
url = HOST+'api/storage/v1/replication/sources/' + SOURCE
response = requests.get(url, headers={'Authorization': 'Basic xx'},verify=False)
nodeRef = json.loads(response.text)
packages = nodeRef['source']['packages']

# Iterrate through the packages and reverse them
# Once again we assume only one source
for package in packages:
    
    #url = 'https://10.2.0.191:215' + package['href'] + '/reverse'
    #url = 'https://10.2.0.191:215' + package['href']
    #response = requests.get(url, headers={'Authorization': 'Basic xx'},verify=False)
    #nodeRef = json.loads(response.text)

    data= {'projname':package['project']}        
    url = HOST+'api/storage/v1/replication/sources/' + SOURCE + '/packages/' + package['id'] + '/reverse'
    #print url, data
    headers = {'Authorization': 'Basic xx', 'Content-Type': 'application/json'}
    response = requests.put(url, headers=headers,data=json.dumps(data),verify=False)
    print "Reversing Replication for " + package['project'], response
    if response.status_code != 202:
        print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))
        
# Set ALL replication actions to continuous
url = HOST+'api/storage/v1/replication/actions'
headers = {'Authorization': 'Basic xx'}
response = requests.get(url, headers=headers,verify=False)
nodeRef = json.loads(response.text)
for action in nodeRef['actions']:
    data= {'continuous':'true'}  
    url = HOST+action['href']
    response = requests.put(url, data=json.dumps(data), headers=headers, verify=False)
    print "Set continuous replication for " + action['project'], response
    if response.status_code != 202:
        print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))
