
# 5.
#  Student Grade Classification System (Python List Assignment)
# A school stores student marks n a list. The system must analyze the marks and generate a *clear performance report*
# by grouping students into grade categories.
# Write a Python program to:

# * Iterate through the list of marks
# * Assign grades based on marks:
#   * *>= 90 → A*
#   * *>= 75 and < 90 → B*
#   * *>= 50 and < 75 → C*
#   * *< 50 → Fail*
# * Store each category in separate lists
# * Count students in each category
# * Display a *final structured report (important)*
# ---
# ## 📌 Output Format (Mandatory)
# Your output must be displayed exactly in this format:
# ===== STUDENT GRADE REPORT =====

# A Grade Students   : [list]
# B Grade Students   : [list]
# C Grade Students   : [list]
# Fail Students      : [list]

# --------------------------------
# A Count   : X
# B Count   : X
# C Count   : X
# Fail Count: X
# --------------------------------
# Total Students: X
# ---
#  Input
# [95, 82, 67, 45, 30]
# Output
# ===== STUDENT GRADE REPORT =====
# A Grade Students   : [95]
# B Grade Students   : [82]
# C Grade Students   : [67]
# Fail Students      : [45, 30]
# --------------------------------
# A Count   : 1
# B Count   : 1
# C Count   : 1
# Fail Count: 2
# --------------------------------
# Total Students: 5

n= int(input("enter the no of students:"))
l=[]
for i in range(n):
   l.append(int(input("enter marks")))

count_A=0
count_C=0
count_B=0
count_f=0
ch=[]
print("===== STUDENT GRADE REPORT =====")
for i in range(len(l)):
    if l[i]>= 90:
      ch.append("A")
      count_A+=1
    elif l[i]>= 75 and l[i]< 90:
      ch.append("B")
      count_B+=1
    elif l[i]>= 50 and l[i]< 75:
      ch.append("C")
      count_C+=1
    elif l[i]<50:
      ch.append("fail")
      count_f+=1
ch.sort()
for i,grad in range(len(ch)):
    print(f"{ch[grad]} Grade Students  :[{l[i]}]")
  

print("-"*20)
print(f"A Count  : {count_A}")
print(f"B Count   : {count_B}")
print(f"C Count   : {count_C}")
print(f"Fail Count: {count_f}")
print("-"*20)