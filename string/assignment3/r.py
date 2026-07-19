rev=""
s=input("enter string: ")
for c in s:
    if not c.isalnum():
        continue
    rev=c+rev
new=""
i=0
for c2 in s:         
    if not c2.isalnum():
         new+=c2
         continue
    new+=rev[i]
    i+=1
print(new)