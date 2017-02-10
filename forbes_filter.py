"""Filter the Forbes billionaire list. Searches a JSON file
and return the youngest valid person and the oldest under 80.
"""

import json

def forbes_filter():
    """Return youngest person and oldest under 80."""
    with open('forbes_billionaires_2016.json') as data:
        moneybags = data.read()
        if moneybags[-3] == ',':
            moneybags = moneybags[:-3] + moneybags[-2:]
        moneybags = json.loads(moneybags)
        oldest_person = None
        oldest_age = 1
        youngest_person = None
        youngest_age = 80
        # import pdb; pdb.set_trace()
        for moneybag in moneybags:
            if moneybag['age'] < 80:
                if moneybag['age'] > oldest_age:
                    oldest_age = moneybag['age']
                    oldest_person = moneybag
                if moneybag['age'] < youngest_age and moneybag['age'] >0:
                    youngest_age = moneybag['age']
                    youngest_person = moneybag
        print("oldest under 80: " + oldest_person['name'])
        print(\t + "net worth: US$" + oldest_person["net_worth (USD)"])
        print(\t + "industry: " + oldest_person["source"])
        print("youngest: " + youngest_person['name'])
        print(\t + "net worth: US$" + youngest_person["net_worth (USD)"])
        print(\t + "industry: " + youngest_person["source"])