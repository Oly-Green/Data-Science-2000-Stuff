# import libraries for making the graph and generating a list
from matplotlib import pyplot as plt
import numpy as np

# defining the collatz function so it returns the number of steps it took to get to one based off of the starting number
def collatz(x):
    steps = 0

    while x != 1:
        if x % 2 == 1:
            x = 3 * x + 1
        else:
            x = x // 2

        steps = steps + 1
    return steps

# getting user inputs for the range and explaing the program
print('This program will plot how many steps it takes for the Collatz function to get to 1 over the range you select.\n')
initial = int(input('Where would you like the range to begin? \n'))
final = int(input('Where would you like the range to end? \n')) + 1

# defining the lists fors the x and y plots of the graph
x_pos = np.arange(initial, final).tolist()
y_pos = []

# performing the collatz function on each member of the x_pos list
# then appending the reults to the y_pos list to create a new list with all the function returns
a = 0
while a < len(x_pos):
    y_pos.append(collatz(x_pos[a]))
    a += 1

# using the mathplotlib to plot these lists and make them look nice and pretty
plt.plot(x_pos ,y_pos, '.r', markersize=2)
plt.xlabel("Initial Value")
plt.ylabel("Steps to 1")
plt.title('Collatz')
plt.show()
