#Question: How many vans do you need? What is the cost to rent vans? What is the cost to split per person?

import math

van_seats = 15
van_rent = 250
days = 1
people = 38

vans_needed = people/van_seats
rental_cost = (van_rent * vans_needed) * days
per_person = rental_cost / people

#print(per_person)
#print(rental_cost)

print("The number of vans needed is " + str(math.ceil(vans_needed)) + " and it will cost $" + str(format(rental_cost, ".2f")) + " to rent the van for " + str(days) + " day. It will cost $" + str(round(per_person, 2)) + " per person if split.")

#How much money to charge per person?: $16.67
#How much is collected?: $633.46
#How much were the vans?: $633.33
#Why do you have leftover money?: I rounded the money per person up to 2 decimal places.