# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 08:11:15 2020

@author: barbora
"""

# Examples in Chapter 3

#Introduction
bicycles = ['trek', 'cannondale', 'redline', 'specialised']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# Modifying elements in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles.append('honda')
print(motorcycles)

bikes2 = []
bikes2.append('honda')
bikes2.append('suzuki')
bikes2.append('yamaha')
print(bikes2)

motorcycles.insert(0, 'vespa')
print(motorcycles)

# Remove by index - del and pop()
del motorcycles[0]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f"The last motorcycle I owned was a {popped_motorcycle.title()}.")

first_owned = motorcycles.pop(0)
print(motorcycles)
print(first_owned)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Remove by value - remove() only removes first occurence of value
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('yamaha')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")



