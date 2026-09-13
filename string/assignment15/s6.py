'''6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number
'''
  
    
s=input("enter PNR :")
dig =False

if len(s)==12 and s[0]=='P' and s[1]=='N' and s[2]=='R':
    
    if  s[3: ].isdigit():
        dig=True
        print("Valid PNR Number")
    else:
        print("not Valid PNR Number")
else:
    print("not Valid PNR Number")

