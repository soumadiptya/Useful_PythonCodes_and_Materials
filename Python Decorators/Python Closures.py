# -*- coding: utf-8 -*-
"""
Created on Sat May 15 10:44:59 2021

@author: souma
"""
# Closures
'''Wikipedia says: A closure is a record storing a function[a] together with an environment.[1] 
The environment is a mapping associating each free variable of the function 
(variables that are used locally, but defined in an enclosing scope) 
with the value or reference to which the name was bound when the closure was created.[b] 
Unlike a plain function, a closure allows the function to access those captured variables through the closure's 
copies of their values or references, even when the function is invoked outside their scope.'''

def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)
    return inner_func()

outer_func()

# A more practical example
import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x+y


def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)