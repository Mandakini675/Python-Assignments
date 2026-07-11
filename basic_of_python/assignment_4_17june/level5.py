"""-------------------------
Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5

---------------------------"""
salary = int(input("Monthly salary = "))
w_days = int(input("salary per day = "))
w_p_hrs = int(input("working per day = "))
 
calc_dy = salary/w_days
calc_hrs = calc_dy/w_p_hrs

print("Salary per day = ",calc_dy)
print("Salary per hour = ",calc_hrs)