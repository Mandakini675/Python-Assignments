'''

QNo 8:--
SMART TEXT PROCESSING SYSTEM

A software company is developing a Smart Text Processing System for
handling user messages. Different users require different text
transformations. To avoid creating separate applications, the company
wants a menu-driven program where users can select operations according
to their requirements.

The system should continue executing until the user selects Exit.

====================================================== MENU
======================================================

===== Smart Text Processing System =====

1.  Reverse Complete String
2.  Reverse Every Word
3.  Reverse Word Order
4.  Exit

====================================================== Choice 1 :

Conditions: - Reverse the complete string - Ignore extra spaces - Keep
special characters (@,#,$,%) in their original positions - Do not use
built-in reverse functions

Example: Input: ja@va#py

Output: yp@av#aj

Test Case 1: ab@cd#ef Output: fe@dc#ba

Test Case 2: py@th#on Output: no@ht#yp

Test Case 3: java@proOutput : orpa@vaj

====================================================== Choice 2 :

Conditions: - Reverse every word separately - Words containing digits
should not be reversed - Ignore extra spaces between words - First
letter of each reversed word should become uppercase

Example: Input: java is easy123 programming

Output: Avaj Si easy123 Gnimmargorp

Test Case 1: python full stack22 developer Output: Nohtyp Lluf stack22
Repoleved

Test Case 2: hello java99 world Output: Olleh java99 Dlrow

====================================================== Choice 3 :

Conditions: - Reverse order of words - Remove duplicate words - Ignore
case while checking duplicates - Keep only first occurrence

Example: Input: Java python Java react Python

Output: React Python Java

Test Case 1: HTML CSS HTML Java CSS Output: Java CSS HTML

Test Case 2: Python React Java Python React Output: Java React Python

====================================================== Choice 4
======================================================

Program Closed Successfully'''

print("=*30","MENU","="*30)
print("===== Smart Text Processing System =====")

print("1.  Reverse Complete String")
print("2.  Reverse Every Word")
print("3.  Reverse Word Order")
print("4.  Exit")
while True:
    ch=int(input("enter your choice:"))
    match ch:
        case 1:
           rev=""
           s=input("enter string: ")
           k=s[::-1]
        # #    print(s)
           for c in s:
              if not c.isalnum():
                continue
              rev=c+rev
           new=""
           i=0
           for c2 in s:
               if not c2.isalnum():
                   new+=c2
                   continue
               new+=rev[i]
               i+=1
           
           print(new)

        case 2:
            s=input("entr string: ")
            word=""
            ans=""
            for i in range(len(s)):
                if i==0 and s[i]==" ":
                    continue
                if s[i]==" " :
                   ans=ans+word+" "
                   word=""
                word=s[i]+word 
            ans+=word
            # ans.title()
            print("Encrypted Message=",ans.title())
        case 3:
            words = input("Enter words: ").split()
            result = []

            for word in words:
                if word.lower() not in [x.lower() for x in result]:
                    result.append(word.capitalize())            
            result.reverse()
            print(*result)
            
        case 4:
           print("Program Closed Successfully")
           break

        case _:
           print("wrong choice try again")
           continue