# 1
# 1*
# 1*3
# 1*3*
# 1*3*5

n=5
i=1
while i<=n:
    print()
    j=1
    while j<=i:
        if j%2==0:
            print("*",end="")
        else:
            print(j,end="")
        # print("@",end="")
        j+=1
    i+=1
