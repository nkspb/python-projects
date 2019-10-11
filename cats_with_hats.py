"""
Cats with hats simulation.

There are 100 cats with no hats.
Go round the cats 100 times, increasing step by 1 each round.
If a cat has no hat - put it on, else put it off.
Print the cats with hats in the end.

github.com/nkspb.
"""

def main():
    """Get cats with hats."""
    # Create list of cats with no hats
    cats = [False] * 100

    # Step for each round
    step_incr = 1

    # Go through cats 100 times
    for _ in range(0, len(cats)):
        # On each round, go through each cat
        for j in range(0, len(cats), step_incr):
        # Invert value
            cats[j] = not cats[j]

        # Increase step for next round
        step_incr += 1

    # Contains indexes of cats with hats
    result = []

    for index, item in enumerate(cats):
        if item is True:
            result.append(index)

    print(result)

if __name__ == '__main__':
    main()
