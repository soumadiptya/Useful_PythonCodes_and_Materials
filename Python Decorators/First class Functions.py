# -*- coding: utf-8 -*-
"""
Created on Sat May 15 10:49:39 2021

@author: souma
"""
# First class functions - A programming language is said to have first class functions if it treats functions
# as first class citizens

# First class Citizen (programming):
# A first class citizen (or first class object) in a programming language is an entity which supports all the 
# operations generally available to other entities. These operations typically include being passed as an argument,
# returned from a function and being assigned to a variable

def square(x):
    return x*x
f = square(5)
print(f)

# We can just assign a function to a variable
f = square
print(f)
print(f(5))

# Some functions
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result
squares = my_map(square, [1,2,3,4,5])
print(squares)
def cube(x):
    return x**3
cubes = my_map(cube, [1,2,3,4,5])
print(cubes)

# Return a function from another function
def logger(msg):
    def log_message():
        print("Log:", msg)
    return log_message

log_name = logger("Hi my name is Soumadiptya")
log_name()
print(type(log_name))

# Practical example
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))
    return wrap_text
print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline')
print_p = html_tag('p')
print_p('Test Paragraph')
