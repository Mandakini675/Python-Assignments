"""4. E-Learning Course Access System

An online learning platform grants access based on 
subscription type, course progress, and test score.

If subscription is premium, then check progress. 
If progress is at least 80, then check test score.
 If score is at least 70, unlock certificate; otherwise allow retry. 
 If progress is less than 80,
  ask to complete course. If subscription is basic, then check progress. 
  If progress is at least 50, allow limited access; otherwise lock content.
   If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Score = 65

Output:
Access Status = Retry Test
"""
Subscription = input("enter subscription premium or basic:")
Progress = int(input("enter progress :"))
Score = int(input("enter score"))
if Subscription=="premium":
    if Progress>=80:
         if Score>=70:
            s="unlock certificate"
         else:
            s="retry test"
    else:
        s="complete course"
else:
    s="allow limited access" if Progress>=50 else "lock content"

print(s)


