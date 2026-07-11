n = int(input("Enter number: "))
i = 1
while i <= n:
    j = 1

    while j <= i:
        if i == n or j == 1 or j == i:
            print(i, end=" ")
        
        else:
            print(" ", end=" ")
        j += 1

    print()
    i+= 1 
    
# Enter number: 5
# 1 
# 2 2 
# 3   3 
# 4     4 
# 5 5 5 5 5 