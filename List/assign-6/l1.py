# =====================================================================
# QUESTION 1: employees SALARY ANALYSIS
# ====================================

# A company wants to store employees details and generate salary reports using NamedTuple.

# Fields:
# emp_id, emp_name, department, salary

# Requirements:

# 1. Read N employees details from the user and store them in a list of NamedTuples.

# ---

# 2. Display all employees details.

# ---

# 3. Find and display the employees with the highest salary.

# ---

# 4. Find and display the employees with the lowest salary.

# ---

# 5. Calculate and display the average salary of all employeess.

# ---

# 6. Accept a department name from the user and display all employeess belonging to that department.

# ---

# Test Case:

# Input:
# Enter number of employeess: 4

# 101 Rahul IT 50000
# 102 Priya HR 45000
# 103 Amit IT 70000
# 104 Neha Finance 60000

# Enter department: IT

# Expected Output:
# Highest Salary employees:
# 103 Amit IT 70000

# Lowest Salary employees:
# 102 Priya HR 45000

# Average Salary:
# 56250.0

# employeess in IT Department:
# 101 Rahul IT 50000
# 103 Amit IT 70000

# ields:
# emp_id, emp_name, department, salary

print("====================================================================")
print("           employees SALARY ANALYSIS")
print(" ==================================================================")

n = int(input("enter no of emploYE in :"))
from collections import namedtuple
Employee = namedtuple("employees",["emp_id", "emp_name", "department", "salary"])
employees =[]
for i in range(n):
    e_id = int(input("enter id ="))
    name = input("enter name = ")
    depart = input("enter department name = ")
    sal = int(input("enter salary ="))
    e1 = Employee(e_id,name ,depart,sal)
    employees.append(e1)
print("details :")
print("-"*20)
for x in employees:
    print(*x)
print("-"*20)


high = employees[0]
low = employees[0]
total_salary = 0

for emp in employees:

    if emp.salary > high.salary:
        high = emp

    if emp.salary < low.salary:
        low = emp

    total_salary += emp.salary

average_salary = total_salary / n
print("-"*20)
print("Highest Salary Employee:")
print(*high)

print("Lowest Salary Employee:")
print(*low)

print("Average Salary:")
print(average_salary)
print("-"*20)

#another try
# emp = employees[0]
# emp2 = employees[0] 
# high = employees[0].salary
# low = employees[0].salary
# sumsalary = 0
# for i in range(n):
#     if employees[i].salary >= high:
#         high = employees[i].salary
#         emp = employees[i]
#     if employees[i].salary <= low :
#         low = employees[i].salary
#         emp2 = employees[i]
#     sumsalary += employees[i].salary

# av = sumsalary//n
# print("Highest Salary employees: ")
# print(*emp) 

# print(" Lowest Salary employees: ")
# print(*emp2)
# # 102 Priya HR 45000

# print(" Average Salary: ")
# print(av)
# # 56250.0
