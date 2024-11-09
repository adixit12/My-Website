import requests
import json
from akamai.edgegrid import EdgeGridAuth, EdgeRc
#from urllib.parse import urljoin

edgerc = EdgeRc('.edgerc')
section = 'default'
baseurl = 'https://akab-xe3dt34aoi3hcmul-y3mjulo6d64sk6tb.luna.akamaiapis.net'

s = requests.Session()
s.auth = EdgeGridAuth(
    client_token=${{secrets.client_token}},
    client_secret=${{secrets.client_secret}},
    access_token=${{secrets.access_token}}
)

# ---------------------------

propertyId='prp_964439'

latest_version_of_property_url = baseurl + '/papi/v1/properties/'+propertyId
result = s.get(latest_version_of_property_url)

latestVersion = result.json()['properties']['items'][0]['latestVersion']

print(latestVersion)
