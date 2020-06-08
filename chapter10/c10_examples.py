# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 08:43:58 2020

@author: barbora
"""

# Reading an entire file
print("\nReading an entire file")
with open('c10_examples_pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print(contents.rstrip())
