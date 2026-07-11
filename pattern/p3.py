n= int(input("enter number"))
j=1
for i in range(1,n+1):
  j=1
  while i>=j:
    if i==j:
       print("*")
    print(" ",end="")
    j+=1