# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:34:48 2020

@author: barbora
"""

# Simple dictionary
print("Simple dictionary example")
alien_0 = {'colour': 'green', 'points': 5}
print(alien_0['colour'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"Congrats, you just earned {new_points} points!")


# Adding key-value pairs
print("\nAdding key-value pairs")
print(alien_0)
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)


# Starting with an empty dictionary
print("\nEmpty dictionaries")
alien_0 = {}
alien_0['colour'] = 'green'
alien_0['points'] = 5
print(alien_0)


# Modifying values in a dictionary
print("\nModifying values")
alien_0 = {'colour': 'green'}
print(f"The alien is {alien_0['colour']}.")
alien_0['colour'] = 'yellow'
print(f"The alien is now {alien_0['colour']}.")


# Change alien's location
alien_0 = {'x-pos': 0, 'y-pos': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x-pos']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x-pos'] = alien_0['x-pos'] + x_increment
print(f"New position: {alien_0['x-pos']}")


# Removing key-value pairs
print("\nRemoving key-value pairs")
alien_0 = {'colour': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
del(alien_0['colour'])
print(alien_0)


# Similar objects
print("\nSimilar objects")
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print(favourite_languages)
language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")


# Using get() to access values
print("\nUsing get()")
alien_0 = {'colour': 'green', 'speed': 'slow'}
#print(alien_0['points']) # Gives a key error

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

point_value = alien_0.get('points')
print(point_value)

alien_0 = {'colour': 'green', 'speed': 'slow', 'points': 5}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)























