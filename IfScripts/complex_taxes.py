#Question: Calculate federal tax based on the values of annual gross income and a filing status ('single' or 'joint').
pay_rate = float(input("Please enter your rate of pay: "))
hours_worked = float(input("Please enter your hours worked: "))
regular_hours = 40
overtime = 1.5
weeks_worked = float(input("Please enter the number of weeks worked for the year: "))
filer_status = str(input("Please enter your filing status (Single/Joint): ").lower())

overtime_pay = 0
gross_pay = 0
#had to set these above variables =0 as a starting value

if hours_worked <= regular_hours:
    gross_pay = pay_rate*hours_worked
    print("You are not eligible for overtime pay. Your gross pay calculates to $" + str(format(gross_pay, ".2f")))
elif hours_worked > regular_hours:
    overtime_hours = hours_worked - regular_hours
    overtime_pay = overtime_hours*pay_rate*overtime
    gross_pay = pay_rate*hours_worked
    print("You have accrued overtime pay! You made an additional $" + 
          str(format(overtime_hours*pay_rate*overtime, ".2f")) + " for the week. Your total weekly gross pay is $" + 
          str(format((gross_pay) + (overtime_pay), ".2f")))
#in the elif print statements, I had to make sure that I was multiplying the original pay rate with the overtime hours/overtime pay.

weekly_gross_pay = gross_pay + overtime_pay
yearly_gross_pay = (gross_pay + overtime_pay) * weeks_worked
print("Your total yearly gross pay is $" + str(format(yearly_gross_pay, ".2f")))

tax_rate = 0
if filer_status == 'single':
    if yearly_gross_pay <= 12000:
        tax_rate = 0.05
    elif yearly_gross_pay <= 25000:
        tax_rate = 0.10
    elif yearly_gross_pay <= 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filer_status == 'joint':
    if yearly_gross_pay <= 12000:
        tax_rate = 0  # No tax for this range
    elif yearly_gross_pay <= 25000:
        tax_rate = 0.06
    elif yearly_gross_pay <= 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20    

#Question 4: Use tax rate to determine tax witheld for weekly gross pay.
tax_withheld_weekly = weekly_gross_pay * tax_rate
net_pay_weekly = weekly_gross_pay - tax_withheld_weekly


#Question 5: Create print statements to print relevant information determined by above calculations.
print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${weekly_gross_pay:.2f}.")
print(f"Your filing status is {filer_status}.")
print(f"Your tax withholding for the week is ${tax_withheld_weekly:.2f}.")
print(f"Your net pay is ${net_pay_weekly:.2f}.")