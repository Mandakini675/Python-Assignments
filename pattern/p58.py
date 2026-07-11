n= int(input("enter number: "))
i=1
while i<=n:
    ch=65
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1
    k=1
    while k<=i:
        print(chr(ch),end="")
        ch+=1
        k+=1
    i+=1
    print()

# enter number: 5
#     A
#    AB
#   ABC
#  ABCD
# ABCDE