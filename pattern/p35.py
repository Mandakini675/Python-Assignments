
n= int(input("enter number : "))
i = 1

while i<=n:
   
    j=1
    while j<=n:
        if i==1 or j==1 or i+j-1==n:
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
        
    i+=1
    print()

# *****
# *  *
# * *
# **
# *
