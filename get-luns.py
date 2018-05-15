#!/usr/bin/python
import requests, json, pprint, sys
import urllib3
from requests.auth import HTTPBasicAuth
from pprint import pprint
from optparse import OptionParser

#
# Get a list of all LUNS
# root:G0d_4c7_      BASE64 =  cm9vdDpHMGRfNGM3Xw==

# Set up some variables

headers = {"Content-Type": "application/json"}
url = 'https://10.2.0.195:215//api/storage/v1/luns'
#url = 'https://10.2.0.191:215//api/storage/v1/luns'

#print url

# Authenticate and get JSON
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers={'Authorization': 'Basic cm9vdDpHMGRfNGM3Xw=='},verify=False)

#response = requests.get(url, auth=HTTPBasicAuth('admin', 'Wx&M4eEq'),verify=False)
#print response.text
#print json.dumps (response.json(), sort_keys=True, indent=4, separators=(',', ': '))

nodeRef = json.loads(response.text)
#print nodeRef

#print nodeRef['luns'][1]['canonical_name']


# Grab list of luns
for lun in nodeRef['luns']:
    print lun['canonical_name'] + ' ' + lun['lunguid']
    



#    url = 'https://'+LoadBalancer+':9070/api/tm/5.1/config/active/pools/'+PoolName['name']
#    poolRef = get_json(url)    
#    for NodeName in poolRef['properties']['basic']['nodes_table']:
#        print NodeName['node']+","+NodeName['state']

