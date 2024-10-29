#Question: Create conditional logic that determines/prints department name based on department code

#Define the known
Marketing = 1
Human_Resources = 5
Accounting = 10
Legal = 12
IT = 18
Customer_Relations = 20

#Calculate the Unknown
department_code = int(input("Enter your department code here: "))
#noting that I needed to set this question as a variable instead of just a print statement. Also needed to cast as integer.

if department_code == 1:
    print("This is the Marketing department.")
elif department_code == 5:
    print("This is the Human Resources department.")
elif department_code == 10:
    print("This is the Accounting department.")
elif department_code == 12:
    print("This is the Legal department.")
elif department_code == 18:
    print("This is the IT department.")
elif department_code == 20:
    print("This is the Customer Relations department.")
else:
    print("This is not a valid department.")

#Display the Results
