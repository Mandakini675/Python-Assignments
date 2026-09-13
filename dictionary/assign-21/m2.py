
# 2.

# =========================================
# EMPLOYEE DEPARTMENT COUNT
# =========================

# A company stores employee department names in a list.

# employees = ["HR","IT","HR","Sales","IT","IT","Finance"]

# Write a program to:

# * Count how many employees belong to each department.
# * Store the result in a dictionary.

# Sample Output:
# {'HR': 2, 'IT': 3, 'Sales': 1, 'Finance': 1}

# ---

# employees = ["HR","IT","HR","Sales","IT","IT","Finance"]
# d = {}
# for i in range(len(employees)):   
#     if employees[i] not in d:
#           d[employees[i]] = employees.count(employees[i])   
# print(d)


#~~~~ better way (●'◡'●)
# employees = ["HR","IT","HR","Sales","IT","IT","Finance"]
employees = [elem for elem in input("enter the  department names:").split()]
d = {}
for x in employees: 
    if x in d:
          d[x] += 1
    else:
        d[x] =1
    
print(d)
