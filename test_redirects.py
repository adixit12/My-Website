import requests
import json
from akamai.edgegrid import EdgeGridAuth, EdgeRc
#from urllib.parse import urljoin

edgerc = EdgeRc('.edgerc')
section = 'default'
baseurl = 'https://%s' % edgerc.get(section, 'host')

s = requests.Session()
s.auth = EdgeGridAuth.from_edgerc(edgerc, section)

# ---------------------------

propertyId='prp_964439'

latest_version_of_property_url = baseurl + '/papi/v1/properties/'+propertyId
result = s.get(latest_version_of_property_url)

latestVersion = result.json()['properties']['items'][0]['latestVersion']

print(latestVersion)
