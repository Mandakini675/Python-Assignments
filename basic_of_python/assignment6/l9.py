"""
9. Student Attendance Eligibility System

A college determines whether a student is eligible to sit for exams based on attendance percentage:

* 75% and above → Eligible
* 60% to 74% → Eligible with warning
* Below 60% → Not eligible

Write a Python program to check eligibility.

Input:
Enter attendance percentage: 58

Output:
Status: Not Eligible

"""
att = int(input("Enter attendance percentage: "))
if att >=75:
    elig="Eligible"
elif att<75 and att>60:  
    elig="Eligible with warning"
else:
    elig ="not eligible"
print("Status =",elig)

