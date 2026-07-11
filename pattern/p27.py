n = int(input("Enter number: "))
i = 1
while i <= n:
    j = 1

    while j <= i:
        if i == n or j == 1 or j == i:
            if j%2==0:
               print("0", end=" ")
            else:
               print("1", end=" ")
        
        else:
            print(" ", end=" ")
        j += 1

    print()
    i+= 1 

# Enter number: 5
# 1 
# 1 0 
# 1   1 
# 1     0 
# 1 0 1 0 1 