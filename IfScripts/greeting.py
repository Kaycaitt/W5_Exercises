#Question: Define a variable that contains the current hour (0-23). Display one of the greetings below based on the current hour:

#Define the Known:
hours = range(0-23)

#Calculate the Unknown
current_hour = int(input("What is the current hour? "))

if current_hour <= 10:
    print("Good morning!")
elif current_hour <= 17:
    print("Good day!")
elif current_hour <= 23:
    print("Good evening!")
else: 
    print("This is not a valid submission.")

if current_hour >= 23 or current_hour < 4:
        print("What are you doing up so late??")
#I tried to add this to the existing conditional logic as elif, but found it wouldn't reach as other statements were deemed true. Had to add as additional if statement.