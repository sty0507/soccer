import http.client
import json
from threading import currentThread
import pandas as pd

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token' : 'a5138360d35743f1961282ccb58f088f' }

numlist = []

for i in range(1000):
    r = '/v4/persons/'
    r = r + str(i)
    connection.request('GET', r, None, headers)
    response = json.loads(connection.getresponse().read().decode())
    if "currentTeam" in response:
        numlist.append(i)

for j in range(len(numlist)):
    r = '/v4/persons/'
    r = r + str(numlist[j])
    connection.request('GET', r, None, headers)
    response = json.loads(connection.getresponse().read().decode())
    currentTeam = response.get('currentTeam')
    Teamname = currentTeam.get('name')
    if Teamname == "Manchester United FC":
        print(response.get('name'))
    else:
        continue
    