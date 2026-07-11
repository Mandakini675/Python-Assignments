# 1
# 00
# 111
# 0000
# 11111
n= int(input("enter n ="))
i=1
while i<=n:
    j=1
    while j<=i:
        if i%2!=0:
            print("1",end="")
        else:
            print("0",end="")
        j+=1
    i+=1
    print()