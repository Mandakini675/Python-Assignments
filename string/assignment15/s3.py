'''
3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many 
times a particular character appears in a product review.

Input: Enter product review: this product is really good
       Enter character to check: o

Output: Character 'o' occurs: 4 times
'''
s = input("Enter product review = ").lower()
val = input("Enter character to check:").lower()

occ = 0

for n in s:
    if n==val:
       occ+=1
print(f" Character '{val}' occurs: {occ} times")