'''
# 3. Secure Banking Transaction Analyzer

A banking server generates encrypted transaction IDs using letters and digits.

The fraud detection team wants a Python program to find the first digit that does not repeat in the transaction ID.

If no unique digit exists, print:

text
No unique digit found


### Input:

text
A122334455667789


### Output:

text
8
'''
s=input("enter string:")
uniq=""
for ch in s:
    if ch.isalpha():
        continue

    count=0
    if ch in uniq:
        continue
    uniq+=ch
    for c in s:
        if c==ch:
            count+=1
    
    if count==1:
       print(ch)
       break
else:
    print("no unique digit found")
        