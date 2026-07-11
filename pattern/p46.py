n=int(input("enter numbr: "))
i = n
while i>0:
    
    j=1
    while j<i:
        print(" ",end="")
        j+=1
    k=1
    while k<=n-i+1:
        if i==1 or k==1 or i+k-1==n:
           print("1",end="")
        else:
           print(" ",end="")
        k+=1
    i-=1
    print()

# enter numbr: 5
#     1
#    11
#   1 1
#  1  1
# 11111