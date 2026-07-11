# a
# ab
# abc
# abcd
# abcde

n= int(input("enter n ="))
char = 'a'
i=1
while i<=n:
    char = 'a'
    j=1
    while j<=i:
        print(char,end="")
        char=new_char = chr(ord(char) + 1)
        j+=1
    i+=1
    print()