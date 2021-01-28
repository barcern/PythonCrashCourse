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


# Collecting data automatically and playing with colours
x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # list comprehension
plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, s=10)
#ax.scatter(x_values, y_values, c='red', s=10)
ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()


# Colormaps = series of colours in a gradient
x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # list comprehension
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Set colormap here
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()


# Saving plots
x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # list comprehension
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

# Save plot here
plt.savefig('squares_plot.png', bbox_inches='tight')
