n= int(input("enter number :"))
i=1

while i<=n:
    ch=97
    j=1
    while j<=i:
        if i==n or j==1 or i==j:
            print(chr(ch),end="")
        else:
            print(" ",end="")
        ch=ch+1
        j+=1
    
    i+=1
    print()

# enter number :5
# a
# ab
# a c
# a  d
# abcde