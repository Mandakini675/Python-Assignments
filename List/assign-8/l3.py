
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


n1 = int(input("how many elements you want state in A here: "))
A = [int(x) for x in input("enter the elemnts here for A :").split()]
n2 = int(input("how many elements you want state in B here: "))
B = [int(x) for x in input("enter the elemnts here for B :").split()]
n3 = int(input("how many elements you want state  in C here: "))
C = [int(x) for x in input("enter the elemnts here for C :").split()]
new = []
i =0
while i<n1:#first loop
    curr = A[i]
    for j in range(n2): #second loop
        curr2 = B[j]
        if curr == curr2:

            for k in range(n3):#third loop
                if curr2 == C[k]:
                  if curr2 not in new:
                    new.append(curr2)
                    break
    i += 1
print(new)
