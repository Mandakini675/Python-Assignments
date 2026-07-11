n= int(input("enter number : "))
i = 1
ch=n+64
while i<=n:  
    j=n
    while i<=j:
        print(chr(ch),end="")
        j-=1
    ch=ch-1
    i+=1
    print()

# EEEEE
# DDDD
# CCC
# BB
# A