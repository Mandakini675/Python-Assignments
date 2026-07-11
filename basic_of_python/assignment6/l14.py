"""---------------
14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
 Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000
-----------------"""
course = input("Enter course category:")
typ = input("Enter user type: Student,working,others==")
fee=0
if course=="programming":
     if typ=="student": 
          dis = 5000*(20/100)
          fee=5000-dis
     elif typ=="working":
          dis = 5000*(10/100)
          fee=5000-dis
     else:
          dis = 0
          fee=5000-dis
elif course=="design":
     if typ=="student": 
          dis = 4000*(20/100)
          fee=4000-dis
     elif typ=="working":
          dis = 4000*(10/100)
          fee=4000-dis
     else:
          dis = 0
          fee=5000-dis
elif course == "marketing":
     if typ=="student": 
          dis = 3000*(20/100)
          fee=3000-dis
     elif typ=="working":
          dis = 3000*(10/100)
          fee=3000-dis
     else:
          dis = 0
          fee=5000-dis

print("Final course fee:₹",fee)
