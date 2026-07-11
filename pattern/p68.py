n= int(input("enter number: "))
i=1
s=1
while i<=n:
   
    k=1
    while k<=i:
        print(" ",end="")
        k+=1
    j=1
    while j<=n+n-s:
        print("*",end="")
        j+=1
    s+=2
    i+=1
    print()

# enter number: 5
#  *********
#   *******
#    *****
#     ***
#      *