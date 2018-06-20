user_input = input("Enter some text: ")
result = user_input

replacements = {
    'a' : '4',
    'b' : '8',
    'e' : '3',
    'l' : '1',
    'o' : '0',
    's' : '5',
    't' : '7'
}

for i, val in replacements.items():
    result = result.replace(i, val)

print("Result: {}".format(result))