import requests
import os
from dotenv import load_dotenv

load_dotenv()


TOMTOM_API_KEY = os.getenv('TOMTOM_API_KEY')
HEREMAP_API_HEY = os.getenv('HEREMAP_API_HEY')


def get_human_readable_address( ):

        lat, lng = '41.85527', '-87.63752'
        nearby_url = 'https://api.tomtom.com/search/2/nearbySearch/.json'
        nearby_params = {
            'key': TOMTOM_API_KEY,
            'lat': lat,
            'lon': lng,
            'radius': '500',
            'limit': 50,
        }

        nearby_response = requests.get(nearby_url, params=nearby_params)
        nearby_response.raise_for_status()
        places = nearby_response.json()
        print( places)


        url = "https://revgeocode.search.hereapi.com/v1/revgeocode"
        params = {
            "at": f"{lat},{lng}",
            "lang": "en-US",  # Language for the response
            "apikey": HEREMAP_API_HEY
        }


        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        print(data)

if __name__ == "__main__":
    get_human_readable_address()