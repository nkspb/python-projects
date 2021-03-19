"""Hangman Game. Guess a word in several attempts."""

import random
import os

words = open('words.txt').read().splitlines()
word = random.choice(words)

# convert to list so that could replace by index
# as strings are immutable
shown_word = 'X' * len(word)

print(f'Word: {shown_word}')

guesses_left = 3
guessed_letters = []

if __name__ == "__main__":
    shown_word = list(shown_word)

    while guesses_left != 0:
        letter = input('Enter a letter: ')

        if letter in word:
            # build list of indexes of letter matched
            letter_indexes = [i for i in range(len(word)) if word.startswith(letter, i)]
            # change to entered letter on indexes where the same letter is in original word
            for i in letter_indexes:
                shown_word[i] = word[i]
            print("".join(shown_word))
            if letter in guessed_letters:
                print('You already entered it')
            guessed_letters.append(letter)
        else:
            # if player got it wrong, decrease number of gueses
            guesses_left = guesses_left - 1
            if guesses_left == 0:
                print('Game over')
                break
            print(f'Be careful! Only {guesses_left} guesses left')

        if "".join(shown_word) == word:
            print('You guessed it, congrats!')
            break
