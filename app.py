from flask import Flask
from requests import get
import ipdb
import pprint

pp = pprint.PrettyPrinter(indent=4)
app = Flask('__main__')


API_URL = 'https://api.yelp.com/v3/transactions/delivery/search'
API_KEY = 'gAgK9ckcalJLnqKb8IUh2ivddoSJ4LVFD_7ULqszN4df479YxhN7_tMy8an2eZAYbsjqWIHoHXegopZ9s5ryenOBQXyffNUlUUHp4y0hcNsEbWXp8sKlkDPlChG2XXYx'

def search_deliveries(lat = None, lon = None, location = '9237 Mapleview Way, Elk Grove CA 95758'):

    headers = {
        "authorization": f'Bearer {API_KEY}'
    }

    params = {}

    if (None in [lat, lon]):
        params["location"] = location
    else: 
        params["latitude"] = lat
        params["longitude"] = lon
    data = get(API_URL, headers=headers, params=params)
    
    if (data.status_code <= 200 and data.status_code < 400):
        return data.json()



ipdb.set_trace()
data = search_deliveries()
pp.pprint(data)
ipdb.set_trace()