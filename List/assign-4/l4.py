
# 4.

# =========================================================
#         MATRIX DIAGONAL ANALYSIS SYSTEM
# =========================================================

# Scenario

# A security company stores surveillance data in matrix form.
# The analyst wants a menu-driven application to examine the
# diagonal elements of the matrix and generate reports.

# The application should allow the user to:

# 1. Display Main Diagonal Elements
# 2. Display Secondary Diagonal Elements
# 3. Compare Main and Secondary Diagonal Sums
# 4. Exit

# ---------------------------------------------------------
# Requirements
# ---------------------------------------------------------

# 1. Display the following menu repeatedly until the user selects Exit.

#    1. Display Main Diagonal Elements
#    2. Display Secondary Diagonal Elements
#    3. Compare Main and Secondary Diagonal Sums
#    4. Exit

# 2. Read the size of a square matrix from the user.

# 3. Read all matrix elements from the user.

# 4. Based on the user's choice:

#    Choice 1 - Display Main Diagonal Elements
#    -----------------------------------------
#    Display all elements present in the main diagonal.

# 5. Choice 2 - Display Secondary Diagonal Elements
#    ----------------------------------------------
#    Display all elements present in the secondary diagonal.

# 6. Choice 3 - Compare Main and Secondary Diagonal Sums
#    ---------------------------------------------------
#    Calculate the sum of both diagonals and display:

#    - Main Diagonal Sum
#    - Secondary Diagonal Sum
#    - Which diagonal has the greater sum
#    - Or whether both sums are equal

# 7. Choice 4 - Exit
#    -----------------------------------------
#    Display:
#    "Thank You for Using Matrix Diagonal Analysis System"

# ---------------------------------------------------------
# Sample Input/Output
# ---------------------------------------------------------

# Enter size of matrix: 3

# Enter matrix elements:

# 1 2 3
# 4 5 6
# 7 8 9

# Menu
# 1. Display Main Diagonal Elements
# 2. Display Secondary Diagonal Elements
# 3. Compare Main and Secondary Diagonal Sums
# 4. Exit

# Enter your choice: 1

# Output:
# Main Diagonal Elements:
# 1 5 9

# ---------------------------------------------------------

# Enter your choice: 2

# Output:
# Secondary Diagonal Elements:
# 3 5 7

# ---------------------------------------------------------

# Enter your choice: 3

# Output:
# Main Diagonal Sum = 15
# Secondary Diagonal Sum = 15
# Both Diagonal Sums are Equal

# ========================================================

print("=========================================================")
print("             MATRIX DIAGONAL ANALYSI SYSTEM")
print("=========================================================")


while True:

   print("Menu")
   print("1. Display Main Diagonal Elements")
   print("2. Display Secondary Diagonal Elements")
   print("3. Compare Main and Secondary Diagonal Sums")
   print("4. Exit")
   
   choice = int(input("enter your choice :"))
   if choice == 4:
      print("Thank You for Using Matrix  Quality Check System")
      break
   r1 = int(input("Enter no of r for Matrix :"))
   c1 = int(input("Enter NO OF c for Matrix :"))
   matric = []
   for i in range(r1):
       row = [int(x) for x in input("enter elements of row").split()]
       matric.append(row)
  
   match choice:
       case 1:
           if r1 != c1:
               print("Diagonal operations require a square matrix.")
           else:
             diag = []
             for i in range(r1):              
               
                  curr_elem = matric[i][j]
                  if i == j:             
                     diag.append(curr_elem)
             print("main diagonal elements are ",*diag)
       
       case 2:
           if r1 != c1:
               print("Diagonal operations require a square matrix.")
           else:
             sec_diag = []
             for i in range(r1):             
               for j in range(c1):
                  curr_elem = matric[i][j]
                  if i+j==(c1-1):
                     
                     sec_diag.append(curr_elem)
             print("secondary elements are ",*sec_diag)
       case 3:
           if r1 != c1:
               print("Diagonal operations require a square matrix.")
           else:
            diag = []
            sec_diag = []
            for i in range(r1):
               
               for j in range(c1):
                  curr_elem = matric[i][j]
                  if i == j:
                     diag.append(curr_elem)
                  if i+j==(c1-1):
                     sec_diag.append(curr_elem)
            d1 = sum(diag)
            d2 = sum(sec_diag)
            if d1==d2:
               print("both sum are equal ")
            elif d1>d2:
               print("sum of main diagonal is greater")
            else:
               print("sum of secondary diagonal is greater")
       case _:
            print("you enterd wrong option try again")