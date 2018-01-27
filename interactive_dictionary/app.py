""" Interactive Dictionary
Enter an English word and get its definition.
By Nikolay Komolov
https://github.com/nkspb
"""

# Dictionary is stored in json file, 
# so we need to import the json library
import json
from difflib import get_close_matches # function which finds similar strings

# Load dictionary into memory and convert it to Python dictionary
data = json.load(open('data.json'))

def translate(word):
	""" Look for definition for word in the dictionary
	and return the result """
	# First checking the most probable scenario that the word is in the dictionary
	if word in data:
		return data[word]
	# If word not found, check if there are similar ones
	elif len(get_close_matches(word, data, cutoff=0.8)) > 0:
		# if similar words found, use the first one, 
		# because they are ordered according to cutoff
		close_match = get_close_matches(word, data, cutoff=0.8)[0]
		correct = input("Word not found. Did you mean %s? y/n " % close_match)
		if correct.lower() == "y":
			return data[close_match]
		else:
			return "Word not found. Please double-check it :)"
	else:
		return "Word not found. Please double-check it :)"

# Ask user for word
word = input("Please enter a word: ")

output = translate(word)

# Determine type of output for correct format
if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)




