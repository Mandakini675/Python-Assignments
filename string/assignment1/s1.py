
'''1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback
 messages by counting how many vowels are present in the
 feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8'''

s = input("enter string = ").lower()
vowel =0
# i=1
# while i<=len(str(s)):
for n in s:
    # if n=="a" or n=="e" or n=="i" or n=="o" or n=="u":
    if n in "aeiou":
       vowel+=1
print(f"Total vowel :  {vowel}")
     