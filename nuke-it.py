#!/usr/bin/python
import requests, json, pprint, sys
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser

requests.packages.urllib3.disable_warnings()

# A REALLY DANGEROUS SCRIPT TO DELETE ALL LUNS AND PROJECTS

HOST = 'https://10.2.0.195:215/'
#HOST = 'https://10.2.0.191:215/'

# Delete ALL LUNS
headers = {"Content-Type": "application/json"}
url = HOST+'api/storage/v1/luns'
response = requests.get(url, headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
nodeRef = json.loads(response.text)
for lun in nodeRef['luns']:   
    response = requests.delete(HOST+lun['href'], headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
    print 'Deleted LUN '+HOST+lun['href'],response

# Delete ALL Projects
headers = {"Content-Type": "application/json"}
url = HOST+'api/storage/v1/projects'
response = requests.get(url, headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
nodeRef = json.loads(response.text)
for project in nodeRef['projects']: 
    if project['name'] != 'default':
        response = requests.delete(HOST+project['href'], headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
        print 'Deleted project '+HOST+project['href'],response