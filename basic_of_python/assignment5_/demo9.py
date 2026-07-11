"""------------------
9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books
---------------------------"""
membrship = input("Membership active (yes/no): ")
b_issue = int(input("how much book issued "))

if membrship == "yes":
     print("Entry allowed")
     if b_issue<3:
         print("can issue more books")
