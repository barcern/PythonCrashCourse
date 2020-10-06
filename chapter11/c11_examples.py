# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:54:34 2020

@author: barbora
"""

# Use function in c11_examples_name_function
from c11_examples_name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    # Print formatted name
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

