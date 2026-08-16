# 1.
# =========================================
# STUDENT CLUB MEMBERSHIP SYSTEM
# =========================================

# A college has two clubs:
# 1. Coding Club
# 2. Robotics Club

# Store student IDs of both clubs using sets.

# Menu:
# 1. Add Student to Coding Club
# 2. Add Student to Robotics Club
# 3. Display Students in Coding Club
# 4. Display Students in Robotics Club
# 5. Find Students in Both Clubs
# 6. Find Students Only in Coding Club
# 7. Find Students Only in Robotics Club
# 8. Display All Unique Club Members
# 9. Display Total Unique Club Members
# 10. Exit

# Requirements:
# - Use two sets.
# - Apply intersection, difference, and union operations.

print("=========================================")
print("STUDENT CLUB MEMBERSHIP SYSTEM")
print("=========================================")

set_a = set()
set_b = set()
while True:
    print("Menu")
    print("1. Add Student to Coding Club")
    print("2. Add Student to Robotics Club")
    print("3. Display Students in Coding Club")
    print("4. Display Students in Robotics Club")
    print("5. Find Students in Both Clubs")
    print("6. Find Students Only in Coding Club")
    print("7. Find Students Only in Robotics Club")
    print("8. Display All Unique Club Members")
    print("9. Display Total Unique Club Members")
    print("10. Exit")
    
    ch= int(input("enter your choice :"))
    match ch:

        case 1:
             set_a = {int(x) for x in input("Enter your IDS to join coding club: ").split()}

        case 2:
             set_b = {int(x) for x in input("Enter your IDS to join robotics club: ").split()} 

        case 3:
             print("Students in the coding club:")
             for x in set_a:
                 print(x)

        case 4:
            print("Students in the robotics club:")
            for x in set_b:
                print(x)

        case 5:
              print("students in both clubs :")
              print(set_a.intersection(set_b))
        case 6:
            print(" Students Only in Coding Club:")
            print(set_a.difference(set_b))
        case 7:
            print(" Students Only in robotics Club:")
            print(set_b.difference(set_a))

        case 8:
            print("All Unique Club Members:")
            print(set_a.union(set_b))

        case 9:
            print("Total Unique Club Members:")
            print(len(set_a.union(set_b)))
        case 10:
            print("thanks for using.......")
            break


    
# print("=========================================")
# print("STUDENT CLUB MEMBERSHIP SYSTEM")
# print("=========================================")

# set_a = {int(x) for x in input("Enter your IDS to join coding club: ").split()}
# set_b = {int(x) for x in input("Enter your IDS to join robotics club: ").split()} 

# while True:
#     print("Menu")
#     print("1. Add Student to Coding Club")
#     print("2. Add Student to Robotics Club")
#     print("3. Display Students in Coding Club")
#     print("4. Display Students in Robotics Club")
#     print("5. Find Students in Both Clubs")
#     print("6. Find Students Only in Coding Club")
#     print("7. Find Students Only in Robotics Club")
#     print("8. Display All Unique Club Members")
#     print("9. Display Total Unique Club Members")
#     print("10. Exit")
    
#     ch= int(input("enter your choice :"))
#     match ch:

#         case 1:

#         case 2:

#         case 3:

#         case 4:

#         case 5:

#         case 6:

#         case 7:

#         case 8:

#         case 9:

#         case 10:
        