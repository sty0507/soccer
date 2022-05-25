from flask import Flask, render_template
import requests
import http.client
import json
import pandas as pd

app = Flask(__name__)

connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token' : 'a5138360d35743f1961282ccb58f088f' }
connection.request('GET', '/v2/matches', None, headers )
response = json.loads(connection.getresponse().read().decode())


key_matches = response.get('matches')
competition = list(c['competition'] for c in key_matches)
competition_name = list(c['name'] for c in competition)
homeTeam = list(km['homeTeam'] for km in key_matches)
homeTeam_name = list(ht['name'] for ht in homeTeam)
awayTeam = list(km['awayTeam'] for km in key_matches)
awayTeam_name = list(at['name'] for at in awayTeam)
match_status = list(st['status'] for st in key_matches)
match_score = list(sc['score'] for sc in key_matches)
live_score = list(ls['fullTime'] for ls in match_score)
live_score_homeTeam = list(lsh['homeTeam'] for lsh in live_score)
live_score_awayTeam = list(lsh['awayTeam'] for lsh in live_score)



@app.route("/",methods=['GET','POST'])
def show():

    # return render_template('index.html', homeTeam_name=homeTeam_name, awayTeam_name=awayTeam_name, competition_name=competition_name, match_status=match_status, live_score_homeTeam=live_score_homeTeam,live_score_awayTeam=live_score_awayTeam)
    for hn, an, cn, ms, lsh, lsa in zip(homeTeam_name, awayTeam_name, competition_name, match_status, live_score_homeTeam,live_score_awayTeam):
        if ms == 'SCHEDULED':
            team_str = "{} VS {} [{}]".format(hn, an,cn)
            score_str = "live score : Scheduled"
            return render_template('index.html', team = team_str, score = score_str)
        else:
            team_str = "{} VS {} [{}]".format(hn, an,cn)
            score_str = "live score[{}]  {} : {}".format(ms, lsh,lsa)
            return render_template('index.html', team = team_str, score = score_str)


if __name__ == "__main__":
    app.run(debug=True)

