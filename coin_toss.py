"""
Calculate the average number of tosses needed to land a coin on both sides
"""

from random import randint

trials = 100000
flips = 0

for trial in range(1, trials):
    flips += 1
    
    first_flip = randint(0, 1)

    # keep tossing until we get the different outcome
    while randint(0, 1) == first_flip:
        flips += 1
    flips += 1

print("The average number of tosses to land on both heads and tails is", flips / trials)

    
