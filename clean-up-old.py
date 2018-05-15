#!/usr/bin/python
import requests, json, pprint, sys
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser

requests.packages.urllib3.disable_warnings()

# This script will delete projects that do not have any LUNS
# ie: we use this when we clean up after a failover

#HOST = 'https://10.2.0.195:215/'
HOST = 'https://10.2.0.191:215/'

# Get list of projects
headers = {"Content-Type": "application/json"}

url = HOST+'api/storage/v1/luns'
response = requests.get(url, headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
lunRef = json.loads(response.text)

url = HOST+'api/storage/v1/projects'
response = requests.get(url, headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
nodeRef = json.loads(response.text)

for project in nodeRef['projects']: 
    if project['name'] != 'default':
        LUNS=0
        # Check if projet has a LUN
        for lun in lunRef['luns']: 
            if lun['project'] == project['name']:
                LUNS=1
        if LUNS==1:
            print project['name'] + ' still has LUNS will not delete!'
        if LUNS==0:
            response = requests.delete(HOST+project['href'], headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
            if response.status_code != 204:
                print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))
            else:
                print 'Deleted project '+HOST+project['href'],response
            




# Delete ALL LUNS
#headers = {"Content-Type": "application/json"}
#url = HOST+'api/storage/v1/luns'
#response = requests.get(url, headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
#nodeRef = json.loads(response.text)
#for lun in nodeRef['luns']:   
#    print lun['project'] + ' still has a LUN: ' + lun['name']
    #response = requests.delete(HOST+lun['href'], headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
    #print 'Deleted LUN '+HOST+lun['href'],response



# Delete ALL Projects
#headers = {"Content-Type": "application/json"}
#url = HOST+'api/storage/v1/projects'
#response = requests.get(url, headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
#nodeRef = json.loads(response.text)
#for project in nodeRef['projects']: 
#    if project['name'] != 'default':
#        response = requests.delete(HOST+project['href'], headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
#        print 'Deleted project '+HOST+project['href'],response