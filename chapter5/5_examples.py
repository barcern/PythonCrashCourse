# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:23:39 2020

@author: barbora
"""

# If loop example
print("Initial if loop example")
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Check for equality - careful with case sensitivity
print("\nChecking for equality")
car = 'bmw'
print(car == 'bmw')
car = 'audi'
print(car == 'bmw')
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

# Check for inequality
print("\nChecking for inequality")
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    
# Numerical comparisons
print("\nChecking for numerical comparisons")
age = 18
print(age == 18)
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")
age = 18
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

# Multiple conditions using and / or
print("\nChecking for multiple conditions using and / or")
age_0 = 22
age_1 = 18
print((age_0 >= 21) and (age_1 >= 21))
print((age_0 >= 18) and (age_1 >= 18))
print((age_0 >= 21) or (age_1 >= 21))
print((age_0 >= 25) or (age_1 >= 25))

# Check whether value in a list
print("\nChecking whether pizza toppings in the list")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

# Check whether value not in a list
print("\nChecking whether values not in a list")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Simple if statements
print("\nSimple if statements")
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
    
# if-else statements
print("\nif-else statements")
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18.")
    
# if-elif-else statements
print("\nif-elif-else statements")
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
    
























