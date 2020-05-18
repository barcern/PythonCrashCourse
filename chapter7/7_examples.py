# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:27:55 2020

@author: barbora
"""

# # Simple user input using input()
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

# prompt = "If you tell us who you are, we can personalise the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")


# # Simple user input using int()
# age = input("How old are you? ")
# age = int(age)
# print(age >= 18)


# # More complex example
# height = input("How tall are you, in inches? ")
# height = int(height)

# if (height >= 48):
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")
    

# # Using modulo operator
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number = int(number)

# if (number % 2 == 0):
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")


# Intro to while loops
print("\nIntro to while loops")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    

# # Letting user choose when to stop
# prompt = "\nTell me something, and I will repeat it back to you: \nEnter "
# prompt += "'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if (message != 'quit'):
#         print(message)


# # Using a flag
# print("\nUsing a flag")
# prompt = "\nTell me something, and I will repeat it back to you: \nEnter "
# prompt += "'quit' to end the program. "

# # Create flag
# active = True
# while active:
#     message = input(prompt)
#     if (message == 'quit'):
#         active = False
#     else:
#         print(message)


# # Using a break statement
# print("\nUsing a break statement")
# prompt = "\nPlease enter the name of a city you have visited."
# prompt += "\n(Enter 'quit' when you are finished.) "
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}.")


# Using continue in a loop
print("\nUsing continue in a loop")
current_number = 0
while (current_number < 10):
    current_number += 1
    if (current_number % 2 == 0):
        continue
    print(current_number)
    



















