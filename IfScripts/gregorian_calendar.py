#Question: Determine whether a given year is a leap year in the Gregorian calendar.
#If a year is divisible evenly by 4, it is a leap year. With that, the time between consecutive leap years is 4 years.

year = int(input("Please enter the year you are curious about: "))
leap_year = (year/4).is_integer()
#I couldn't figure out how to check for whole numbers with what we've learned so far. I used chatgpt and it said to use the .is_integer() method to check the value.
#Need to ask my peers or Bess how they properly calculated this value.

if leap_year:
    print(f"{year} is a leap year. We get an extra day and orbit the sun longer!")
else:
    print(f"{year} is NOT a leap year!")

#For question 3: The only years that aren't leap years are 1950, 1999, and 2001. All other years are leap years.