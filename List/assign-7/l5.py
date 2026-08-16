
# 5.
# =========================================
# LIBRARY ISBN MANAGER
# =========================================

# A library stores unique ISBN numbers of books.

# Menu:
# 1. Add ISBN
# 2. Remove ISBN
# 3. Search ISBN
# 4. Display ISBN List
# 5. Count Books
# 6. Exit

# Requirements:
# - Use Set.
# - Duplicate ISBNs are not allowed.

print("=========================================")
print("         LIBRARY ISBN MANAGER")
print("=========================================")

isbn_set = set()

while True:

    print("Menu")
    print("1. Add ISBN")
    print("2. Remove ISBN")
    print("3. Search ISBN")
    print("4. Display ISBN List")
    print("5. Count Books")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    match ch:

        case 1:
            isbn = input("enter the next isbn book:")
            isbn_set.add(isbn)

        case 2:
            isbn = input("enter nameof isbn book to remove:")
            if isbn in isbn_set:
               isbn_set.remove(isbn)
               print("Removed successfully")
            else:
                print("No data found")

        case 3:
            isbn = input("enter nameof isbn book to search:")
            if isbn in isbn_set:  
               print("found")
            else:
                print("No data found")


        case 4:
            print("List of ISBN  :")
            for b in isbn_set:
                print(b)

        case 5:
            print("Total books ",len(isbn_set))

        case 6:
            print("Thanks for using the Library ISBN Manager.")
            break

        case _:
            print("Invalid choice. Try again.")