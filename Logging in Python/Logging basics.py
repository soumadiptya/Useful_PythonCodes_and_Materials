# -*- coding: utf-8 -*-
"""
Created on Sat May 15 12:40:18 2021

@author: souma
"""
# %% Import modules
import logging
import Employee  # Importing a module runs the code within it

# Add custom logger
logger = logging.getLogger(__name__)
# Set level
logger.setLevel(logging.DEBUG)
# Set formatter
formatter_test = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
# Add a file Handler and set custom logging
file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.ERROR)
# Add formatter to handler
file_handler.setFormatter(formatter_test)
# Add handler to logger
logger.addHandler(file_handler)

# Create and add another logger
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)


# %% Helper Functions
def add(x, y):
    """Add function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result


# %% Main
# Add more log info
num_1 = 20
num_2 = 0
# logging.basicConfig(filename='test.log', level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
add_result = add(num_1, num_2)
logger.debug('Add {} + {} = {}'.format(num_1, num_2, add_result))
subtract_result = subtract(num_1, num_2)
logger.debug('Subtract {} - {} = {}'.format(num_1, num_2, subtract_result))
multiply_result = multiply(num_1, num_2)
logger.debug('Multiply {} * {} = {}'.format(num_1, num_2, multiply_result))
divide_result = divide(num_1, num_2)
logger.debug('Divide {} / {} = {}'.format(num_1, num_2, divide_result))
