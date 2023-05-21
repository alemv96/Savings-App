#CREATOR: Veloz
#DESCRIPTION: This will be an app that will 
#users to find best grocery deals around them. 
#they will be able to save money by just entering their zip code.
#from geopy.geocoders import Nominatim
import googlemaps
import time
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from config import API_KEY
import googlemaps.places as places


# Verify with Google so we can use my API-Key
map_client = googlemaps.Client(API_KEY)

# Initialize the geolocator object
geolocator = Nominatim(user_agent='my_savings_app')

# Get the zip code from the user
zipcode = input("Please enter your Zip Code: ")

# Find user's location using geolocator.
location = geolocator.geocode(f"{zipcode}, USA")

# Get the latitude and longitude for the parameters
latitude = location.latitude
longitude = location.longitude

# Get the distance from the user
distance = int(input("How many miles away would you like to see your deals? "))

# Define our search
places_result = map_client.places_nearby(location=f"{latitude},{longitude}", radius=distance, open_now=False, type='supermarket')

# Loop through each place in the result
for place in places_result['results']:

    # Defining my place ID
    my_place_id = place['place_id']

    # Defining what information I would like to gather
    my_fields = ['name', 'formatted_phone_number', 'type']

    # Make a request for the details
    place_details = places.place(client=map_client, place_id=my_place_id, fields=my_fields)

    # Print the name of the place
    print(place_details['result']['name'])

#print(places_result)

#to make sure it works we need to make sure the script is paused. 
#time.sleep(3)

#get the next 20 results.
#places_result = map_client.places_nearby(page_token = places_result['next_page_token'])

# Get the distance from the user.
#distance = input('Enter the distance in meters : ')
#
# Find the user's location using the geolocator object
#location = geolocator.geocode(f"{zipcode}, USA")

# Get the latitude and longitude of the user's location
#latitude = location.latitude
#longitude = location.longitude

# Specify what's the search query you would like to use:
#search_query = 'Grocery Store'

# Create a list of the businesses.
#business_list = []

 

#I found the error in the main program. My API is not working properly. 
# need to find a way to set it up correctly.