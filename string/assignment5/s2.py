'''
2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india'''

s=input("enter sentence to check frequency=")
words=s.split()
h_cvalue=""
unique=""
high = 0
count=0

for ch in words:
    count=0
    if ch in unique:
        continue
    unique+=ch+" "
    for c in words:
        if ch==c:
           count+=1
    if count>high:
        high=count
        h_cvalue = ch


        
print(h_cvalue)