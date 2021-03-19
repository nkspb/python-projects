# Email Slicer

import re

# Load list of emails from a file
emails_file = open('emails.txt', 'r')
emails = emails_file.readlines()

target_file = open("emails_data.txt", "w")

# Go through each string and extract username and domain
for email in emails:
    username = re.search('.*(?=\@)', email).group(0)
    domain = re.search('(?<=@).*', email).group(0)
    email_array = [username, domain]
    target_file.write(" ".join(email_array) + "\n")

target_file.close()
