'''
# 2. AI Auto-Correct Consecutive Word Remover

An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

### Input:

text
hello hello hello team meeting meeting started


### Output:

text
hello team meeting started

'''

s=input("enter sentence=")
word=s.split()
orignal =""
for i in range(len(word)):
    if word[i]!=word[i-1]:
           
        orignal+=word[i]+" "
    
print(orignal)