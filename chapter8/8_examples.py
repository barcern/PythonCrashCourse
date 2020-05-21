# -*- coding: utf-8 -*-
"""
Created on Thu May 21 08:27:50 2020

@author: barbora
"""

# Simple function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
    
greet_user()


# Passing information to a function
def greet_user(username):
    """"Display a simple greeting."""
    print(f"Hello, {username.title()}.")
    
greet_user('jesse')
greet_user('sarah')
#name = input("Please tell me your username and I will say hello to you: ")
#greet_user(name)


# Positional arguments
print("\nPositional arguments")
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')


# Keyword arguments
print("\nKeyword arguments")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# Default values and equivalent function calls
print("\nDefault values and equivalent function calls")
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# A dog named Willie
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')




















