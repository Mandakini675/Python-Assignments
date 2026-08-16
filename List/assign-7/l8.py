
# 8.
# =========================================
# ALLOWED CHARACTER VALIDATOR
# =========================================

# Allowed characters are:
# A-Z, a-z, 0-9

# Store allowed characters in a Frozen Set.

# Menu:
# 1. Enter Username
# 2. Validate Username
# 3. Display Allowed Characters
# 4. Exit

# Requirements:
# - Use Frozen Set.
# - Username should contain only allowed characters.


print("=========================================")
print("      ALLOWED CHARACTER VALIDATOR")
print("=========================================")

allowed_chars = frozenset(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
)
username = ""

while True:

    print("Menu")
    print("1. Enter Username")
    print("2. Validate Username")
    print("3. Display Allowed Characters")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    match ch:

        case 1:
            user = input("enter username").lower()
            username = set(user)

        case 2:
            if username.difference(allowed_chars) == set():
                print("Valid")
            else:
                print("Not valid")

        case 3:
            print("Allowed characters:")

            for ch in allowed_chars:
                print(ch, end=" ")

            print()

        case 4:
            print("Thanks for using the Allowed Character Validator.")
            break

        case _:
            print("Invalid choice. Try again.")