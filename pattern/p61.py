n= int(input("enter number: "))
i=1

s=1
while i<=n:
    ch=65
    j=1
    while j<=n-i:
        print(" ",end="")
        j+=1
    k=1
    while k<=s:
        print(chr(ch),end="")
        k+=1
        ch+=1
    s+=2
    i+=1
    print()

# enter number: 5
#     A
#    ABC
#   ABCDE
#  ABCDEFG
# ABCDEFGHI