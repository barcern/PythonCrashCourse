# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:27:55 2020

@author: barbora
"""

# Simple user input using input()
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalise the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")


# Simple user input using int()
age = input("How old are you? ")
age = int(age)
print(age >= 18)


# More complex example
height = input("How tall are you, in inches? ")
height = int(height)

if (height >= 48):
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
    

# Using modulo operator
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if (number % 2 == 0):
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")






























