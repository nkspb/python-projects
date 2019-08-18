"""Simulate a fair coin toss.

Find out how many flips are needed on average
for a coin to land on a both a heads and a tails.
"""

from random import randint

def main():
    """Find the average number of coin tosses it takes to land coin on both sides."""
    # number of time coin lands on both sides
    heads_count = 0
    tails_count = 0

    # number of times coin landed on both sides one after the other,
    # per number of trials
    heads_tails = 0
    num_trials = 10000

    def toss_coin():
        """Toss a coin and get its side."""
        if randint(0, 1) == 0:
            return 'heads'
        return 'tails'

    for _ in range(num_trials):
        if toss_coin() == 'heads':
            heads_count = heads_count + 1
        else:
            tails_count = tails_count + 1
        if heads_count > 0 and tails_count > 0:
            # if the coin has landed on both sides
            # increase the counter and nulify attempts it took
            heads_tails = heads_tails + 1
            heads_count = 0
            tails_count = 0

    # count the average number of attempts
    average = num_trials/ heads_tails
    print(f'The average number of flips per trial is {average}')

if __name__ == "__main__":
    main()
