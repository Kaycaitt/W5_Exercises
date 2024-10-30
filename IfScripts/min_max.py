#Question: Create a script that displays both the smallest and largest of 3 numbers.

# a = float(input("Please enter a number here: "))
# b = float(input("Please enter a second number here: "))
# c = float(input("Please enter a third number here: "))

a = 7328
b = 4
c = 6483143

if a <= b and a <= c:
    smallest = a
else:
    if b <= a and b <= c:
        smallest = b
    else:
        smallest = c

if a >= b and a >= c:
    largest = a
else:
    if b >= a and b >= c:
        largest = b
    else:
        largest = c

print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")