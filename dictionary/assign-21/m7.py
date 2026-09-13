
# 7.

# =========================================
# ONLINE EXAM RESULT SYSTEM
# =========================

# Store student marks in a dictionary.

# results = {
# "Ajay":88,
# "Ravi":45,
# "Neha":76,
# "Aman":39
# }

# Write a program to:

# * Display names of students who passed.
#   (Passing Marks = 50)

# Sample Output:
# Ajay
# Neha
# Ravi

# ---
print("===========================")
print(" ONLINE EXAM RESULT SYSTEM")
print("============================")

n = [name  for name in input("enter the name of all students").split()]
mar = [int(mark) for mark in input("enter the marks of all students").split()]

result = {}
for i in (range(len(n))):
    result[n[i]] = mar[i]

for x in result:
   if result[x]>50:
    print(x)