#Question 1: Customize the prompt within parenthese as appropriate for your chosen exercise.

bill_total = 365.98
tip = input("How much would you like to tip as a percentage (whole number)? ")
#noting that for input, you MUST place a space so the user can input a value and specify what type should go there.

tip_percentage = float(tip) / 100
tip_amount = bill_total * tip_percentage
#I also learned I needed to create two new variables to help calculate the tip properly for the resulting print statement
print("The tip on a $" + str(bill_total) + " restaurant bill is $" + str(format(tip_amount, ".2f")))

#a pitfall in my coding is that you will need to name a percentage(whole number) that you would like to tip, not a dollar amount.
#pit fall is having to create additional variables and equations, must test out to ensure code works with input of input function
#having to translate the tip into a float so that input can be accepted