print("Menu")
print("1. Add Two Matrices")
print("2. Subtract Two Matrices")
print("3. Compare Two Matrices")
print("4. Exit")
   
r1 = int(input("Enter rows for Matrix 1:"))
C1 = int(input("Enter columns for Matrix 1:"))
mat_A = []
for i in range(r1):
    row = [int(x) for x in input("enter elements of row").split()]
    mat_A.append(row)
   # Second matrix
r2 = int(input("Enter rows for Matrix 2: "))
c2 = int(input("Enter columns for Matrix 2: "))

mat_B = []

for i in range(r2):
    row = [int(x) for x in input("Enter elents of row: ").split()]
    mat_B.append(row)

   
    if  r1==r2 and c1==c2:
        addition = []
        for i in range(len(mat_A)):
            for j in range(len(row)):
                result = []
                result.append((mat_A[i][j]+mat_B[i][j]))
               
            addition.append(result)
      