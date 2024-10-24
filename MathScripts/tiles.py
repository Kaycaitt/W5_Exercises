#Question: How many boxes of tiles do you need? (Can only buy full boxes, no partials)
import math
#all values are in feet
tile_length = 1
tile_width = 1

tiles_per_box = 12

room_dimension = 150

tile_total = room_dimension / (tile_width * tile_length)

boxes_needed = tile_total / tiles_per_box

print("The number of boxes of tiles needed for a " + str(room_dimension) + " sqft room is " + str(math.ceil(boxes_needed)))

#Question: You also want to buy 10% more tiles than you need in order to handle chips, breakage, and mess-ups. How many total boxes will you buy?

additional_boxes = .10

total_boxes_needed = additional_boxes * boxes_needed

print("For handling chips, breakage, and mess-ups, I will need to purchase an extra " + str(math.ceil(total_boxes_needed)) + " boxes")