"""
9. Neon Number LED Unlock Game
You're programming a new LED display game. The game level
 unlocks only when a neon number is entered.
A neon number is a number where the sum of the digits of 
its square is equal to the number itself.
Example: 9 → 9² = 81 → 8 + 1 = 9
Accept a number from the player.
Check whether it is a neon number using loops.
If true, display:
Glowing Success! You've found the Neon Number!
Otherwise display:
Try again! Not quite glowing yet.
Input:
9

Output:
Glowing Success! You've found the Neon Number!
"""
n= int(input("enter if it is a neon number? :"))
sqr = n**2
sum=0
for i in range(len(str(sqr))):
      d=sqr%10
      sum+=d
      sqr//=10
print("sum=",sum)
if n==sum:
    print("Glowing Success! You've found the Neon Number! ")
else:
    print("Try again! Not quite glowing yet.")