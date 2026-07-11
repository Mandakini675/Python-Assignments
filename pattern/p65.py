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
        if k==1 or i==n or k==s:  #😢
            print("1",end="")
        else:
             print("*",end="")
        k+=1
    s+=2
    i+=1
    print()

# enter number: 6
#      1
#     1*1
#    1***1
#   1*****1
#  1*******1
# 11111111111