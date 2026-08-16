'''
# 7. Enterprise Password Pattern Strength Analyzer

A cybersecurity company wants to validate advanced passwords.

## Conditions:

* Minimum 10 characters
* At least:

  * 1 uppercase letter
  * 1 lowercase letter
  * 1 digit
  * 1 special character
* No consecutive repeating characters
* No spaces allowed

### Input:
text
Pyth@n1234
### Outpu

text
Strong Password
### Input:
text
Paaass@12
### Output:
text
Weak Password

'''
s= input("enter =")
lower=0
upper=0
dig=0
special=0
strong=True
if len(s)>=10:
    for i in range(len(s)-1):
        if s[i]==" ":
            strong=False
            break
        if s[i]==s[i+1]:
            strong=False
            print("weak password")
            break

        if s[i].isalpha():
            if s[i].islower():
              lower=1
            elif s[i].isupper():
              upper=1
        elif s[i].isdigit():
            dig=1
        else:
           if not s[i].isalnum():
               special=1
    if upper==1 and lower==1 and dig==1 and special==1 and strong:
      print("Strong Password")     
   
else:
  print("weak password")