n= int(input("enter number : "))
i = 1

while i<=n:
    ch=65
    j=n
    while i<=j:
        print(chr(ch),end="")
        j-=1
        ch=ch+1
    i+=1
    print()

# ABCDE
# ABCD
# ABC
# AB
# A