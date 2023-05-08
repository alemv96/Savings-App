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
#print("FLAG 8")
#grocery_data = {}
#print("FLAG 9")
#for store in grocery_stores:
 #  print("FLAG 10")
 #  grocery_data[store] = {}
 #  print("FLAG 11")
#    for item in grocery_items:
#        print("FLAG 12")
#        #url = f"https://www.{store}.com/search?q={item}" #this URL is giving me an error. NEED TO FIX
#       print(f"{store} and {item}")#Store is getting "Cedar Bluff" and that is why I am getting an error.
#        print("FLAG 13")
#        response = requests.get(url)
#        print("FLAG 14")
#        if response.status_code == 200:
#            print("FLAG 15")
#            soup = BeautifulSoup(response.text, "html.parser")
#            print("FLAG 16")
#            if soup.find("span", class_="price") is not None:
#                print("FLAG 17")
#                price = soup.find("span", class_="price").text
#                print("FLAG 18")
#                grocery_data[store][item] = price
#                print("FLAG 19")
#            else:
#                print(f"{item} not found at {store}")
#        else:
#            print("FLAG 20")
#            print(f"Unable to retrieve data for {store} - {item}")
#            print("FLAG 21")

# Find the best deals for each item
#print("FLAG 22")
#deals = {}
#print("FLAG 23")
#for item in grocery_items:
#    print("FLAG 24")
#    best_price = float("inf")
#    print("FLAG 24")
#    best_store = ""
#    print("FLAG 25")
#    for store, data in grocery_data.items():
#        print("FLAG 26")
#        if item in data and float(data[item]) < best_price:
#            print("FLAG 27")
#            best_price = float(data[item])
#            print("FLAG 28")
#            best_store = store
#            print("FLAG 29")
#    if best_store:
#        print("FLAG 30")
#        deals[item] = (best_store, best_price)
#        print("FLAG 31")
# Print out the best deals for each item
#print("FLAG 32")
#for item, (store, price) in deals.items():
#    print("FLAG 33")
#    print(f"The best deal for {item} is at {store} for ${price:.2f}")
#    print("FLAG 34")