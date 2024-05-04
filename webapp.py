#get your current location
import geocoder
from geopy.geocoders import ArcGIS
import openrouteservice as ors
from functools import reduce
import streamlit as st
import pandas as pd


client = ors.Client(key = '5b3ce3597851110001cf6248a1038de5c5304bb39fdff93c8db3113d')

def get_current_coordinates():
    g = geocoder.ip('me')
    return g.latlng

def dest_location(dest):
    nom = ArcGIS()
    dest_coord = list(nom.geocode(dest))
    dest_coord = list(dest_coord[1])
    return dest_coord

def swap(b = []):
    a = b[:]
    a[0], a[1] = a[1], a[0]
    return a

def finalroute(s, e):
    coords = [s, e]
    route = client.directions(coordinates = coords,
                             profile = 'driving-car',
                             format = 'geojson')
    final = []
    for coord in route['features'][0]['geometry']['coordinates']:
        final.append(coord)
    test = 1
    return route['features'][0]['geometry']['coordinates'], final, test
car_positions = {
    1: [77.5946, 12.9716],
    2: [77.5913, 12.9791],
    3: [77.6213, 12.9200],
    4: [77.6271, 12.9279],
    5: [77.7018, 12.9561],
    6: [77.630917, 13.026247],
    7: [77.6169, 12.9044],
    8: [77.6245, 12.9352],
    9: [77.5847, 12.9528],
    10: [77.65297, 13.029655],
    11: [77.748162, 12.899122],
    12: [77.781409, 12.856742],
    13: [77.725157, 12.767398],
    14: [72.878057, 21.204618],
    15: [77.717389, 13.256997]
}
start = get_current_coordinates()
#start = [12.895033, 77.675858]
#Front-End
st.title("Emergency Route Optimization using LoRAWAN")
st.subheader("Current Location")   
col1, col2 = st.columns(2)
col1.metric("Latitude", start[0]) 
col2.metric("Longitude", start[1])
destination = st.text_input("Enter your destination : ")
if(st.button("Look for vehicles")):
    start = get_current_coordinates()
    #start = [12.895033, 77.675858]
    start_s = swap(start)
    end = dest_location(destination)
    st.text("Destination Coordinates")
    col1, col2 = st.columns(2)
    col1.metric("Latitude", end[0]) 
    col2.metric("Longitude", end[1])
    end_s = swap(end)
    with st.spinner("Please wait"):
        direction, final, test = finalroute(start_s, end_s)
    if test == 1:
        st.success("Route Coordinates obtained")
        df = pd.DataFrame(final)
        st.dataframe(df)
    else:
        st.error("Optimal route not found")
    count = 0
    for coord in direction:
        for key, value in car_positions.items():
            if value==coord:
                count+=1
                st.text("Car ID " + str(key) + " found in the selected route")
                st.text("Car ID " + str(key) + " Location : ")
                col1, col2 = st.columns(2)
                value_s = swap(value)
                col1.metric("Latitude", value_s[0]) 
                col2.metric("Longitude", value_s[1])
                st.text("Send Alert Message")
    st.subheader(str(count) + " vehicles found in the route")