from tkinter import *

# Create Windows
window = Tk()

# Code goes here

def convert():
    """
    Convert kg to grams, pounds and ounces, 
    and display the results.
    """
    # Convert to grams
    grams = float(entry_kg_value.get()) * 1000
    # Clear grams entry
    entry_grams.delete(0, END)
    # Update grams entry
    entry_grams.insert(END, grams)

    # Convert to pounds
    pounds = float(entry_kg_value.get()) * 2.20462;
    # Clear pounds entry
    entry_pounds.delete(0, END)
    # Update pounds entry
    entry_pounds.insert(END, pounds)

    # Convert to ounces
    ounces = float(entry_kg_value.get()) * 35.274
    # Clear ounces entry
    entry_ounces.delete(0, END)
    # Update ounces entry
    entry_ounces.insert(END, ounces)

label_1 = Label(window, text="kg")
label_1.grid(row=0, column=0)

entry_kg_value = StringVar()

entry_kg = Entry(window, textvariable=entry_kg_value)
entry_kg.grid(row=0, column=1)

button_1 = Button(window, text="Convert", command=convert)
button_1.grid(row=0, column=2)

entry_grams = Entry(window)
entry_grams.grid(row=1, column=0)

entry_pounds = Entry(window)
entry_pounds.grid(row=1, column=1)

entry_ounces = Entry(window)
entry_ounces.grid(row=1, column=2)

window.mainloop()