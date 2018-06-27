"""
Simulate an election between two candidates
"""

from random import random

total_A_wins = 0
total_B_wins = 0

# Probability that candidate A will win in each region
prob_A_reg_1 = 0.87
prob_A_reg_2 = 0.65
prob_A_reg_3 = 0.17

# Number of elections
trials = 100000

for trial in range(0, trials):
    # Number of regions in which a candidate wins
    A_wins = 0
    B_wins = 0
    # 1st region
    if random() < prob_A_reg_1:
        A_wins += 1
    else:
        B_wins += 1
    # 2nd region
    if random() < prob_A_reg_2:
        A_wins += 1
    else:
        B_wins += 1
    # 3d region
    if random() < prob_A_reg_3:
        A_wins += 1
    else:
        B_wins += 1
    # Determine who won an election
    # and add to total number of wins
    if A_wins > B_wins:
        total_A_wins += 1
    else:
        total_B_wins += 1

print("The probability of A winning an election is", total_A_wins / trials)
print("The probability of B winning an election is", total_B_wins / trials)
        
        
    
