n= int(input("enter number :"))
s=1
i=1
while i<=n:
    k=1
    while k<=i:
        print(" ",end="")
        k+=1
    j=1
    while j<=n+n-s:
        if j==1 or i==1 or j==n+n-s:
            print(j,end="")
        else:
            print("+",end="")
        j+=1
    s+=2
    i+=1
    print()

# enter number :5
#  123456789
#   1+++++7
#    1+++5
#     1+3
#      1