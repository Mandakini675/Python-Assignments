# ====================================================================
# QUESTION 5: LIBRARY BOOK RECORDS
# ================================
# A library maintains book information using NamedTuple.
# Fields:
# book_id, title, author, price

# Requirements:
# 1. Read N book records from the user and store them in a list of NamedTuples
# ---
# 2. Display all book details.
# ---
# 3. Find and display the most expensive book.
# ---
# 4. Search books by author name.
# ---
# 5. Calculate and display the average price of all books.
# ---
# Test Case:

# Input:
# Enter number of books: 4

# B101 Python Basics John 450
# B102 Java Programming James 550
# B103 Data Science John 700
# B104 SQL Guide Smith 300

# Enter Author Name: John

# Expected Output:
# Most Expensive Book:
# B103 Data Science John 700

# Average Book Price:
# 500.0

# Books Written By John:
# B101 Python Basics John 450
# B103 Data Science John 700


from collections import namedtuple
print("====================================================================")
print("            LIBRARY BOOK RECORDS")
print(" ==================================================================")

n = int(input("Enter number of books:"))

Library = namedtuple("books",["book_id","title","author", "price"])
books = []
for i in range(n):
    book_id = input("enter books id =")
    name = input("enter Title name = ")
    author_name = input("enter author name = ")
    price= int(input("enter price  ="))
    b = Library(book_id,name ,author_name,price)
    books.append(b)

auth = input("Enter Author Name:")
print("details :")
print("-"*20)
for x in books:
    print(*x)
print("-"*20)

expensive = books[0]
total_amount = 0
count =0
for book in books:
    if book.price > expensive.price:
        expensive = book

    total_amount += book.price

average_amount = total_amount/n
print("-"*20)
print("Most Expensive Book :")
print(*expensive)

print("Average Book Price:")
print(average_amount)

print("Books Written By ",auth,":")
for x in books:
    if x.author == auth:
        print(*x)
print("-"*20)