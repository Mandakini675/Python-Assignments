
# 2.
#  Employee Joining & Experience System

# Create an employee experience calculator.

# Read:

# Employee name
# Joining date
# Current date

# Calculate:

# Total days worked
# Total years worked
# Total months approximately
# Experience in Years Months Days
# Whether employee has completed 1 year
# Whether employee has completed 5 years

# Example:

# Enter employee name: Rahul
# Enter joining date: 10-06-2021
# Enter current date: 10-09-2026

# Output:

# Employee: Rahul
# Joining Date: 10-06-2021
# Experience: 5 Years 3 Months 0 Days
# Total Days Worked: 1918
# 5 Years Completed: Yes
from datetime import datetime ,date, timedelta
employee_name = input("Enter your name :")
joining_date = input("Enter joining date :")
current_date = input("Enter current date :")

j_date = datetime.strptime(joining_date,"%d-%m-%Y")
c_date = datetime.strptime(current_date,"%d-%m-%Y")

total_days = (c_date.date()-j_date.date()).days
five_year_date = date(
    j_date.year + 5,
    j_date.month,
    j_date.day
)
if c_date.date()>five_year_date:
    complet="yes"
else:
    complet = "No"

years = c_date.year - j_date.year
months = c_date.month - j_date.month
days = c_date.day - j_date.day

if months < 0:
    years -= 1
    months += 12
experience = f"{years} years {months} months {days} days"

print("Employee: ",employee_name)
print("Joining Date: ",j_date.date())
print("Experience: ",experience)
print("Total Days Worked: ",total_days)
print(f"5 Years Completed: ",complet)
