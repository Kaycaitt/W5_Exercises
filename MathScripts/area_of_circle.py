#Question: How do you calculate the area of a circle?

import math
pi = math.pi
radius = pow(5,2)
#I wrote pow in the order above because this takes the number 5 and squares it by itself)

area_of_circle = pi * radius

print("The area of a circle with radius " + str(radius) + " is " + str(format(area_of_circle, ".2f")))

