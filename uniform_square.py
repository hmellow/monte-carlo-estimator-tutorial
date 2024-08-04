import random
import math
from tqdm import tqdm
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np


matplotlib.use('TkAgg')

f = lambda x : math.sqrt(1 - x**2)

fig, ax = plt.subplots()
x_data, y_data, colors = [], [], []
in_lst = []

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

x_curve = np.linspace(0, 1, 100)
y_curve = np.sqrt(1 - x_curve**2)


def animate(frame):
    # Generate random points
    ran_x = random.uniform(0, 1)
    ran_y = random.uniform(0, 1)

    # Determine color based on the function
    color = 'red' if f(ran_x) < ran_y else 'blue'
    if f(ran_x) < ran_y:
        color = 'red'
        in_lst.append(0)
    else:
        color = 'blue'

    # Append new data to the lists
    x_data.append(ran_x)
    y_data.append(ran_y)
    colors.append(color)

    # Clear the axis and plot the updated data
    ax.clear()
    plt.plot(x_curve, y_curve, color='black', linewidth=2)
    ax.scatter(x_data, y_data, c=colors, s=1)  # s=1 to make points smaller
    print(f"Approximation: {4*len(in_lst)/len(x_data)}")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)


# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=2000, interval=25, repeat=False)
plt.show()
