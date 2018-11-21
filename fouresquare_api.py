import json
import requests


""" 
This module uses Foursquare api to find restaurant data to return the top 3 addresses
to food stores within a specified location
"""


def find_restaurant(food_type, location):
    # retrieves the data from the foursquare api and takes in 2 parameters the type of food
    # you want and the the location you would like to eat at
    url = 'https://api.foursquare.com/v2/venues/search'
    params = dict(
        client_id='{YOUR CLIENT ID}',
        client_secret='{YOUR CLIENT SECRET}',
        v='20180323',
        # ll='40.7243,-74.0018', you can use coordinates if you don't use near param
        near=location,
        query=food_type,
        limit=5
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    return data


def display_store(level):
    # displays the addresses. The level param chooses the restaurant from the query
    data = find_restaurant('pizza', 'San Diego, California')
    store_name = data['response']['venues'][level]['name']
    store_street = data['response']['venues'][level]['location']['formattedAddress'][0]
    store_city = data['response']['venues'][level]['location']['formattedAddress'][1]

    stores = [store_name, store_street, store_city]

    for store in stores:
      print(store)


if __name__ == '__main__':

    for i in range(3):
        display_store(i)
        print('\n')

