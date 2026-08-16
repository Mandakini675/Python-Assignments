
# 2.

# =========================================================
#             MATRIX ANALYSIS SYSTEM
# =========================================================


# A research laboratory stores experimental data in matrix form.
# Scientists want a program that can analyze the matrix and provide
# different statistics through a menu-driven application.

# The application should allow the user to:

# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Count Prime Numbers Row-wise
#    2. Count Perfect Numbers Column-wise
#    3. Display Row-wise Sum
#    4. Exit

# 2. Read the number of rows and columns from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Count Prime Numbers Row-wise
#    ---------------------------------------
#    Count and display the number of prime numbers present
#    in each row of the matrix.

# 5. Choice 2 - Count Perfect Numbers Column-wise
#    --------------------------------------------
#    Count and display the number of perfect numbers present
#    in each column of the matrix.

#    Note:
#    A perfect number is a number that is equal to the sum
#    of its proper divisors.

#    Examples:
#    6  = 1 + 2 + 3
#    28 = 1 + 2 + 4 + 7 + 14

# 6. Choice 3 - Display Row-wise Sum
#    --------------------------------
#    Calculate and display the row_sumof each row.

# 7. Choice 4 - Exit
#    --------------------------------
#    Display:
#    "Thank You for Using Matrix Analysis System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 1

# Enter rows: 3
# Enter columns: 3

# Enter matrix elements:
# 2 4 5
# 6 7 8
# 11 28 13

# Output:
# Row 1 Prime Count = 2
# Row 2 Prime Count = 1
# Row 3 Prime Count = 2

# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 2

# Output:
# Column 1 Perfect Number Count = 1
# Column 2 Perfect Number Count = 1
# Column 3 Perfect Number Count = 0

# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 3

# Output:
# Row 1 row_sum= 11
# Row 2 row_sum= 21
# Row 3 row_sum= 52

# ---------------------------------------------------------

# Menu
# 1. Count Prime Numbers Row-wise
# 2. Count Perfect Numbers Column-wise
# 3. Display Row-wise Sum
# 4. Exit

# Enter your choice: 4

# Output:
# Thank You for Using Matrix Analysis System

# =========================================================

import math
print("=========================================================")
print("             MATRIX ANALYSIS SYSTEM")
print("=========================================================")


while True:

   print("Menu")
   print("1. Count Prime Numbers Row-wise")
   print("2. Count Perfect Numbers Column-wise")
   print("3. Display Row-wise Sum")
   print("4. Exit")
   
   choice = int(input("enter your choice :"))
   if choice == 4:
      print("Thank You for Using Matrix Analysis System")
      break
   r1 = int(input("Enter no of r for Matrix :"))
   c1 = int(input("Enter NO OF c for Matrix :"))
   matric = []
   for i in range(r1):
       row = [int(x) for x in input("enter elements of row").split()]
       matric.append(row)
  
   match choice:
       case 1:
             for i in range(r1):
               count=0
               for j in range(c1):
                  curr_elem = matric[i][j]
                  if curr_elem >1:
                     p = 2
                     while p<=int(math.sqrt(curr_elem)):
                        if curr_elem % p == 0:
                           break              
                        p += 1
                     else:
                        count+=1
               print(f"ROW {i+1} Prime count = {count}")
       case 2:
             for j in range(c1):
               count=0
               for i in range(r1):
                  curr_elem = matric[i][j]
                  rsum=0
                  p=1
                  while p < curr_elem:
                     if curr_elem % p == 0:
                        rsum+=p            
                     p += 1
                  if rsum== curr_elem:
                     count+=1
               print(f"Column {j+1} Perfect Number Count = {count}")
       case 3:
              
            for i in range(r1):
               row_sum=0
               for j in range(c1):
                  curr_elem = matric[i][j]
                  row_sum+= curr_elem
               print(f"Row {i+1} sum= {row_sum}")

       case _:
            print("you enterd wrong option try again")