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
        

# Making a list of lines
print("\nMaking a list of lines")
file_name = 'c10_examples_pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())


# Working with a file's contents
print("\nWorking with a file's contents")
file_name = 'c10_examples_pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
 
# Remove whitespace on right side of string only
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
print(pi_string)
print(len(pi_string))

# Remove whitespace on both sides of string - doesn't make a difference
# in spyder
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))


# Extended example - using one million digits of pi
print("\nWorking with a file's contents")
file_name = 'c10_examples_pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
 
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(f"{pi_string[:52]}")
print(len(pi_string))


# Check if birthday in the first one million digits of pi
print("\nWorking with a file's contents")
file_name = 'c10_examples_pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
 
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")











