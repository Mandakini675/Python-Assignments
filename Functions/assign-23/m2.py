# 2.
# NUMBER ANALYSIS SYSTEM
# Scenario:
# A software company wants to develop a Number Analysis System. The application should be menu-driven and perform different mathematical operations on a given number.

# MENU
# 1. Check Perfect Number
# 2. Check Prime Number
# 3. Find Reverse of a Number
# 4. Calculate Factorial
# 5. Display Factors of a Number
# 6. Exit

# Requirements

# Choice 1 – Check Perfect Number

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return True if the number is Perfect, otherwise False.
# * Display an appropriate message based on the returned value.

# Choice 2 – Check Prime Number

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return a message such as "Prime Number" or "Not a Prime Number".
# * Display the returned message.

# Choice 3 – Find Reverse of a Number

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return the reversed number.
# * Display the returned value.

# Choice 4 – Calculate Factorial

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return the factorial value.
# * Display the returned value.

# Choice 5 – Display Factors of a Number

# * Accept a number from the user.
# * Pass the number to a function.
# * The function should return all factors of the given number.
# * Display the returned factors.

# Choice 6 – Exit

# Sample Output

# Enter Choice : 1

# Enter Number : 28

# 28 is a Perfect Number

# ---

# Enter Choice : 2

# Enter Number : 17

# Prime Number

# ---

# Enter Choice : 3

# Enter Number : 1234

# Reverse Number : 4321

# ---

# Enter Choice : 4

# Enter Number : 5

# Factorial : 120

# ---

# Enter Choice : 5

# Enter Number : 12

# Factors : 1 2 3 4 6 12

# ---

# Important Instructions

# 1. Create separate functions for each operation.
# 2. Use parameters to pass values to functions.
# 3. Use return statements appropriately.
# 4. Different functions should return different types of values such as Boolean, String, Integer, and Collection/List.
# 5. Avoid using global variables.
# 6. Implement the solution using a menu-driven approach.
# 7. Write meaningful function names and maintain proper code readability.

import math
print("=========================================")
print("          NUMBER ANALYSIS SYSTEM")
print("=========================================")

def perfect(a):
    total=0
    for i in range(1,a//2+1):
        if a%i==0:
            total+=i
    if total == a:
        print(f"{a} is a Perfect Number")
    else:
        print("False")

def prime(a):
    if a>1:
        i = 2
        while i<=math.sqrt(a):
            if a%i==0:
                print("NOT Prime Number")
                break
            i+=1
        else:
            print("Prime Number")

def reverse(num):
    rev =0
    while num>0:
        rev=rev*10+num%10
        num//=10
    print("Reverse Number :",rev)
        
def factorial(num):
    fact =1
    while num>0:
        fact*=num
        num-=1
    print("Factorial :",fact)

def factor(numb):
    factors = []
    for i in range(1,numb+1):
        if numb%i==0:
            factors.append(i)
    print(*factors)
while True:
    print("\n--------------- MENU ----------------")
    print("1. Check Perfect Number")
    print("2. Check Prime Number")
    print("3. Find Reverse of a Number")
    print("4. Calculate Factorial")
    print("5. Display Factors of a Number")
    print("6. Exit")
    print("-------------------------------------")

    choice = int(input("Enter Choice : "))

    match choice:

        case 1:
            print("\n========== PERFECT NUMBER ==========")
            num = int(input("Enter Number : "))
            perfect(num)
            print("====================================")

        case 2:
            print("\n========== PRIME NUMBER ===========")
            num = int(input("Enter Number : "))
            prime(num)
            print("===================================")

        case 3:
            print("\n========== REVERSE NUMBER =========")
            num = int(input("Enter Number : "))
            reverse(num)
            print("===================================")

        case 4:
            print("\n============ FACTORIAL ============")
            num = int(input("Enter Number : "))
            factorial(num)
            print("===================================")

        case 5:
            print("\n============= FACTORS =============")
            num = int(input("Enter Number : "))
            factor(num)
            print("===================================")

        case 6:
            print("\nThank You. Program Terminated.")
            break

        case _:
            print("\nInvalid Choice! Please try again.")