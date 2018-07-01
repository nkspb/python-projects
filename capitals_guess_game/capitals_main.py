"""
    Simple guessing game
"""

from capitals import capitals_dict
import random

def capitals_game():
    exit_game = False
    
    while True:
        if exit_game:
            quit()
        print("Guess the capital. Type Exit to quit")
        # Get random state/capital pair
        state, capital = random.choice(list(capitals_dict.items()))
        guess = input("What's the capital of {} is? ".format(state)).lower()
        while True:
            if guess == "exit":
                print("The capital of {} is {}.".format(state, capital))
                print("Goodbye!")
                exit_game = True
                break
            # If player guesses correctly, ask for the next capital
            if guess == capital.lower():
                print("Congratulations!")
                break
            else:
                guess = input("Try again: ")
                                   
