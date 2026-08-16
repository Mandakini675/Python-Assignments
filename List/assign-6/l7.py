
# 7.

# A cricket academy wants to analyze player performance. 
# Each player's information is stored as a tuple.

# Tuple Format:

# (player_id, player_name, runs_scored)

# Requirements:

# Read N player records from the user and store them as tuples in a list.
# Display all player records.
# Find and display the player who scored the highest runs.
# Find and display the player who scored the lowest runs.
# Calculate and display the total runs scored by all players.
# Calculate and display the average runs scored.
# Display players who scored more than 50 runs.

# Test Case:
# Input:
# Enter number of players: 5
# 101 Virat 82
# 102 Rohit 45
# 103 Gill 120
# 104 Hardik 38
# 105 SKY 76

# Expected Output:

# All Players:
# (101, 'Virat', 82)
# (102, 'Rohit', 45)
# (103, 'Gill', 120)
# (104, 'Hardik', 38)
# (105, 'SKY', 76)

# Highest Scorer:
# (103, 'Gill', 120)

# Lowest Scorer:
# (104, 'Hardik', 38)

# Total Runs:
# 361

# Average Runs:
# 72.2

# Players Scoring More Than 50 Runs:
# (101, 'Virat', 82)
# (103, 'Gill', 120)
# (105, 'SKY', 76)


n = int(input("enter no of team -----"))
members = []
for i in range(n):
    player_id = input("enter the player id =")
    player_name = input("enter the player name =")
    runs_scored = int(input("enter the total amount so far ="))
    m = (player_id, player_name, runs_scored)
    members.append(m)

print("details:")
print("-"*30)
for x in members:
    print(*x)
print("-"*30)

team_mem_f = members[i]
team_mem_l = members[i]
total_runs =0
highest_score = members[0][2]
least = members[0][2]
for i in range(n):
    score = members[i][2]

    if score >= highest_score:
        highest_score = score
        team_mem_f = members[i]
    if score <= least:
        least = score
        team_mem_l = members[i]

    total_runs += score

average = total_runs/n
print("="*30)
print("Highest scorer :")
print(team_mem_f)

print("least scorer :")
print(team_mem_l)

print("Total runs :")
print(total_runs)
print("Average runs:")
print(average)

print("Players Scoring More Than 50 Runs:")
for i in range(n):
    if members[i][2] >50:
        print(members[i])
print("="*30)