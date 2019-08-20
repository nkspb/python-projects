"""Simulate election.

Simulate election between three states
and two candidates.

2019 By Nikolay Komolov
https://www.github.com/nkspb
"""

from random import random

def main():
    """Simulate voting in three states."""
    # number of votes in each state
    num_trials = 10000
    # number of times candidate A wins
    won_a = 0

    def elect(probability):
        """Determine if candidate was elected.

        Depends on expected voting results.
        """
        if random() < probability:
            return True
        return False

    # candidate A chances of winning in the three states
    region1_prob_a = .87
    region2_prob_a = .65
    region3_prob_a = .17

    # vote a specified number of times
    for _ in range(num_trials):
        # determine voting results for candidate A
        region1_results_a = elect(region1_prob_a)
        region2_results_a = elect(region2_prob_a)
        region3_results_a = elect(region3_prob_a)

        # if candidate A wins in at least two states, they win the election
        if ((region1_results_a and region2_results_a) or
                (region1_results_a and region3_results_a) or
                (region2_results_a and region3_results_a)):
            # increase total of candidate A wins
            won_a = won_a + 1

    # determine percentage of candidate A wins
    chances_a = (won_a / num_trials) * 100
    # the rest from 100 goes for another candidate
    chances_b = 100 - chances_a

    print(f'Candidate A chances to win are {chances_a}%')
    print(f'Canditate B chances to win are {chances_b}%')

if __name__ == '__main__':
    main()
