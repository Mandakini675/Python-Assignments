n= int(input("enter number: "))
i=1
s=1
while i<=n:
   
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1
    k=1
    while k<=s:
        print(k,end="")
        k+=1
    s+=2
    i+=1
    print()

# enter number: 5
#     1
#    123
#   12345
#  1234567
# 123456789