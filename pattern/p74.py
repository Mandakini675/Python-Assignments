n= int(input("enter number :"))
s=1
i=1
while i<=n:
    k=1
    while k<=i:
        print("X",end="")
        k+=1
    i+=1
    print()
p=n
while p>0:
    k=1
    while k<p:
        print("X",end="")
        k+=1
    p-=1
    print()

# X
# XX
# XXX
# XXXX
# XXX
# X