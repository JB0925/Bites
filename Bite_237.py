import requests

import json
from pathlib import Path
from datetime import datetime, date

SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
BELTS = ('white yellow orange green blue brown black '
         'paneled red').split()
scores_dict = dict(zip(SCORES, BELTS))

TMP = Path('/tmp')


url = 'https://bites-data.s3.us-east-2.amazonaws.com/bite_scores2.json'
response = requests.get(url).json()



def get_belts(data: str) -> dict:
    """Parsed the passed in json data:
       {"date":"5/1/2019","score":1},
       {"date":"9/13/2018","score":3},
       {"date":"10/25/2019","score":1},

       Loop through the scores in chronological order,
       determining when belts were achieved (use SCORES
       and BELTS).

       Return a dict with keys = belts, and values =
       readable dates, example entry:
       'yellow': 'January 25, 2018'
    """

    total_score = 0
    belts_dict = {}
    scores_already_passed = set()

    for d in data:
        d['date'] = datetime.strptime(d['date'],'%m/%d/%Y')
        d['date'] = date(d['date'].year, d['date'].month, d['date'].day)

    data = sorted(data, key=lambda x: x['date'])

    for d in data:
        d['date'] = datetime.strftime(d['date'],'%B %d, %Y')
        total_score += d['score']
        for score in SCORES:
            if total_score >= score and score not in scores_already_passed:
                scores_already_passed.add(score)
                belt = scores_dict.get(score)
                belts_dict[belt] = d['date']
    
    return belts_dict
                

    
    


print(get_belts(response))















