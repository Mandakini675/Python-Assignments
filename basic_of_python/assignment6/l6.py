"""
6. Company Bonus Distribution System


A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6

Output:
Bonus Amount: ₹5000
"""
s = int(input("Enter salary: "))
expr = int(input("Enter years of experience: "))
if expr>10:
     bonus = (20/100)*s
elif expr<=10 and expr>5:
     bonus = (10/100)*s
elif expr<=5 and expr>2:
     bonus = (10/100)*s
else:
     print("no bonus")
print("Bonus Amount :",bonus)