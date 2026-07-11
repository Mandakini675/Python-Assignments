n= int(input("enter number : "))
i = 1

while i<=n:
    ch=65
    j=1
    while j<=n:
        if i==1 or j==1 or i+j-1==n:
            print(chr(ch),end=" ")
        else:
            print(" ",end=" ")
        j+=1
        ch=ch+1
    i+=1
    print()
# enter number : 5
# A B C D E 
# A     D   
# A   C     
# A B       
# A     