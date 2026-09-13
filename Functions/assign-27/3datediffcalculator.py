
# Assignment 3 — Date Difference Calculator

# Create a program that accepts two dates and displays:

# Enter first date: 10-09-2026
# Enter second date: 25-12-2026

# Display:

# Difference in days
# Difference in weeks
# Difference in hours
# Difference in minutes

# Example:

# Days Difference: 106
# Weeks Difference: 15
# Hours Difference: 2544
# Minutes Difference: 152640
from datetime import datetime 
first = input("Enter first date: ")
second = input("Enter second date: ")

f_date = datetime.strptime(first,"%d-%m-%Y")
s_date = datetime.strptime(second,"%d-%m-%Y")


difference = s_date - f_date

day_diff = difference.days
week_diff = difference.days // 7
hours_diff = difference.days * 24
minutes_diff = difference.days * 24 * 60

print("Days Difference:", day_diff)
print("Weeks Difference:", week_diff)
print("Hours Difference:", hours_diff)
print("Minutes Difference:", minutes_diff)

