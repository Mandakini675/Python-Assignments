
# 7.
# =========================================
# MISSING ALPHABET FINDER
# =========================================

# Enter a sentence and find which
# alphabets are missing.

# Menu:
# 1. Enter Sentence
# 2. Display Missing Alphabets
# 3. Count Missing Alphabets
# 4. Exit

# Requirements:
# - Use Set containing a-z.

print("=========================================")
print("        MISSING ALPHABET FINDER")
print("=========================================")

sentence = ""
alphabets = set("abcdefghijklmnopqrstuvwxyz")

while True:

    print("Menu")
    print("1. Enter Sentence")
    print("2. Display Missing Alphabets")
    print("3. Count Missing Alphabets")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    match ch:

        case 1:
            s = input("enter the string:").lower()
            s = s.replace(" ", "")
            # s = "".join(s.split())
            sentence = set(s)
        case 2:
            if len(sentence)>0:
               print(alphabets.difference(sentence))
            else:
                print(".........enter sentenve first")
        case 3:
            if len(sentence)>0:
               print(len(alphabets.difference(sentence)))
            else:
                print("enter sentenve first")
            
        case 4:
            print("Thanks for using the Missing Alphabet Finder.")
            break

        case _:
            print("Invalid choice. Try again.")