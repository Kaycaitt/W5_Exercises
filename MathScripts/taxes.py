#Question: Federal taxes are 23% of your salary every month. You make X amount of money. How much is witheld from taxes?

federal_taxes = 0.23
monthly_income = 5275

witheld_money = monthly_income * federal_taxes

print("Federal taxes takes $" + str(round(witheld_money, 2)) + " from my paycheck each month.")