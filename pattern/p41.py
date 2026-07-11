n= int(input("enter number :"))
ch=65
alp = 1
i=1
while i<=n:
    j=1
    while j<=alp:
        print(chr(ch),end="")
        ch+=1
        j+=1
    alp +=2
    print()
    i+=1

# A
# BCD
# EFGHI
# JKLMNOP
