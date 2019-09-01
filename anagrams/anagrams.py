"""Find anagrams for a given word."""

from collections import Counter
import load_dictionary

# Load dictionary file
word_list = load_dictionary.load('dict.txt')

# Create a list to store anagrams
anagrams = []
# Accept a word from user
user_word = input('Enter a word: ').lower()

# Go through each word in dictionary
for word in word_list:
    word = word.lower()
    # Skip same word as user supplied
    if word != user_word:
        if Counter(word) == Counter(user_word):
            # Append word to anagrams list
            anagrams.append(word)
# Print anagrams list
if len(anagrams) == 0:
    print('No anagrams found')
else:
    print('Anagrams = ', *anagrams, sep='\n')