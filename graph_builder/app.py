"""
Build different types of graphs
By Nikolay Komolov
https://github.com/nkspb
"""
from matplotlib import pyplot as plt

# Define functions for building different graphs
def build_basic_plot():
    # Ask user to enter x and y coords
    x_points = input("Please enter a comma-seperated list of x points: ")
    y_points = input("Please enter a comma-seperated list of y points: ")
    x_points = x_points.split(',')
    y_points = y_points.split(',')

    # Build a graph
    plt.plot(x_points, y_points)

# Main loop
while True:
    print("""
        1) Basic plot
    """)
    user_input = int(input("Which graph do you want to build? "))
    if user_input == 1:
        build_basic_plot()

    plt.show()








