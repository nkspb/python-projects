"""
Find and display each user's highest score taken from a csv file
"""
import os, csv
# This dictionary will contain the results
highest_scores = {}

# Read csv file with scores
with open('scores.csv') as scores_file:
    csv_reader = csv.reader(scores_file)
    # Itterate through each row in csv
    for user, score in csv_reader:
        # We need convert score to int for comparisons
        # Otherwise, it will be compared lexically and not arithmetically
        score = int(score)
        # If no key for a user exists, create it
        if user not in highest_scores:
            highest_scores[user] = score
        # If a key for the user exists, compare its value
        else:
            if score > highest_scores[user]:
                # And update if needed
                highest_scores[user] = score

# Display the results
for key, value in sorted(highest_scores.items()):
    print("{} : {}".format(key, value))
