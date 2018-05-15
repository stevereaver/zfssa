#!/usr/bin/python
import requests, json, pprint, sys, urllib3, pprint
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()

# This function will itereate through each of the hosts and build and array
# that contains all the necessary information to do either a rebuild or
# a site failover (reverse replication)

def getenv(environment):
    ENV = []

    if environment=='HLO_TEST':
        PASSWORD = "xx"
        HOSTS=["ihlocs03","ihlocs23"]
    if environment=='HLO_PROD':
        PASSWORD = "xx"
        HOSTS=["ihlocs02","ihlocs22"]

    if environment=='FCL_TEST':
        PASSWORD = "xx"
        HOSTS=["iclyi11b","iclyi05b"]
    if environment=='FCL_PROD':
        PASSWORD = "xx"
        HOSTS=["iclyi10b","iclyi04b"]

    for host in HOSTS:
        print "Getting LUN info for host: "+host
        url = 'https://'+host+':215/api/storage/v1/pools'
        response = requests.get(url, headers={'Authorization': 'Basic '+PASSWORD},verify=False)
        nodeRef = json.loads(response.text)
        for pool in nodeRef['pools']:
            # Check if pool is online
            if pool['status']=="online":
                url = 'https://'+host+':215/api/storage/v1/pools/'+pool['name']+'/projects'
                response = requests.get(url, headers={'Authorization': 'Basic '+PASSWORD},verify=False)
                projRef = json.loads(response.text)
                for project in projRef['projects']:
                    url = 'https://'+host+':215'+project['href']+'/luns'
                    response = requests.get(url, headers={'Authorization': 'Basic '+PASSWORD},verify=False)
                    lunRef = json.loads(response.text)
                    for lun in lunRef['luns']:
                        # Loop thru replication actions
                            url = 'https://'+host+':215/api/storage/v1/replication/actions'
                            response = requests.get(url, headers={'Authorization': 'Basic '+PASSWORD},verify=False)
                            raRef = json.loads(response.text)
                            for action in raRef['actions']:
                                if action['pool'] == pool['name'] and action['project'] == project['name']:
                                    url = 'https://'+host+':215'+action['href']
                                    response = requests.get(url, headers={'Authorization': 'Basic '+PASSWORD},verify=False)
                                    actRef = json.loads(response.text)
                                    ENV.append({"HOST":host,"PROJECT":project['name'],"POOL":pool['name'],"LUN":lun['name'],"ENABLED":actRef['action']['enabled'],"CONTINUOUS":actRef['action']['continuous']})
    return ENV

    
#pprint (getenv("HLO_TEST"))
