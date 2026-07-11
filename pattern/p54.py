n= int(input("enter number :"))
i=n
while i>0:
    ch=65
    j=n
    while j>i:
        print(".",end="")
        j-=1

    k=1
    while k<=i:
        print(chr(ch),end="")
        ch+=1
        k+=1
    i-=1
    print()

# enter number :5
# ABCDE
# .ABCD
# ..ABC
# ...AB
# ....A