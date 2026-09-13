'''
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website
'''
s=input("Enter Website: ")
if s[:4]=="www." and s[-4:]==".com":
    print("valid website")
else:
    print("not valid")