
# 3.
# =========================================
# WEBSITE VISITOR TRACKING SYSTEM
# =========================================

# A website stores unique visitor IDs.

# Menu:
# 1. Add Visitor
# 2. Remove Visitor
# 3. Check Visitor
# 4. Display All Visitors
# 5. Count Unique Visitors
# 6. Clear Visitor Data
# 7. Exit

# Requirements:
# - Use a set to store visitor IDs.
# - Duplicate visitor IDs should not be stored.
# - Use add(), remove(), and membership operations.

print("=" * 41)
print("      WEBSITE VISITOR TRACKING SYSTEM")
print("=" * 41)

visitors = set()

while True:

    print("Menu")
    print("1. Add Visitor")
    print("2. Remove Visitor")
    print("3. Check Visitor")
    print("4. Display All Visitors")
    print("5. Count Unique Visitors")
    print("6. Clear Visitor Data")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    match ch:

        case 1:
            visitor = input("Enter visitor ID: ")
            visitors.add(visitor)

        case 2:
            visitor = input("Enter visitor ID to remove: ")

            if visitor in visitors:
                visitors.remove(visitor)
            else:
                print("Visitor not found.")

        case 3:
            visitor = input("Enter visitor ID to check: ")

            if visitor in visitors:
                print("Visitor exists.")
            else:
                print("Visitor not found.")

        case 4:
            print("All visitors:")

            for visitor in visitors:
                print(visitor)

        case 5:
            print("Total unique visitors:", len(visitors))

        case 6:
            visitors.clear()
            print("Visitor data cleared.")

        case 7:
            print("Thank you.")
            break

        case _:
            print("Invalid choice.")