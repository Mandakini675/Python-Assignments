"""-----------------------
1. Insurance Claim Approval System

An insurance company processes claims based on policy age, claim amount, and accident type. The approval depends on multiple levels of verification to reduce fraud.

If the policy age is at least 2 years, then check the claim amount. If the claim amount is up to 50000, then check the accident type. If it is minor, approve the claim; otherwise, approve it with inspection. If the claim amount is between 50001 and 200000, then check the accident type. If it is major, approve with investigation; otherwise reject. If the claim amount exceeds 200000, reject. If the policy age is less than 2 years, then check accident type. If minor, reject; otherwise mark as pending review.

Input:
Policy Age = 3
Claim Amount = 120000
Accident Type = major

Output:
Claim Status = Approved with Investigation
----------------------"""
age = int(input("enter  policy age:"))
amount = int(input("claim amount:"))
acctype= input("type accident major or minor")
if age>=2:
      if amount<=50000:
           if acctype =="minor":
                status="approved"
           else:
               status = "approve with inspection"
      elif amount>50000 and amount<200000:
             if acctype =="major":
                status="approved with investigetion"
             else:
               status = "rejected"
      elif amount>200000:
               status = "rejected"
else:
       if age<2:
            if acctype =="minor":
                status="rejected"
            else:
                status = "pending rewiew"
print("Claim Status = ",status)

                  