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


