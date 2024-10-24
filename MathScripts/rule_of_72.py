#Question: How long will it take a savings account worth X to double in value based on an interest rate of IR?

savings_worth = 5000
doubled = 10000
ir = 0.04

value_in_years = 72/(ir*100)

print("At a " + str(format(ir, "0.0%")) +  " interest rate, your savings account will be worth " + str(format(doubled, ".2f")) + " in " + str(format(value_in_years, ".1f")))