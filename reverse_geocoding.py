import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()


TOMTOM_API_KEY = os.getenv('TOMTOM_API_KEY')
HEREMAP_API_HEY = os.getenv('HEREMAP_API_HEY')


def get_human_readable_address( ):

        lat, lng = '41.85527', '-87.63752'
        lat, lng = '31.5204', '74.3587'
        # lat, lng = '34.052235', '-118.243683'
        # lat, lng = '29.760427', '-95.369804'
        nearby_url = 'https://api.tomtom.com/search/2/nearbySearch/.json'
        nearby_params = {
            'key': TOMTOM_API_KEY,
            'lat': lat,
            'lon': lng,
            'radius': '500',
            'limit': 1,
        }

        nearby_response = requests.get(nearby_url, params=nearby_params)
        nearby_response.raise_for_status()
        places = nearby_response.json()

        with open("tomtom_result.json", "w") as file:
            json.dump(places, file, indent=4)
        print( places)


        url = "https://revgeocode.search.hereapi.com/v1/revgeocode"
        params = {
            "at": f"{lat},{lng}",
            "lang": "en-US",  # Language for the response
            "apikey": HEREMAP_API_HEY,
            "mode":'retrieveAddresses'
        }


        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
      

        if data.get("items"):
                address = data["items"][0].get("address", {})
                city = address.get("city", "")
                state = address.get("state", "")

                # Build the location string
                if city and state:
                    location = f"{city}, {state}"
                elif city:
                    location = city
                elif state:
                    location = state
                else:
                    location = "Location not found"

                
                print(f"Lat/Lng: {lat},{lng} => Location: {location}")
        else:
            print(f"Lat/Lng: {lat},{lng} => No address found.")
            


       
        with open("here_result.json", "w") as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
    get_human_readable_address()