#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Getting Map Coordinates 
# importing geopy library
from geopy.geocoders import Nominatim

# calling the Nominatim tool
loc = Nominatim(user_agent="AREKAL")

# entering the location name
getLoc = loc.geocode("ADONI")

# printing address
print(getLoc.address)

# printing latitude and longitude
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)


# In[21]:


#Google Place Locator
from geopy.geocoders import Nominatim
import folium

def get_coordinates(place_name):
    geolocator = Nominatim(user_agent="place_locator")
    location = geolocator.geocode(place_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None

def show_place_on_map(place_name):
    coordinates = get_coordinates(place_name)

    if coordinates:
        # Create a folium map centered around the coordinates
        map_location = folium.Map(location=coordinates, zoom_start=15)

        # Add a marker for the specified place
        folium.Marker(location=coordinates, popup=place_name).add_to(map_location)

        # Save the map as an HTML file and open it in the default web browser
        map_location.save("map_location.html")
        import webbrowser
        webbrowser.open("map_location.html")

    else:
        print(f"Could not find coordinates for {place_name}")

if __name__ == "__main__":
    user_input = input("Enter the place name: ")
    show_place_on_map(user_input)


# In[27]:


#Generating Coordinates 
from geopy.geocoders import Nominatim

def get_coordinates(place_name):
    geolocator = Nominatim(user_agent="your_app_name")
    location = geolocator.geocode(place_name)

    if location:
        return location.latitude, location.longitude
    else:
        print(f"Coordinates not found for {place_name}")
        return None

# Example usage
user_input_place = input("Enter a place name: ")
coordinates = get_coordinates(user_input_place)

if coordinates:
    print(f"Coordinates for {user_input_place}: Latitude {coordinates[0]}, Longitude {coordinates[1]}")


# In[35]:


#Generating place name using coordinates
import folium
from geopy.geocoders import Nominatim

def generate_map_and_place_name(latitude, longitude):
    # Convert coordinates to human-readable address
    geolocator = Nominatim(user_agent="map_generator")
    location = geolocator.reverse((latitude, longitude), language='en')
    address = location.address if location else "Address not found"

    # Generate map centered at the given coordinates
    map_center = [latitude, longitude]
    my_map = folium.Map(location=map_center, zoom_start=15)

    # Add a marker with a popup displaying the address
    folium.Marker(location=map_center, popup=folium.Popup(address, parse_html=True)).add_to(my_map)

    # Save the map to an HTML file or display it
    map_filename = "generated_map.html"
    my_map.save(map_filename)
    print(f"Map generated successfully. Address: {address}")
    print(f"Map saved to {map_filename}")

if __name__ == "__main__":
    # Example coordinates (you can replace these with user input)
    user_latitude = float(input("Enter latitude:"))
    user_longitude = float(input("Enter longitue:"))

    generate_map_and_place_name(user_latitude, user_longitude)


# In[41]:


#ISS Present Coordinates
import requests
from datetime import datetime

def get_iss_location():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        data = response.json()
        iss_location = data['iss_position']
        latitude = float(iss_location['latitude'])
        longitude = float(iss_location['longitude'])
        return latitude, longitude
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_iss_pass_times(latitude, longitude, num_passes=5):
    try:
        response = requests.get(f"http://api.open-notify.org/iss-pass.json?lat={latitude}&lon={longitude}&n={num_passes}")
        data = response.json()
        pass_times = data['response']
        return pass_times
    except Exception as e:
        print(f"Error: {e}")
        return None

# Get the current ISS location
current_location = get_iss_location()
if current_location:
    print(f"Current ISS Location: Latitude {current_location[0]}, Longitude {current_location[1]}")

# Example: Get upcoming ISS pass times for New York City
latitude_nyc, longitude_nyc = 40.7128, -74.0060
pass_times_nyc = get_iss_pass_times(latitude_nyc, longitude_nyc)

if pass_times_nyc:
    print("\nUpcoming ISS Pass Times for New York City:")
    for pass_info in pass_times_nyc:
        risetime_unix = pass_info['risetime']
        risetime_utc = datetime.utcfromtimestamp(risetime_unix)
        duration_seconds = pass_info['duration']
        print(f"Rise Time (UTC): {risetime_utc}, Duration: {duration_seconds} seconds")


# In[ ]:




