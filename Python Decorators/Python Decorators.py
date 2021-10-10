# -*- coding: utf-8 -*-
"""
Created on Sat May 17 19:00:16 2021

@author: souma
"""


# Decorators are functions that take other functions as arguments and add some functionality to them without
# changing their source code
import time


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print("Display function ran")


# decorated_display = decorator_function(display) #This is same as @decorator_function
# decorated_display()
display()


# Decorators with arguments. Normally you cant supply arguments to decorators since you don't know how many arguments
# the input function will take. So have to use *args and **args for this
@decorator_function
def display_info(name, age):
    print('display_info ran with arguments {}, {}'.format(name, age))


display_info('Soumadiptya', 30)


# You can also use classes as decorators
class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display_info_class(name, age):
    print('display_info ran with arguments {}, {}'.format(name, age))


display_info_class('Surbhi', 36)


# Practical examples- Logging function runs and timings
def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

    def wrapper_function(*args, **kwargs):
        logging.info('{} Ran with args: {} and kwargs: {}'.format(original_function.__name__, args, kwargs))
        return original_function(*args, **kwargs)

    return wrapper_function


def my_timer(original_function):
    import time

    def wrapper_function(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time()
        print('{} ran in {} seconds'.format(original_function.__name__, t2 - t1))
        return result
    return wrapper_function


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(2)
    print('display_info ran with arguments {}, {}'.format(name, age))


display_info('Srini', 44)