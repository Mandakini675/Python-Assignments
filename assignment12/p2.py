'''2. Next Prime ID Generator

A multinational company auto-generates employee IDs in numeric sequence.
 Due to internal policy, only prime numbered IDs are assigned to new premium employees.

The HR manager enters the current last issued ID, and the software must search forward to find the next available prime number ID.

Write a program to find the first prime number after n.

Input:
14

Output:
Next Prime = 17
import math
n= int(input("enter code: "))
i=2
while i<=int(math.sqrt(n)):
  if n%i==0:
    continue
  i=i+1
  n=n+1     
else:
    print(f"next Prime ={n} ")
    
    '''
import math
n= int(input("enter code: "))
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