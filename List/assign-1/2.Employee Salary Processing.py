'''
2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []
'''
l=[]
n=int(input("enter the no of employee: "))
new_list=[]
for i in range(n):
    sal=(int(input()))
    l.append(sal)

for i in range(n):
    if l[i]>15000:
       new_list.append()
if len(new_list)==0:
    print("Remmaining list =[]")
else:
  sum=0
  for i in range(len(l)):
    sum+=l[i]
  av=sum//n
  print("average =",av,end=",")
  for i in l:
    if i>av:
       print("Above average =",i)
