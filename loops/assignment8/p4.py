'''4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407
'''
a = int(input("enter starting number = "))
b = int(input("enter ending number = "))
while a<b:
    p=len(str(a))
    temp=a
    sum=0
    while temp>0:
        d=temp%10
        if p>1:
          sum=sum+d**p
        temp//=10
    
    if a==sum:
        print(a)
    a+=1