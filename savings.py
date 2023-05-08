#CREATOR: Veloz
#DESCRIPTION: This will be an app that will 
#users to find best grocery deals around them. 
#they will be able to save money by just entering their zip code.
from geopy.geocoders import Nominatim
import requests
from bs4 import BeautifulSoup
from config import API_KEY

# Initialize the geolocator object
geolocator = Nominatim(user_agent='my_app')

# Get the zip code from the user
zipcode = input("Please enter your Zip Code: ")

# Get the distance from the user
distance = int(input("How many miles away would you like to see your deals?"))

# Find the user's location using the geolocator object
location = geolocator.geocode(f"{zipcode}, USA")

# Print the user's location
print("It looks like your location is:", location.address)

# Get the latitude and longitude of the user's location
latitude = location.latitude
longitude = location.longitude

# Find grocery stores near the user's location
grocery_stores = []
search_query = "Supermarket"
url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={latitude},{longitude}&radius={distance}&type={search_query}&key={API_KEY}"
#print("FLAG 1")
response = requests.get(url)
#print("FLAG 2")
if response.status_code == 200:
    #print("FLAG 3")
    results = response.json()["results"]
    #print("FLAG 4")
    for search_result in results:
    #    print("FLAG 5")
        grocery_stores.append(search_result["name"])
    #    print("FLAG 6")
else:
    print("Your search was not possible...")

# Debugging step to check the grocery stores list
#print(grocery_stores)
print(grocery_stores)
# Scrape pricing data from grocery stores for specific items
print("FLAG 7")
#grocery_items = ["apples", "bread", "milk", "chocolate"]
#grocery_data = {}
#for store in grocery_stores:
 #  grocery_data[store] = {}
 #   for item in grocery_items:
#        #url = f"https://www.{store}.com/search?q={item}" #this URL is giving me an error. NEED TO FIX
#        print(f"{store} and {item}")#Store is getting "Cedar Bluff" which is a location not a store. 
#        response = requests.get(url)
#        if response.status_code == 200:
#            soup = BeautifulSoup(response.text, "html.parser")
#            if soup.find("span", class_="price") is not None:
#                price = soup.find("span", class_="price").text
#                grocery_data[store][item] = price
#            else:
#                print(f"{item} not found at {store}")
#        else:
#            print(f"Unable to retrieve data for {store} - {item}")
#
# Find the best deals for each item
#deals = {}
#for item in grocery_items:
#    best_price = float("inf")
#    best_store = ""
#    for store, data in grocery_data.items():
#        if item in data and float(data[item]) < best_price:
#            best_price = float(data[item])
#            best_store = store
#    if best_store:
#        deals[item] = (best_store, best_price)
# Print out the best deals for each item
#for item, (store, price) in deals.items():
#    print(f"The best deal for {item} is at {store} for ${price:.2f}")
#
