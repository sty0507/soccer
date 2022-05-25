import http.client
import json
from numpy import mat

import pandas as pd

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token' : 'a5138360d35743f1961282ccb58f088f' }
connection.request('GET', '/v2/matches', None, headers )
response = json.loads(connection.getresponse().read().decode())
print (response)

key_matches = response.get('matches')

match_status = list(st['status'] for st in key_matches)
match_score = list(sc['score'] for sc in key_matches)
live_score = list(ls['fullTime'] for ls in match_score)
live_score_homeTeam = list(lsh['homeTeam'] for lsh in live_score)
live_score_awayTeam = list(lsh['awayTeam'] for lsh in live_score)

# for ms, lsh, lsa in zip(match_status, live_score_homeTeam,live_score_awayTeam):
#     if ms == 'IN_PLAY':
#         print()