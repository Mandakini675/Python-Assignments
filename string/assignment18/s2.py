'''2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input:


Python is powerful


Output:


lufrewop si nohtyP'''

# rev=""
# s=input("enter string: ")
# for c in s:
#     rev=c+rev
# print(rev)

rev=""
s=input("enter string: ")
ans=""
w = s.split()
for ch in w:
    for c in ch:
        rev=c+rev
    ans=rev+" "+ans
    rev=""
print(ans)


