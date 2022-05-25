import http.client
import json

import pandas as pd

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token' : 'a5138360d35743f1961282ccb58f088f' }
connection.request('GET', '/v2/matches', None, headers )
response = json.loads(connection.getresponse().read().decode())
print (response)