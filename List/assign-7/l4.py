
# 4.
# =========================================
# FROZEN SET SUBJECT MANAGEMENT
# =========================================

# An institute offers fixed subjects:

# Python
# Java
# MySQL
# React
# Spring Boot

# These subjects cannot be modified after creation.

# Menu:
# 1. Display Subjects
# 2. Search Subject
# 3. Count Subjects
# 4. Attempt to Add Subject
# 5. Exit

# Requirements:
# - Use Frozen Set.
# - Show that modification is not allowed.

print("=========================================")
print("FROZEN SET SUBJECT MANAGEMENT")
print("=========================================")
courses = frozenset(["python","java","mysql","react","springboot"])
while True:
    print("Menu")
    print("1. Display Subjects")
    print("2. Search Subject")
    print("3. Count Subjects")
    print("4. Attempt to Add Subject")
    print("5. Exit")
    
    ch= int(input("enter your choice :"))
    match ch:

        case 1:
             print("="*30)
             print("subjects : ")
             for x in courses:
                print(x)
             print("="*30)

        case 2:
            subject = input("enter subject to check :").lower()
            if subject in courses:
                print("it is here..")
            else:
                print("not found ")
        case 3:
            print("total subjects :")
            print(len(courses))
        case 4:
            try:
                subject = input("Add subject: ")
                courses.add(subject)
            except AttributeError:
                print("Modification is not allowed.")
        case 5:
            print("thanks for using")
            break
        case _:
           print("wrong try again...")