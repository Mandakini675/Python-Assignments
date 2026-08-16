
# 6.

# =========================================
# COMMON CHARACTER FINDER
# =========================================

# Enter two strings and find common characters.

# Menu:
# 1. Enter First String
# 2. Enter Second String
# 3. Display Common Characters
# 4. Count Common Characters
# 5. Exit

# Example:
# String1: python
# String2: typhoon

# Output:
# {p, t, h, o, n}


print("=========================================")
print("        COMMON CHARACTER FINDER")
print("=========================================")

str1 = set()
str2 = set()

while True:

    print("Menu")
    print("1. Enter First String")
    print("2. Enter Second String")
    print("3. Display Common Characters")
    print("4. Count Common Characters")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    match ch:

        case 1:
            print("="*30)
            s = input("enter first string :")
            str1 = set(s)
            print("="*30)
        case 2:
            print("="*30)
            s = input("enter second string :")
            str2 = set(s)
            print("="*30)
        case 3:
            print(str1.intersection(str2))

        case 4:
            print(len(str1.intersection(str2)))

        case 5:
            print("Thanks for using the Common Character Finder.")
            break

        case _:
            print("Invalid choice. Try again.")