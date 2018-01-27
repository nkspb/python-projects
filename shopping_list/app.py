shopping_list = []

def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)

def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")

def save_tasks():
    with open("tasks.txt", "w") as save_file:
        for item in shopping_list:
            save_file.write(item + "\n")
    print("Saved to file")
    
def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

def load_file():
    with open('tasks.txt') as f:
        for line in f:
            shopping_list.append(line.strip())

try:
    load_file()
except:
    pass

show_help()

while True:
    new_item = input("> ")
    if new_item == "DONE":
        save_tasks()
        break
    elif new_item == "SHOW":
        show_list()
        continue
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SAVE":
        save_tasks()
        continue
        
    add_to_list(new_item)


show_list()

