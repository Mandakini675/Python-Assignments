"""-----------------------
4. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test
---------------------"""
subs = input("subscription")
progress = int(input("enter progress="))
score = int(input("enter test score ="))

if subs=="premium":
     if progress>=80:
          if score>=70:
              s="unlock certificate"
          else:
              s="Retry test"
     else:
          s="complete cours!!"

elif subs=="basic":
     if progress>=50:
           s="allow limited access"
     else:
           s="lock content"
else:
      s="deny access"
print("Access Status =",s)