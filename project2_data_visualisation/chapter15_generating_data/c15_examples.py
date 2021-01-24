# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:09:36 2021

@author: barbora
"""

import matplotlib.pyplot as plt

# First matplotlib plot
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)
plt.show()


# View available styles
#plt.style.available


# Plot improved, x values included
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Add in a style value
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=34)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

# Show plot
plt.show()


# Plotting a scatter graph
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()


# Plotting a scatter graph with a series of points
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()