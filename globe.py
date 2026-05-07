from vpython import sphere, textures, rate, vector
from math import radians

print("Rendering globe")

earth = sphere(pos=vector(0,0,0), radius=1, texture=textures.earth)
#Rotation optional. for sake of clarity and ease of use, 
# earth.rotate(angle=radians(23.5), axis=vector(0,0,1))
while True:
    rate(60)
    earth.rotate(angle=0.01, axis=vector(0,1,0))