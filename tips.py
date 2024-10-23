# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00

# Calculate the unknown
total_due = food_cost + tax + tip

# Display the results
#print("The total due is " +str(total_due))
#str is added because concatenation can not be applied when using float numbers

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
#print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))
#Bonus Question: It doesn't apply the variables established previously in the script because the "quotations" used are backticks seemingly in the workbook.
