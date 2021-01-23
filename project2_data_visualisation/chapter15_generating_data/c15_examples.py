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


# Plot improved
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=34)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

# Show plot
plt.show()