'''4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31
'''

import math
n= int(input("enter number ="))
prime=False
if n<=1:
   prime = False
else:
    i=2
    while i<=int(math.sqrt(n)):
        if n%i==0:
            break
        i+=1
    else:
        prime=True
        print("Prime number")    
'''if count>0:
    prime=False
else:
    prime=True'''

#IF TRUE THEN CHECK FOR NEXT

if prime==True:
  n=n+1
  while True:
    if n<=1:
        n+=1
        continue
    i=2
    while i<=int(math.sqrt(n)):
        if n%i==0:
          break
        i=i+1
    else:
        print(f"next Prime ={n} ")
        break   
    n=n+1
else:
    n=n-1
    while True:
      if n<=1:
        n+=1
        continue
      i=2
      while i<=int(math.sqrt(n)):
          if n%i==0:
            break
          i=i+1
      else:
          print(f"PREV Prime ={n} ")
          break   
      n=n-1