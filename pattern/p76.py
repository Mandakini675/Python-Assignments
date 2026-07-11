n= int(input("enter number :"))
s=1
i=1
while i<=n:
    
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1
   #spaces
   
    k=1
    while k<=i:
        print(k,end="")
        k+=1
    i+=1
    print()
r=1
p=n
while p>0:
    j=1
    while j<=r:
        print(" ",end="")
        j+=1
    k=1
    while k<p:
        print(k,end="")
        k+=1
    r+=1
    p-=1
    print()

# enter number :5
#     1
#    12
#   123
#  1234
# 12345
#  1234
#   123
#    12
#     1