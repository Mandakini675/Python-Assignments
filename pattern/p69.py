n= int(input("enter number: "))
i=0
s=1
while i<n:
    ch=65
    k=1
    while k<=i:
        print(" ",end="")
        k+=1
    j=1
    while j<=n-i:
        print(chr(ch),end="")
        j+=1
        ch+=1
    s+=2
    i+=1
    print()

# enter number: 5
# ABCDE
#  ABCD
#   ABC
#    AB
#     A