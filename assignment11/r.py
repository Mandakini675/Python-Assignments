m= int(input("enter id number:"))
l=len(str(m))
sum=0
max=0
#for reverse
n=0
while m>0:
    n=n*10+m%10
    m=m//10
print(n)
#finding adjacent diff
while n>=10:
    last=n%10
    n=n//10
    seclast = n%10
    diff = seclast-last if seclast>last else last-seclast
    seclast=last
    print(diff,end=" ")
    max = max if max > diff else diff
    sum=sum +diff

print(f"\nsum = {sum}")
print("largest difference = ",max)
if sum%l==0:
    print("Balanced Number")
else:
    print("Unbalanced Number")