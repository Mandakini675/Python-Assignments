n=int(input("enter numbr: "))
i = n
while i>0:
    ch=65
    j=1
    while j<i:
        print(" ",end="")
        j+=1
    k=1
    while k<=n-i+1:
        if k%2!=0:
           print("1",end="")
        else:
           print("0",end="")
      
        k+=1
    i-=1
    print()

# enter numbr: 5
#     1
#    10
#   101
#  1010
# 10101