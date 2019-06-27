# 4.
# Write a program to find distance between two locations when their latitude and longitudes are given.
# Hint: Use math module.

import math

def geoCoordinates(inputMessage):
    location = [float(x) for x in input(inputMessage).split()]
    if (len(location) < 2):
        return None
    latitude = location[0]
    longitude = location[1]
    if (latitude < -180) or (latitude > 180):
        return None

    if (longitude < -90) or (longitude > 90):
        return None  
    return location

origin = geoCoordinates("Enter latitude and longitude for Origin: ")
destination = geoCoordinates("Enter latitude and longitude for Destination: ")
if (len(origin) == 2) and (len(destination) == 2):
    x1 = math.radians(origin[0])
    y1 = math.radians(origin[1])
    x2 = math.radians(destination[0])
    y2 = math.radians(destination[1])
    dist = 6371.01 * math.acos(math.sin(x1)*math.sin(x2) + math.cos(x1)*math.cos(x2)*math.cos(y1 - y2))
    print("The distance is %.2fkm." % dist)
else:
    print ("Wrong input")
