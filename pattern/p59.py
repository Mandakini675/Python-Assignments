n= int(input("enter number: "))
i=1
while i<=n:
   
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1
    k=1
    while k<=i:
        if i==k or k==1 or i==n:
            print("X",end="")
        else:
             print(" ",end="")
        k+=1
    i+=1
    print()
 

# enter number: 5
#     X
#    XX
#   X X
#  X  X
# XXXXX