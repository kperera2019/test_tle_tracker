from threading import Thread, Lock
import json
import httpx
from math import radians, sin, cos
from vpython import sphere, textures, rate, vector, color





URL = "http://127.0.0.1:8000/iss-stream"
latest_position = None
position_lock = Lock()
def listen_for_iss():
    global latest_position

    with httpx.stream("GET", URL, timeout=None) as response:
        response.raise_for_status()

        for line in response.iter_lines():
            if not line or not line.startswith("data:"):
                continue

            payload = json.loads(line.removeprefix("data:").strip())

            with position_lock:
                latest_position = payload


def lat_lon_to_xyz(latitude, longitude, radius=1.15):
    lat = radians(latitude)
    lon = radians(longitude)

    x = radius * cos(lat) * cos(lon)
    y = radius * sin(lat)
    z = -radius * cos(lat) * sin(lon)

    return vector(x, y, z)


Thread(target=listen_for_iss, daemon=True).start()


earth = sphere(pos=vector(0,0,0), radius=1, texture=textures.earth)
iss = sphere(pos=vector(0, 0, 0), radius=0.04, color=color.red)

#Rotation optional. for sake of clarity and ease of use, 
# earth.rotate(angle=radians(23.5), axis=vector(0,0,1))
while True:
    rate(60)

    with position_lock:
        position = latest_position #retain and set latest position to local variable for use outside of lock

    if position:
        iss.pos = lat_lon_to_xyz(position["latitude"], position["longitude"])

    #earth.rotate(angle=0.01, axis=vector(0, 1, 0))