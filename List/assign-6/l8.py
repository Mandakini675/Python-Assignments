
8.
MATRIX PATTERN DETECTION SYSTEM

A satellite monitoring center stores signal strengths in matrix form. Engineers want to identify special patterns in the matrix.

Menu
1. Count Even Numbers Above Main Diagonal
2. Count Odd Numbers Below Main Diagonal
3. Display Boundary Elements
4. Exit
Requirements
Choice 1 – Count Even Numbers Above Main Diagonal

Count all even numbers where:

column > row
Choice 2 – Count Odd Numbers Below Main Diagonal

Count all odd numbers where:

row > column
Choice 3 – Display Boundary Elements

Display all elements present on:

First Row
Last Row
First Column
Last Column

without repeating corner elements.

Sample Input
1 2 3
4 5 6
7 8 9
Output
Even Numbers Above Main Diagonal = 2
(2, 6)

Odd Numbers Below Main Diagonal = 1
(7)

Boundary Elements:
1 2 3 6 9 8 7 4

print("=========================================================")
print("             MATRIX PATTERN DETECTION SYSTEM")
print("=========================================================")


while True:

   print("Menu")
   print("1. Count Even Numbers Above Main Diagonal")
   print("2. Count Odd Numbers Below Main Diagonal")
   print("3. Display Boundary Elements")
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
             

       case 2:


       case 3:


       case _: