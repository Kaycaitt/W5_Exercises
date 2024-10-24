candy_type = (
    'Sour Belts',
    'Starburst',
    'Skittles'
) #this is a tuple with items separated by commas

fruity_flavors = (
    'Strawberry',
    'Pink Lemonade',
    'Grape'
) #this is a tuple with items separated by commas

candy_combinations = {
    ("Skittles", "Strawberry", "Grape"),
    ("Starburst", "Strawberry"),
    ("Sour Belts", "Pink Lemonade", "Strawberry", "Grape")
} #this is required to be a set

print("Today's candy options include:" + str(candy_combinations))
#When printing the output multiple times, I noticed that the order of each candy type changes. However, the fruity flavors retain their proper positions within the candy type.
