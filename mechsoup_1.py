"""
Submit login form using mechanicalsoup and test whether login data was correct.
"""


import mechanicalsoup

my_browser = mechanicalsoup.Browser()
login_page = my_browser.get("https://realpython.com/practice/login.php")
login_html = login_page.soup

# Fill in form data
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# Submit the form
profiles_page = my_browser.submit(form, login_page.url)

# Get the title of the page to make sure it's profiles page
title = profiles_page.soup.title.text
print("Title is: " + title)

# Go back to login page
page = my_browser.get("https://realpython.com/practice/login.php")
page_html = page.soup

# Fill in form data
form = page_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# Submit the form
page = my_browser.submit(form, page.url)

# Check that username/pass are correct
result = page.soup.text.find("Wrong username or password")
if result != -1:
    print("Wrong username or password")
else:
    print("Login successful")

