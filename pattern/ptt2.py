# A
# AB
# ABC
# ABCD
# ABCDE

n= int(input("enter n ="))
char = 'A'
i=1
while i<=n:
    char = 'A'
   
    j=1
    while j<=i:
        print(char,end="")
        
        char= chr(ord(char) + 1)
        j+=1
    i+=1
    print()