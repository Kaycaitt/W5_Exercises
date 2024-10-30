starting_balance = float(input("Please enter your starting bank balance:"))
savings_goal = float(input("Please enter your savings goal amount: "))
weekly_savings = float(input("Please enter your weekly savings amount: "))

while starting_balance < savings_goal:
    starting_balance += weekly_savings
    print(f'''This week my balance increased to: ${str(format(starting_balance,".2f"))}''')
    if starting_balance >= savings_goal * 0.5 and starting_balance < savings_goal *0.75:
        print(f'''Almost there! This week my balance is up to ${str(format(starting_balance,".2f"))}''')
    elif starting_balance >= savings_goal * 0.75 and starting_balance < savings_goal:
        starting_balance -= 30.85
        print(f'''So close! After treating myself, my balance is up to ${str(format(starting_balance,".2f"))}''')
    elif starting_balance == 1000:
        print(f'''Goal met! My current balance is ${str(format(starting_balance,".2f"))}''')
#after the 75%, it is taking out 30.85 each weekly save until reaching $1000