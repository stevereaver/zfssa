#!/usr/bin/python
import requests, json, pprint, sys
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser


#Get replication target ID
requests.packages.urllib3.disable_warnings()
url = 'https://10.2.0.195:215/api/storage/v1/replication/targets'
response = requests.get(url, headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
nodeRef = json.loads(response.text)
# We assume only one target, which should always be the case in our environment
Target = nodeRef['targets'][0]['label']

# Grab list of LUNS

headers = {"Content-Type": "application/json"}
url = 'https://10.2.0.195:215/api/storage/v1/luns'
response = requests.get(url, headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)
nodeRef = json.loads(response.text)
for luns in nodeRef['luns']:

# Here we assume that the target pool is the same name as the source pool, emm bad!
    data = {
        "pool": luns['pool'],
        "project": luns['project'],
        "target_pool": luns['pool'],
        "target": Target,
        "continuous": "true"
        }

    print data

    url = 'https://10.2.0.195:215/api/storage/v1/replication/actions'
    headers = {'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw==', 'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers, verify=False)
    print response   