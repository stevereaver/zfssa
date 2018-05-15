#!/usr/bin/python
import requests, json, pprint, sys, urllib3, time
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

# This script is run on the replica side, that is where the reversing is done.
# Add relication packages you want left alone in this variable
PREVENT = [ "fs_vhlocs03_backup","zn_ihlocs22_vhlocs20","zn_ihlocs05_vhlocs00"
            "zn_iclys00_aclys09","zn_iclys06_aclys08","fs_aclys03_avail_cache"]
            
HOST = sys.argv[1]

# Host is primary side
if HOST == '10.2.0.191':
    HOST_PR = '10.2.0.195'
    HOST_DR = '10.2.0.191'
    SOURCE = 'zfssa-00a'

# Host is Secondary side
if HOST == '10.2.0.195':
    HOST_PR = '10.2.0.191'
    HOST_DR = '10.2.0.195'
    SOURCE = 'zfssa-01a'

print '**         YOU ARE ABOUT TO REVERSE PRELICATION ON ON '+HOST_DR+'        **'
print '**  THIS CANNOT BE UNDONE, ENSURE YOU HAVE SET THE "PREVENT" VARIABLE   **'
answer=raw_input('**         ARE YOU CERTAIN YOU WANT TO DO THIS ? (Type: yesiam)         **\n')
if answer != "yesiam":
        quit()

# Start by sending updates from source first
# and wait for the update to finish
url = 'https://'+HOST_DR+':215/api/storage/v1/replication/actions'
response = requests.get(url, headers={'Authorization': 'Basic xx'},verify=False)
nodeRef = json.loads(response.text)
for action in nodeRef['actions']:
    url = 'https://'+HOST_DR+':215/api/storage/v1/replication/actions'+action['id']+'/sendupdate'
    response = requests.put(url, headers={'Authorization': 'Basic xx'},verify=False)
    print 'Sent replication update for '+action['replication_of']
    # If Replication action is scheduled wait for it to finish
    if action['continuous']==0:
        url = 'https://'+HOST_DR+':215/'+action['href']
        response = requests.get(url, headers={'Authorization': 'Basic xx'},verify=False)
        nodeRef2 = json.loads(response.text)
        #print nodeRef2
        action2=nodeRef2['action']
        while action2['state'] != 'idle':
            print 'Replication state is "'+action2['state']+'" waiting....'
            time.sleep(2)
            url = 'https://'+HOST_DR+':215/'+action['href']
            response = requests.get(url, headers={'Authorization': 'Basic xx'},verify=False)
        print 'Replication state is '+action2['state']+' continuing'
    else:
        print 'Replication action is continuous'

#Get source target ID
#url = 'https://'+HOST_DR+':215/api/storage/v1/replication/sources'
#response = requests.get(url, headers={'Authorization': 'Basic xx'},verify=False)
#nodeRef = json.loads(response.text)
# We assume only one source, which should always be the case in our environment
#SOURCE = nodeRef['sources'][0]['name']

# Get a list of the replication packages
url = 'https://'+HOST_DR+':215/api/storage/v1/replication/sources/' + SOURCE
#print url
response = requests.get(url, headers={'Authorization': 'Basic xx'},verify=False)
nodeRef = json.loads(response.text)
#print nodeRef
packages = nodeRef['source']['packages']


# Iterrate through the packages and reverse them
# except for those in the PREVENT array
for package in packages:
    replica_of = package['project']
    if not replica_of in PREVENT:
        data= {'projname':package['project']}        
        # Reverse it!
        url = 'https://'+HOST_DR+':215/api/storage/v1/replication/sources/' + SOURCE + '/packages/' + package['id'] + '/reverse'
        #print url, data
        headers = {'Authorization': 'Basic xx', 'Content-Type': 'application/json'}
        response = requests.put(url, headers=headers,data=json.dumps(data),verify=False)
        print "Reversing Replication for " + package['project'], response
        if response.status_code != 202:
           print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))
    else:
        print "Skipping "+ replica_of

# Enable ALL replication actions to continuous
url = 'https://'+HOST_DR+':215/api/storage/v1/replication/actions'
headers = {'Authorization': 'Basic xx'}
response = requests.get(url, headers=headers,verify=False)
nodeRef = json.loads(response.text)
for action in nodeRef['actions']:
    data = {'continuous':'true'}  
    url = 'https://'+HOST_DR+':215/'+action['href']
    response = requests.put(url, data=json.dumps(data), headers=headers, verify=False)
    print "Set continuous replication for " + action['project'], response
    if response.status_code != 202:
        print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))
