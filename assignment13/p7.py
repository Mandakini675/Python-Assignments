'''Alternate Digit Prime Checker
A math lab adds alternate digits from right side.
Write a program to:
- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345
Output:
Alternate Sum = 9
Not Prime
'''
import math
n = int(input("enter input number :"))
m=n
l=len(str(n))
sum=0
for i in range(1,l+1 ):
    d=n%10
    # if l%2==0:
    #    if i%2==0:
    #        sum=sum+d
    # else:
    if i%2!=0:
        sum+=d
    n//=10
print("Alternate Sum = ",sum)
if sum<=1:
    print("not prime")
else:
    i=2
    while i<=int(math.sqrt(sum)):
        if sum%i==0:
            print("not prime")
            break
        i+=1
    else:
        print("prime")
        
#--------------->
# rev=0
# sum2=0
# for i in range(1,l+1 ):
#     i=1
#     temp=m
#     while i<=l:
#         rev=rev*10+m%10
#         m//=10
#         i+=1
#     dg=rev%10
#     if i%2!=0:
#          sum2+=dg
#     temp//=10
#     rev//=10
#     print(rev)
# print("sum ==",sum2)