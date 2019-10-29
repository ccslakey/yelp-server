from requests import get
import ipdb
import pprint

pp = pprint.PrettyPrinter(indent=4)

BASE_URL = 'https://api.yelp.com/v3'
API_KEY = 'gAgK9ckcalJLnqKb8IUh2ivddoSJ4LVFD_7ULqszN4df479YxhN7_tMy8an2eZAYbsjqWIHoHXegopZ9s5ryenOBQXyffNUlUUHp4y0hcNsEbWXp8sKlkDPlChG2XXYx'

auth_headers = {
    "authorization": f'Bearer {API_KEY}'
}

def search_deliveries(lat = None, lon = None, location = '9237 Mapleview Way, Elk Grove CA 95758'):

    params = {}

    if (None in [lat, lon]):
        params["location"] = location
    else: 
        params["latitude"] = lat
        params["longitude"] = lon
    data = get(f'{BASE_URL}/transactions/delivery/search', headers=auth_headers, params=params)
    
    if (data.status_code <= 200 and data.status_code < 400):
        return data.json()

def get_business(id: int):
    #  https://api.yelp.com/v3/businesses/
    data = get(f'{BASE_URL}/businesses/{id}', headers=auth_headers)
    if (data.status_code <= 200 and data.status_code < 400):
        return data.json()

def get_reviews(id: int):
    data = get(f'{BASE_URL}/businesses/{id}/reviews', headers=auth_headers)
    if (data.status_code <= 200 and data.status_code < 400):
        return data.json()

# ipdb.set_trace()
# data = search_deliveries()
# pp.pprint(data)
# ipdb.set_trace()