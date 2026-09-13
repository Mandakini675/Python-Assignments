
# 4.

# =========================================
# STUDENT GRADE ANALYSIS
# ======================

# Store student marks in a dictionary.

# students = {
# "Ajay":78,
# "Ravi":92,
# "Neha":85,
# "Aman":65
# }

# Write a program to:

# * Find the student with highest marks.
# * Find the student with lowest marks.

# Sample Output:
# Highest Marks : Ravi 92
# Lowest Marks : Aman 65

# ---
print("===========================")
print("STUDENT GRADE ANALYSIS")
print("============================")
n = int(input("enter no of inputs :"))
stud = {}
for i in range(n):
   key,val = input("enter student name and marks :").split()
   stud[key] = int(val)
highest = max(stud.values())
lowest = min(stud.values())


for key in stud:
    if stud[key] == highest:
        print("Highest Marks :", key, highest)

    if stud[key] == lowest:
        print("Lowest Marks :", key, lowest)