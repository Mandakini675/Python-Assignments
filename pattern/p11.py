n= int(input("enter number = "))

i=1
while i<=n:
    ch = 65
    j=1
    while j<=i:
        
        print( chr(ch),end="")
        j+=1
        ch = ch+1
    print()
    i+=1

# enter number = 5
# A
# AB
# ABC
# ABCD
# ABCDE