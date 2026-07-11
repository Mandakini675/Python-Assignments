n= int(input("enter number: "))
i=0
s=1
m=n
while i<n:
   
    k=1
    while k<=i:
        print(" ",end="")
        k+=1
    j=1
    while j<=n-i:
        print(m,end="")
        j+=1
    m-=1
    s+=2
    i+=1
    print()

# enter number: 5
# 55555
#  4444
#   333
#    22
#     1