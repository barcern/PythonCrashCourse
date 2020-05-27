# -*- coding: utf-8 -*-
"""
Created on Wed May 27 08:52:24 2020

@author: barbora
"""

# Creating classes
print("\nCreating a class")
class Dog:
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialise name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
