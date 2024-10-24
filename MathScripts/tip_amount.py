#Question: How do you calculate the tip amount on a restaurant bill given the tip percentage?

bill_total = 365.98
tip = 0.15

tip_amount = bill_total * tip

print("The tip on a $" + str(bill_total) + " restaurant bill is $" + str(format(tip_amount, ".2f")))

#code runs when running specific code lines, when trying to run whole file, I get SyntaxError: invalid syntax. Reach out to Bess about this
#Figured it out, VS Code bug and typing exit() in the terminal below fixes the issue.