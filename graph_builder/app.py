"""
Build different types of graphs
By Nikolay Komolov
https://github.com/nkspb
"""
from matplotlib import pyplot as plt
from numpy import arange

# Define functions for building different graphs
def build_basic_plot(add_dots):
    # Ask user to enter x and y coords
    x_points = input("Please enter a comma-seperated list of x points: ")
    y_points = input("Please enter a comma-seperated list of y points: ")
    x_points = x_points.split(',')
    y_points = y_points.split(',')
    # Build a graph
    if add_dots.lower() == "y":
        plt.plot(x_points, y_points, "g-o")
    else:
        plt.plot(x_points, y_points)

def build_basic_bar():
    x_points = input("Please enter a comma-seperated range of x points: ").split(',')
    y_points = input("Please enter a comma-seperated range of y points: ").split(',')
    x_points_range = arange(int(x_points[0]), int(x_points[1])+1)
    y_points_range = arange(int(y_points[0]), int(y_points[1])+1)
    print(x_points_range)
    print(y_points_range)
    plt.bar(x_points_range, y_points_range)

# Main loop
while True:
    print("""
        1) Basic plot
        2) Basic bar
    """)
    user_input = int(input("Which graph do you want to build? "))
    if user_input == 1:
        add_dots = input("Do you want to add dots? (y/n) ")
        build_basic_plot(add_dots)
    elif user_input == 2:
        build_basic_bar()

    plt.show()








