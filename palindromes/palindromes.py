"""Find palindromes in a dictionary file."""

import load_dictionary
# load a dictionary file
word_list = load_dictionary.load('2of4brif.txt')
# create a list to store palindromes
pali_list = []

# go through each word
for word in word_list:
    # check if it's palindrome
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

# print palindromes found
print('\nNumber of palindromes found = {}\n'.format(len(pali_list)))
print(*pali_list, sep='\n')