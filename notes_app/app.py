"""
CLI notes app
By Nikolay Komolov
https://github.com/nkspb
"""
import sqlite3

# Connect to db
conn = sqlite3.connect('notes.db')
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Notes(ID INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT, Text TEXT)")

# Show menu
while True:
    print("""Choose an action:
    1) Add an entry
    2) View entries""")
    # Ask user to make a choice
    try:
        user_input = int(input())
    except ValueError:
        print("You should enter a number")
        continue

    # ADD ENTRY
    if user_input == 1:
        user_title = input("Enter title: ")
        user_text = input("Enter text: ")
        cur.execute("INSERT INTO Notes (Title, Text) VALUES (?, ?)", (user_title, user_text))
        conn.commit()
    # VIEW ENTRIES    
    if user_input == 2:
        # Display all entries
        cur.execute("SELECT Id, Title FROM Notes")
        # Check if there are any notes
        rows = cur.fetchall()
        if not rows:
            print("There aren't any notes. Add the first one :)")
            continue
        for row in rows:
            print("{}) {}".format(row[0], row[1]))
        # Ask user to select an entry to watch
        while True:
            try:
                # If user does enter a number, stop asking it to enter it again
                user_input = int(input("Enter entry id to read: "))
                break
            # If user doesn't enter a number, ask to enter again
            except ValueError:
                print("You should enter a number")
                continue
        
        cur.execute("SELECT Text FROM Notes WHERE Id=?", (user_input,))

        # Display notes
        not_empty = False
        for row in cur.fetchall():
            not_empty = True # Check that note with this id exists
            print(row[0])
        if not not_empty:
            print("There is no such note")     


