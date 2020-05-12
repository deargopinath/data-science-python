# 1. 
# A Robot moves in a Plane starting from the origin point (0	0). 
# The robot can move toward UP	 DOWN	 LEFT	 RIGHT.
#  
# The trace of Robot movement is as given following:
# UP 5 DOWN 3 LEFT 3 RIGHT 2 The numbers after directions are steps. 
# 
# Write a program to compute the distance current position after sequence of movements.
# Hint: Use math module.


import math

robo_x = 0
robo_y = 0

while True:
    movement = input("Specify robot's movement { UP | DOWN | LEFT | RIGHT  #steps} : ")
    if not movement:
        break
    steps = movement.split()
    if not (len(steps) == 2):
        print ("Wrong number of input arguments")
        continue
    direction = steps[0].upper()
    try:
        distance = int(steps[1])
        if (distance < 0):
            continue
        if (direction == "UP"):
            robo_y += distance
        elif (direction == "DOWN"):
            robo_y -= distance
        elif (direction == "RIGHT"):
            robo_x += distance
        elif (direction == "LEFT"):
            robo_x -= distance
    except:
        print("Exception: Wrong input value")

print("Net displacement = ", int(round(math.sqrt(robo_x**2 + robo_y**2))))
