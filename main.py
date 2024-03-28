import geocoder
import requests

g = geocoder.ip('me')
#print(g.latlng)

def get_route(api_key, coordinates):
    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    headers = {"Authorization": f"YourApiKey {api_key}"}
    params = {
        "coordinates": coordinates,
        "geometry": "true",
        "instructions": "true"
    }
    
    response = requests.post(url, json=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None

# Example usage
api_key = '5b3ce3597851110001cf6248a1038de5c5304bb39fdff93c8db3113d'
coordinates = [[8.34234,48.23424],[8.34423,48.26424]]  # Example coordinates
route_data = get_route(api_key, coordinates)
print(route_data)
