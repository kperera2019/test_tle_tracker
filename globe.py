from query import get_iss_position
from math import cos, sin, radians
import time
def lat_lon_xyz(lat, lon, r):
    lat2rad= radians(lat)
    lon2rad = radians(lon)
    x = r * cos(lat2rad) * cos(lon2rad)
    y = r * cos(lat2rad) * sin(lon2rad)
    z = r * sin(lat2rad)
    return x, y, z

def main():
    payloads=[]
    while True:
        payload = get_iss_position()
       
        payloads.append(payload)

        print(f"Current time: {time.ctime().split()[3]} LOCAL - ISS position query:")
        lat = payload["latitude"]
        lon = payload["longitude"]
        vel = payload["velocity"]
        timestamp= payload["timestamp"]

        print(f"ISS is currently at lat: {lat}, lon: {lon} moving at a speed of {vel} km/h")


        if(len(payloads) > 1):
            print("Previous position:")
            prev = payloads[-2]
            print(f"lat: {prev['latitude']}, lon: {prev['longitude']}")
            print(f"Velocity: {prev['velocity']} km/h")
            dlon = radians(lon - prev['longitude'])
            dlat = radians(lat - prev['latitude'])
            dt = timestamp - prev['timestamp']
            print(f"Change in position: dlat={dlat:.4f} rad, dlon={dlon:.4f} rad, dt={dt} seconds")
        else:
            print("No previous position data available.")


        print("In globe space, we'd need to account for some basics.")

        print("Assuming a globe with a radius of... what, 10 inches?")
        r = 10

        print(f"Radius of the globe: {r} inches")
        x, y, z = lat_lon_xyz(lat, lon, r)
        print(f"ISS position in globe space: x={x:.2f}, y={y:.2f}, z={z:.2f}")
        time.sleep(10)


if __name__ == "__main__":
    main()