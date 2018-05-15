#!/usr/bin/python
import requests, json, pprint, sys
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser

requests.packages.urllib3.disable_warnings()

# A REALLY DANGEROUS SCRIPT TO DELETE ALL LUNS AND PROJECTS

HOSTS = ['https://10.2.0.191:215/','https://10.2.0.195:215/']

for HOST in HOSTS:

    # Delete ALL LUNS
    headers = {"Content-Type": "application/json"}
    url = HOST+'api/storage/v1/luns'
    response = requests.get(url, headers={'Authorization': 'Basic xx'},verify=False)
    nodeRef = json.loads(response.text)
    for lun in nodeRef['luns']:   
        response = requests.delete(HOST+lun['href'], headers={'Authorization': 'Basic xx'},verify=False)
        print 'Deleted LUN '+HOST+lun['href'],response

    # Delete ALL Projects
    headers = {"Content-Type": "application/json"}
    url = HOST+'api/storage/v1/projects'
    response = requests.get(url, headers={'Authorization': 'Basic xx'},verify=False)
    nodeRef = json.loads(response.text)
    for project in nodeRef['projects']: 
        if project['name'] != 'default':
            response = requests.delete(HOST+project['href'], headers={'Authorization': 'Basic xx'},verify=False)
            print 'Deleted project '+HOST+project['href'],response

    # Delete ALL Replication Packages if they exist
    # Get source target ID
    url = HOST+'api/storage/v1/replication/sources'
    response = requests.get(url, headers={'Authorization': 'Basic xx'},verify=False)
    nodeRef = json.loads(response.text)
    # We assume only one source, which should always be the case in our environment
    # Test if the string is empty, ie: do we really have a source
    if nodeRef['sources']:
        SOURCE = nodeRef['sources'][0]['name']
        headers = {"Content-Type": "application/json"}
        url = HOST+'api/storage/v1/replication/sources/' + SOURCE
        response = requests.get(url, headers={'Authorization': 'Basic xx'},verify=False)
        nodeRef = json.loads(response.text)
        for package in nodeRef['source']['packages']: 
            if package['project'] != 'default':
                url = HOST+package['href']
                response = requests.delete(url, headers={'Authorization': 'Basic xx'},verify=False)
                print 'Deleted replication package '+HOST+package['project'],response
