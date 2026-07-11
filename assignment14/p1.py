"""1. Utility Toolkit System
You are developing a Utility Toolkit Application for a small office.
 Employees use this tool to quickly perform common number operations like 
checking prime numbers, reversing numbers, etc.

The system should be menu-driven and must continue running until 
the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Check Prime Number
2 → Check Palindrome Number
3 → Reverse a Number
4 → Count Digits
5 → Exit

Sample Run 1:
Input:
Enter your choice: 1
Enter number: 7

Output:
7 is a Prime Number

Sample Run 2:
Input:
Enter your choice: 2
Enter number: 121

Output:
121 is a Palindrome Number

Sample Run 3:
Input:
Enter your choice: 3
Enter number: 456

Output:
Reversed Number is: 654

Sample Run 4:
Input:
Enter your choice: 4
Enter number: 98765

Output:
Total digits: 5

Sample Run 5 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

Sample Run 6 (Exit):
Input:
Enter your choice: 5

Output:
Exiting program... Thank you!

Requirements:

* Use while loop to repeat menu
* Use match-case for decision making
* Handle negative numbers properly
* Use only loops and conditions
"""

# Menu Options:
# 1 → Check Prime Number
# 2 → Check Palindrome Number
# 3 → Reverse a Number
# 4 → Count Digits
# 5 → Exit

import math
while True:
    print("-----------.^.--------------")
    print(" 1 → Check Prime Number")
    print(" 2 → Check Palindrome Number")
    print(" 3 → Reverse a Number")
    print(" 4 → Count Digits")
    print(" 5 → Exit") 
    print("-----------...--------------")
    opt = int(input("what would you choose :"))
    match opt:
        case 1:
            a=int(input("enter the number to check:"))
            if a<=1:
                print(f"{a} is not prime")
            i=2
            while i<=int(math.sqrt(a)):
                if a%i==0:
                    print(f"{a} is not prime")
                    break
                i=i+1
            else:
                print(f"{a} is a Prime number ")
                   
        case 2:
            n=input("enter number:")
            rev=""
            for i in n:
               rev = i+rev
            if rev==n:
                 print(f" {n} is a palindrome")
            else:
                 print("not")
        case 3:
            n = int(input("enter numbers:"))
            rev=0
            for i in range(len(str(n))):
                 rev=rev*10+n%10
                 n=n//10
            print(f"reverse = {rev}")

        case 4:
            # n = int(input("enter numbers:"))
            # count=0
            # for i in n:
            #     count+=1
            # print(f"count= {count}")

            n = int( input("enter numbers:"))
            count=0
            while n>0:
               d=n%10
               count+=1
               n//=10
            print(f"{count} is a count")
         
        case 5:
            print("exit.........")
            break
        case __:
            print("Invalid choice. Please try again.")
        
print("thanks for using the menu ")