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


# Using relative file paths
print("\nRelative file paths")
with open('text_files/c10_examples_pi_digits.txt') as file_object:
    cotents = file_object.read()
print(contents)


# Using absolute file paths
print("\nAbsolute file paths")
file_path = '/users/barbora/Documents/c10_examples_pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)


# Reading line by line
print("\nReading line by line")
file_name = 'c10_examples_pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line)
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip()) 