# Lab 05 - practice file
#
# Use this file to try out the examples as you work through the lab.
# Type them in, run the file, then clear it out and use it again for the next one.
#
# Run it from the terminal with:   python exercise.py
# On Windows you may need:         py exercise.py
#
# Nothing in this file is marked, so experiment as much as you like.
# Let's see Python keywords
'''  
import keyword
print(keyword.kwlist)
'''
# Numeric data types
age = 21                    # int (integer)
height = 5.9               # float (floating-point number)
temperature = -15.5        # float (can be negative)

# String data type
student_name = "Muhammad Syaifuddean Hisham"    # str (string)
course_title = 'Python Programming'  # str (single or double quotes)
description = """This is a multi-line string that spans several lines."""   # str (triple quotes)
favorite_Game = 'Free Fire'  # str (string with special characters)
# Boolean data type
is_active = True           # bool (boolean)
has_submitted = False      # bool (boolean).


# Special data type
nothing = None             # NoneType (represents absence of value)
'''
print( " Name = " + student_name)
print( " Course = " + course_title)
print( " Description = " + description)
print( " Favorite Game = " + favorite_Game)
print( " Is Active = " + str(is_active))
print( " Has Submitted = " + str(has_submitted))
print( " Nothing = " + str(nothing))
'''
'''
# Checking the data types
print(type(student_name)) 
print(type(course_title))
print(type(description))
print(type(favorite_Game))
print(type(is_active))
print(type(has_submitted))
print(type(nothing))
'''
'''
print(type(25))  # int
print(type("25"))  
'''
'''
number_text = "25"
print(type(number_text))

real_number = int(number_text)
print(type(real_number))

name = "false"
print(type(name))

real_name = bool(name)
print(type(real_name))
'''

'''
text = "Hello Syaifuddean, welcome to Python programming! How are you doing today?"

# len() is a function, so the value goes inside the brackets
print(len(text))          # 74

# upper() and lower() are methods, so the value comes before the dot
print(text.upper())       # HELLO SYAIFUDDEAN, WELCOME TO PYTHON PROGRAMMING! HOW ARE YOU DOING TODAY?
print(text.lower())       # hello syaifuddean, welcome to python programming! how are you doing today?
'''

'''
text = "Hello World"

text = "Hello World"

print(text.upper()) # HELLO WORLD  
print(text.upper) # error

print(text.upper())
print(text.lower())
'''
'''
text = "hello"
real_text = text.upper()
print(real_text)          # HELLO
print(text)               # hello

text = "hello"
text = text.upper()
print(text)               # HELLO

'''
'''
# Import entire modules
import math
import random
import datetime

# Using imported modules
circle_area = math.pi * (8 ** 2)
random_number = random.randint(1, 50)
current_date = datetime.datetime.now()

# Import specific functions from modules
from math import sqrt, pow, sin, cos
from random import choice, shuffle
from datetime import datetime, timedelta

# Using imported functions directly (no module prefix needed)
square_root = sqrt(25)
power_result = pow(2, 8)
random_choice = choice(['apple', 'banana', 'cherry'])

print("Circle Area:", circle_area)
print("Random Number:", random_number)
print(square_root)
print("Current Date:", current_date)
'''

'''
name = input("Enter your name: ")
print(" Your name is " +name)
print(type(name))

age = input("Enter your age: ")
print(age)
print(type(age)) #input() always returns a string. 
#It makes no difference that you typed digits — what you received is the text "25"
#, the same "25" you compared against 25 in the previous section.
'''
'''
import math
first = input("First number: ")
second = input("Second number: ")
print(first + second)
'''

'''
first = int(input("First number: "))
second = int(input("Second number: "))
print(first + second)
'''
'''
print("Hello", "Python", "World")
print("Hello", "Python", "World", sep="-")

print("Hello", end=" ")
print("World")

'''

name = "Syaifuddean"
age = 18
print("My name is " + name + " and I am " + str(age) + " years old.")

name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")