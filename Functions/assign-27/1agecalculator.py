# Assignment 1 — Age Calculator

# Create a program that accepts the user's date of birth and calculates:

# Current age in years
# Completed months
# Total number of days lived
# Next birthday date
# Number of days remaining for the next birthday

# Input:

# Enter DOB (DD-MM-YYYY): 15-08-1998

# Expected Output:

# Age: 28 years
# Total Days Lived: XXXXX days
# Next Birthday: 15-08-2027
# Days Remaining: XX days

from datetime import datetime,date,timedelta
inp = input("Enter DOB (DD-MM-YYYY): ")
db = datetime.strptime(inp,"%d-%m-%Y")
dob = db.date()
td = date.today()

# age finding here
age = td.year-dob.year
print("Age : ",age," years")

# total days lived here
total_days = (td - dob).days
print(f"Total Days Lived: {total_days} days")

next_birthday = date(td.year + 1, dob.month, dob.day)
print(f"Next Birthday: {next_birthday.strftime('%d-%m-%Y')}")

days_remaining = (next_birthday - td).days
print(f"Days Remaining: {days_remaining} days")
