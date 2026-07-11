n= int(input("enter number : "))
i = 1
k=n
while i<=n:
   
    j=1
    while j<=n:
        if i==1 or j==1 or i+j-1==n:
            print(k,end="")
        else:
            print(" ",end="")
        j+=1
    k-=1    
    i+=1
    print()

# 55555
# 4  4 
# 3 3  
# 22   
# 1 