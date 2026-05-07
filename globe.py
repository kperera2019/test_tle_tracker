from query import get_iss_position
from math import cos, sin, radians
payload = get_iss_position()
lat = payload["latitude"]
lon = payload["longitude"]

lat2rad= radians(lat)
lon2rad = radians(lon)

print(f"ISS is currently at lat: {lat}, lon: {lon}")

print("In globe space, we'd need to account for some basics.")

print("Assuming a globe with a radius of... what, 10 inches?")
r = 10

def lat_lon_xyz(lat, lon, r):
    lat2rad= radians(lat)
    lon2rad = radians(lon)
    x = r * cos(lat2rad) * cos(lon2rad)
    y = r * cos(lat2rad) * sin(lon2rad)
    z = r * sin(lat2rad)
    return x, y, z

print(f"Radius of the globe: {r} inches")
x, y, z = lat_lon_xyz(lat, lon, r)
print(f"ISS position in globe space: x={x:.2f}, y={y:.2f}, z={z:.2f}")