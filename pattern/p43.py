n= int(input("enter number :"))
i = 1
while i<=n:
    j=n
    while j>i:
        print(" ",end="")
        j-=1
    
    k=1
    while k<=i:
       print(i,end="")
       k+=1
    i+=1
    print()


#     1
#    22
#   333
#  4444
# 55555
