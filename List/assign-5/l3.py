
# 3.

# MATRIX PERFORMANCE EVALUATION SYSTEM

# A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

# The HR department wants a menu-driven application to analyze employee performance.

# Menu
# 1. Find Employee with Highest Total Score
# 2. Find Month with Lowest Average Score
# 3. Display Employee-wise Maximum Score
# 4. Exit
# Requirements
# Choice 1 – Find Employee with Highest Total Score
# Calculate the sum of each row.
# Display the employee number having the highest total score.
# Choice 2 – Find Month with Lowest Average Score
# Calculate the average of each column.
# Display the month having the lowest average score.
# Choice 3 – Display Employee-wise Maximum Score
# Find and display the maximum value present in each row.
# Sample Input
# 10 20 30
# 40 50 60
# 25 35 45
# Output
# Employee 2 has Highest Total Score = 150

# Month 1 Average = 25
# Month 2 Average = 35
# Month 3 Average = 45

# Employee 1 Max Score = 30
# Employee 2 Max Score = 60
# Employee 3 Max Score = 45
print("="*60)
print("-"*15,"MATRIX PERFORMANCE EVALUATION SYSTEM")
print("="*60)

while True:

   print("Menu")
   print("1. Find Employee with Highest Total Score")
   print("2. Find Month with Lowest Average Score")
   print("3. Display Employee-wise Maximum Score")
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
            greater=0
            for i in range(r1):             
                mon_sum =0
                for j in range(c1):
                    curr_elem = matric[i][j]
                    mon_sum += curr_elem
                if mon_sum>greater:
                    greater = mon_sum
                    
            print(f"Employee {i+1} has Highest total  score = {greater}")
       case 2:
            lowest = 99
            for j in range(c1):
                sum_clwise=0

                for i in range(r1):
                   curr_elem = matric[i][j]
                   sum_clwise += curr_elem
                av = sum_clwise//r1
                if av < lowest:
                    lowest = av
                    
                print(f"Month  {j+1} average   = {av}")
       case 3:
              
            for i in range(r1):
               greater = 0
              
               for j in range(c1):
                  curr_elem = matric[i][j]
               
               greater = curr_elem if curr_elem>greater else greater
               print(f"Employee {i+1} Max Score = {greater}")
       case _:
            print("you enterd wrong option try again")