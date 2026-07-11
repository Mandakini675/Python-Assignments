"""---------------------
Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67

---------------------------"""
run = int(input("enter total run :"))
over,ball = map(int,input("enter the overs and ball:").split("."))
total_ball = (over*6)+ball

run_rate = run/(total_ball/6)
print("Total ball = ",total_ball)
print("Run Rate = ",run_rate)
