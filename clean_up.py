#!/usr/bin/python
import requests, json, pprint, sys, urllib3
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

# This script will delete projects that do not have any LUNS
# ie: we use this when we clean up after a failover

HOST = sys.argv[1]
PASSWORD = open('.password','r').readline().replace('\n','')  

print '**     YOU ARE ABOUT TO DELETE PROJECTS ON '+HOST+'     **'
print '**  THIS SCRIPT WILL ONLY DELETE PROJECTS WITH NO LUNS  **'
answer=raw_input('** ARE YOU CERTAIN YOU WANT TO DO THIS ? (Type: yesiam) **\n')
if answer != "yesiam":
        quit()

# Get list of projects
headers = {"Content-Type": "application/json"}

url = 'https://'+HOST+':215/api/storage/v1/luns'
response = requests.get(url, headers={'Authorization': 'Basic '+PASSWORD},verify=False)
if response.status_code != 200:
        print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))
        quit()
lunRef = json.loads(response.text)

url = 'https://'+HOST+':215/api/storage/v1/projects'
response = requests.get(url, headers={'Authorization': 'Basic '+PASSWORD},verify=False)
if response.status_code != 200:
        print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))
        quit()
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
            response = requests.delete('https://'+HOST+':215'+project['href'], headers={'Authorization': 'Basic '+PASSWORD},verify=False)
            if response.status_code != 204:
                print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))
            else:
                print 'Deleted project '+HOST+project['href'],response