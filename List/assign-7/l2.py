# 2.
# =========================================
# ONLINE COURSE ENROLLMENT SYSTEM
# =========================================

# An institute offers:
# 1. Python Course
# 2. Java Course

# Store enrolled student email IDs using sets.

# Menu:
# 1. Enroll Student in Python
# 2. Enroll Student in Java
# 3. Display Python Students
# 4. Display Java Students
# 5. Find Students Enrolled in Both Courses
# 6. Find Students Enrolled Only in Python
# 7. Find Students Enrolled Only in Java
# 8. Check Enrollment in Python Course
# 9. Display Total Unique Students
# 10. Exit

# Requirements:
# - Use two sets.
# - Use membership operator (in).
# - Use union, intersection and difference operations.


    
print("=========================================")
print("      ONLINE COURSE ENROLLMENT SYSTEm")
print("=========================================")

set_a = set()
set_b = set()
while True:
    print("Menu")
    print("1. Enroll Student in Python")
    print("2. Enroll Student in Java")
    print("3. Display Python Students")
    print("4. Display Java Students")
    print("5. Find Students Enrolled in Both Courses")
    print("6. Find Students Enrolled Only in Python")
    print("7. Find Students Enrolled Only in Java")
    print("8. Check Enrollment in Python Course")
    print("9. Display Total Unique Students")
    print("10. Exit")
    
    ch= int(input("enter your choice :"))
    match ch:

        case 1:
             new = {x for x in input("Enter your EMAIL IDS to PYTHON course: ").split()}
             set_a.update(new)
        case 2:
             new = {x for x in input("Enter your EMAIL IDS to join Java course : ").split()} 
             set_b.update(new)
        case 3:
             print("PYTHON students are:")
             for x in set_a:
                print(x)
        case 4:
             print("JAVA students are:")
             for x in set_b:
                print(x)

        case 5:
             print("students enrolled in both")
             print(set_a.intersection(set_b))
        case 6:
             print("students enrolled ONLY in python")
             print(set_a.difference(set_b))
        case 7:
             print("students enrolled ONLY in java")
             print(set_b.difference(set_a))
        case 8:
             email = input("enter email if student is enrolled =")
             if (email in set_a) or (email in set_b):
                print("enrolled already ")
             else:
                print("no data found")
        case 9:
             print("Total unique elements ")
             print(len(set_a.union(set_b)))
        case 10:
             print("thanks ................")
             break