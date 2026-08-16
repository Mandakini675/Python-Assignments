
# =====================================================================
# QUESTION 2: STUDENT RESULT PROCESSING
# =====================================

# A training institute wants to manage student records using NamedTuple.

# Fields:
# roll_no, name, course, marks

# Requirements:

# 1. Read N student records from the user and store them in a list of NamedTuples.

# ---

# 2. Display all student details.

# ---

# 3. Find and display the topper of the class.

# ---

# 4. Count and display the number of students scoring above 80 marks.

# ---

# 5. Calculate and display the average marks.

# ---

# 6. Accept a course name from the user and display all students enrolled in that course.

# ---

# Test Case:

# Input:
# Enter number of students: 4

# 1 Ravi Python 85
# 2 Anjali Java 78
# 3 Karan Python 92
# 4 Pooja Testing 88

# Enter course: Python

# Expected Output:
# Topper:
# 3 Karan Python 92

# Students Above 80:
# 3

# Average Marks:
# 85.75

# Students in Python Course:
# 1 Ravi Python 85
# 3 Karan Python 92

from collections import namedtuple
print("=================================================================")
print("             STUDENT RESULT PROCESSING")
print("==================================================================")
n= int(input("enter no of students ="))

Stud = namedtuple("Studentresult",["roll_no", "name", "course", "marks"])
students =[]
for i in range(n):
    roll = int(input("enter rollno ="))
    name = input("enter name =")
    course = input("enter course name =")
    mark = int(input("enter marks ="))
    s = Stud(roll,name,course,mark)
    students.append(s)

print("details :")
for x in students:
    print(*x)

cour = input("enter the course name to search:")
count=0
topper = students[0]
total = 0
for sts in students:
    if sts.marks >topper.marks:
        topper = sts
    if sts.marks >= 80:
        count+=1       
    total += sts.marks

average = total/n
print("Topper:")
print(*topper)
print("Students Above 80:")
print(count)

print("Average Marks:")
print(average)

print("Students in Python Course:")
for x in students:
    if x.course == cour:
        print(*x)