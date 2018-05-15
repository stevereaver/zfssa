#!/usr/bin/python
import requests, json, pprint, sys, urllib3, pprint, environment
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser

# Disable SSL warnings
requests.packages.urllib3.disable_warnings()

HOST_PR="10.2.0.195"
HOST_DR="10.2.0.191"

#ENV=environment.getenv('HLO_PROD')
#ENV=environment.getenv('HLO_TEST')
ENV=environment.getenv('FCL_PROD')
#ENV=environment.getenv('FCL_TEST')

#pprint(ENV)
#quit()

for PROJ in ENV:
    HOST=PROJ["HOST"]
    # oh god this is dodgy, but we need a way to translate what is in production to the test environment
    if HOST=="ihlocs02":
        HOST=HOST_PR
    if HOST=="ihlocs03":
        HOST=HOST_PR
    if HOST=="ihlocs22":
        HOST=HOST_DR
    if HOST=="ihlocs23":
        HOST=HOST_DR
    if HOST=="iclyi10b":
        HOST=HOST_PR
    if HOST=="iclyi11b":
        HOST=HOST_PR
    if HOST=="iclyi04b":
        HOST=HOST_DR
    if HOST=="iclyi05b":
        HOST=HOST_DR
    PROJECT=PROJ["PROJECT"]
    LUN=PROJ["LUN"]
    # Because we are rebuilding in sandbox the pools are always called VM-MIRROR
    #POOL=PROJ["POOL"]
    POOL="VM-MIRROR"

    # Get replication target ID, this needs to be already setup in the BUI
    url = 'https://'+HOST+':215/api/storage/v1/replication/targets'
    response = requests.get(url, headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
    nodeRef = json.loads(response.text)
    # We assume only one target, which should always be the case in our environment
    TARGET = nodeRef['targets'][0]['label']

    # Create the projects and LUNS
    data = { 'name':PROJECT }
    headers = {'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw==', 'Content-Type': 'application/json'}
    url = 'https://'+HOST+':215/api/storage/v1/pools/'+POOL+'/projects'
    response = requests.post(url,headers=headers,data=json.dumps(data),verify=False)
    print 'Created '+PROJECT+' on '+POOL, response
    if response.status_code != 201:
        print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))

    # Create LUNS while we are here
    data = { 
        'name':LUN,
        'volsize':500*1024*1024
    }
    url = 'https://'+HOST+':215/api/storage/v1/pools/'+POOL+'/projects/'+PROJECT+'/luns'
    response = requests.post(url,headers=headers,data=json.dumps(data),verify=False)
    #print json.loads(response.text)
    print 'Created '+LUN+' in project '+PROJECT, response
    if response.status_code != 201:
        print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))

    # Yeah why not... set up the replication scheduale
    if PROJ['ENABLED'] == True:
        data = {
            "pool": POOL,
            "project": PROJ['PROJECT'],
            "target_pool": POOL,
            "target": TARGET,
            "continuous": PROJ['CONTINUOUS']
        }
        url = 'https://'+HOST+':215/api/storage/v1/replication/actions'
        response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
        nodeRef = json.loads(response.text)
        print 'Created replication action for '+PROJECT, response
        if response.status_code != 201:
            print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))
        href = nodeRef['action']['href']
        # Now we set a scheduale using the href to refer to the scheduale we just created
        if PROJ['CONTINUOUS'] == False:
            data = {"frequency": "5min"}
            url = 'https://'+HOST+':215'+href+'/schedules'
            #print url
            response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
            print 'Set replication scheduale for '+PROJECT, response