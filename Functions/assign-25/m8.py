
# 4.
# Assignment 10: Cyber Security (Strong Password Check)

# A cybersecurity company considers a numeric password to be "strong" if every digit is even.

# Task

# Write a recursive function to check whether all digits of the given number are even.

# Input 1
# Enter Password:
# 248620
# Output 1
# Strong Password
# Input 2
# Enter Password:
# 248621
# Output 2
# Weak Password
# i=0
def strongpass(passw,i):
    if i==len(passw):
        return True
    if int(passw[i])%2!=0:
         return False
    return strongpass(passw,i+1)


num=input("enterr")
if strongpass(num,0)==True:
    print("Strong Password")
else:
    print("Weak Password")
# 5.
#  Hospital Record System (Search Digit)


# A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.

# Task

# Write a recursive function to determine whether a given digit is present.

# Input
# Enter Patient ID:
# 5837264

# Enter Digit:
# 7
# Output
# Digit Found
def found(number,dig,i):
    if i == len(number):
        return False
    if number[i]==dig:
        return True
    return found(number,dig,i+1)

numb = input("enter ::")
digit = input("digit:")

if found(numb,digit,0)==True:
    print("Digit Found")
else:
    print("Not found")