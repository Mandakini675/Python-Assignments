n= int(input("enter number : "))
i = 1

while i<=n:
    k=1
    j=n
    while i<=j:
        print(k,end="")
        j-=1
        k+=1
    i+=1
    print()

# 12345
# 1234
# 123
# 12
# 1