"""-------------------------
4. Gym Membership Eligibility Checker
   A gym checks multiple conditions:

* If age ≥ 18 → Allowed for gym
* If BMI > 25 → Suggest weight loss program

Input:
Enter age: 25
Enter BMI: 27

Output:
Gym access granted
Enroll in weight loss program
---------------------"""
age = int(input("enter the age"))
bmi = int(input("whats is your bmi"))
if age>=18:
   print("Gym access granted")
if bmi>25:
   print("Enroll in weight loss program")