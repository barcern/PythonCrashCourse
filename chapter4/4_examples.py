# -*- coding: utf-8 -*-
"""
Created on Fri May  1 08:34:27 2020

@author: barbora
"""

# Indent placement
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()} that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
print("Thank you everyone, that was a great magic show.")

# Numerical lists using range() and list() functions
for value in range(1, 5):
    print(value)
    
for value in range(6):
    print(value)
    
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(f"Even numbers: {even_numbers}")

# List of square numbers
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(f"List of squares: {squares}")

# More concise, omitting temporary variable
squares = []
for value in range(1,11):
    squares.append(value**2)

print(f"List of squares (more concise code): {squares}")

# Stats functions: min(), max() and sum()
digits = list(range(1,10))
digits.append(0)
print(f"Digits: {digits}")
min_val = min(digits)
max_val = max(digits)
sum_val = sum(digits)
print(f"Digits smallest value: {min_val}")
print(f"Digits largest value: {max_val}")
print(f"Digits sum: {sum_val}")

# List comprehension - build lists in one line
squares = [value**2 for value in range(1,11)]
print(f"List comprehension squares: {squares}")





























