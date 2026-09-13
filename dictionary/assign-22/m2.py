
# 2.

# ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

# A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

# Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

# The system should store student records in a nested dictionary where:

# Key → Student ID
# Value → Dictionary containing student information

# Each student record should contain:

# Student Name
# Course Name
# Mobile Number
# Fees
# City
# Sample Data Structure
# {
# 101:{
#     "name":"Ajay",
#     "course":"Python",
#     "mobile":"9876543210",
#     "fees":25000,
#     "city":"Indore"
# },
# 102:{
#     "name":"Ravi",
#     "course":"Java",
#     "mobile":"9876500000",
#     "fees":22000,
#     "city":"Bhopal"
# }
# }
# Menu Driven Program

# Display the following menu repeatedly until the user chooses Exit.

# =========================================
#  STUDENT MANAGEMENT SYSTEM
# =========================================

# 1. Add New Student
# 2. Search Student
# 3. Update Course
# 4. Delete Student
# 5. Display All Students
# 6. Count Total Students
# 7. Display Students By Course
# 8. Display Students By City
# 9. Find Student Paying Highest Fees
# 10. Find Student Paying Lowest Fees
# 11. Exit
# Functional Requirements
# 1. Add New Student

# Accept the following details:

# Student ID
# Student Name
# Course Name
# Mobile Number
# Fees
# City

# Store the information in the nested dictionary.

# Validation

# If Student ID already exists:

# Student ID Already Exists
# 2. Search Student

# Accept Student ID from the user.

# If found, display complete student information.

# Sample Output
# Student ID : 101
# Name       : Ajay
# Course     : Python
# Mobile     : 9876543210
# Fees       : 25000
# City       : Indore

# If not found:

# Student Not Found
# 3. Update Course

# Accept Student ID.

# If found:

# Ask for new course name.
# Update the course.
# Sample Output
# Course Updated Successfully
# 4. Delete Student

# Accept Student ID.

# If found:

# Delete the record.
# Sample Output
# Student Deleted Successfully

# Otherwise:

# Student Not Found
# 5. Display All Students

# Display all student records in a proper format.

# Sample Output
# -----------------------------------
# Student ID : 101
# Name       : Ajay
# Course     : Python
# Fees       : 25000
# -----------------------------------

# Student ID : 102
# Name       : Ravi
# Course     : Java
# Fees       : 22000
# -----------------------------------
# 6. Count Total Students

# Display total number of students enrolled.

# Sample Output
# Total Students : 45
# 7. Display Students By Course

# Accept a course name from the user.

# Display all students enrolled in that course.

# Sample Output
# Enter Course : Python

# 101  Ajay
# 105  Neha
# 112  Aman

# If no students are found:

# No Students Found
# 8. Display Students By City

# Accept city name from the user.

# Display all students belonging to that city.

# Sample Output
# Enter City : Indore

# 101  Ajay
# 108  Ravi
# 115  Pooja
# 9. Find Student Paying Highest Fees

# Display complete details of the student who has paid the highest fees.

# Sample Output
# Highest Fee Paying Student

# Student ID : 121
# Name       : Neha
# Course     : Data Science
# Fees       : 50000
# 10. Find Student Paying Lowest Fees

# Display complete details of the student who has paid the lowest fees.

# Sample Output
# Lowest Fee Paying Student

# Student ID : 131
# Name       : Aman
# Course     : React
# Fees       : 15000
# 11. Exit

# Terminate the application.

# Sample Output
# Thank You For Using Student Management System

def addstudent():
    id_no = int(input("enter the student id :"))
    
    name = input("Enter name:")
    course = input("Enter course :")
    mobile_no = int(input("enter your no:"))
    fees = int(input("Enter your fees:"))
    city = input("Enter the city name:")

    details = {
    "name":name,
    "course":course,
    "mobile":mobile_no,
    "fees":fees,
    "city":city
    }
    student[id_no] = details
#---------------

def tosearch():
    search_id = int(input("search by entering the id ")) 
    if search_id in student:
       print("Student ID : ",search_id)
       print("Name       :",student[search_id]["name"])
       print("Course     : ",student[search_id]["course"])
       print("Mobile     : ",student[search_id]["mobile"])
       print("Fees       : ",student[search_id]["fees"])
       print("City       : ",student[search_id]["city"])
    else:
        print("No record found")
#---------------
def update():
    upd_id = int(input("Enter the id to update course:")) 
    if upd_id in student:
        student[upd_id]["course"] = input("Enter the updated course name:")
        print("Course Updated Successfully")
    else:
        print("No record found")

#---------------
def delete():
    del_id = int(input("Enter the id to delete:")) 
    if del_id in student:
        student.pop(del_id)
        print("Student Deleted Successfully")
    else:
        print("NO record found")
#---------------
def display():
    for stud_id in student:
        print("-----------------------------------")
        print("Student ID : ",stud_id)
        print("Name       :",student[stud_id]["name"])
        print("Course     : ",student[stud_id]["course"])
        print("Mobile     : ",student[stud_id]["mobile"])
        print("Fees       : ",student[stud_id]["fees"])
        print("City       : ",student[stud_id]["city"])
        print("--------------------------------")

#---------------
def s_by_course():
    cour = input("Enter Course : ")
    found = False
    for stud in student:
        if student[stud]["course"]==cour:
            print(stud ,student[stud]["name"])
            found = True 
    if not found:
        print("no course found ")
#---------------
def s_by_city():
    cty = input("Enter City name : ")
    found = False
    for stud in student:
        if student[stud]["city"]==cty:
            print(stud ,student[stud]["name"])
            found = True 
    if not found:
        print("no city found ")
#---------------
def highpayed():
    highest = 0
    for idies in student:
        if student[idies]["fees"]>highest:
            highest = student[idies]["fees"]
            idyy = idies
    
    print("Highest Fee Paying Student")
    print("Name       :",student[idyy]["name"])
    print("Course     : ",student[idyy]["course"])
    print("Fees       : ",student[idyy]["fees"])
     
#---------------
def lowpayed():
    lowest = float("inf")
    for idies in student:
        if student[idies]["fees"]<lowest:
            lowest = student[idies]["fees"]
            idyy = idies
    
    print("Lowest Fee Paying Student")
    print("Name       :",student[idyy]["name"])
    print("Course     : ",student[idyy]["course"])
    print("Fees       : ",student[idyy]["fees"])
     

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``
print("=========================================")
print("        STUDENT MANAGEMENT SYSTEM")
print("=========================================")

student = {}

while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Add New Student")
    print("2. Search Student")
    print("3. Update Course")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Count Total Students")
    print("7. Display Students By Course")
    print("8. Display Students By City")
    print("9. Find Student Paying Highest Fees")
    print("10. Find Student Paying Lowest Fees")
    print("11. Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~")
    
    choice = int(input("enter your choice:"))
    match choice:
     
        case 1:
           print("====================")
           addstudent()
           print("====================")
           
        case 2:
           print("====================")
           tosearch()
           print("====================")

        case 3:
           print("====================")  
           update()
           print("====================")

        case 4:
            print("====================")  
            delete()
            print("====================")

        case 5:
            print("====================")  
            display()
            print("====================")

        case 6:
            print("====================")  
            print("Total Students : ",len(student))
            print("====================")

        case 7:
            print("====================")  
            s_by_course()
            print("====================")

        case 8:
            print("====================")  
            s_by_city()
            print("====================")

        case 9:
            print("====================")  
            highpayed()
            print("====================")

        case 10:
           print("====================")  
           lowpayed()
           print("====================")

        case 11:
             print("Thank You For Using Student Management System")
             break
        case _:
             print("you entered wrong choice:")
             print("try again-----------~!")
