#Question: Choose an above exercise and rewrite the print output as an f-string. I am choosing distance.py

#Question: How do you calculate the distance between coordinates (x1,y1) and (x2,y2)?

import math

x2 = 300
x1 = 90
y2 = 700
y1 = 200

distance_y = y2 - y1
distance_x = x2 - x1
#takes difference between modified x and y values and squares them
distance_between_y = pow(distance_y, 2)
distance_between_x = pow(distance_x, 2)
#adds squared values together
added_distance = distance_between_y + distance_between_x
#takes square root of added distance

print(f"The total distance between coordinates (x1,y1) and (x2,y2) is {str(round(math.sqrt(added_distance), 2))}")
#I needed to understand that the curly brackets need to go around the the variable, and the quotations need to come after the "f" and after the last bracket of the variable.