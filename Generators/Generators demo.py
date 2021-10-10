# -*- coding: utf-8 -*-
"""
Created on Wed May 12 11:10:48 2021

@author: souma
"""
# %% Import Libraries
import memory_profiler as mem_profile
import random
import time


# %% Helper Functions and Main
def square_nums(num_list):
    result = []
    for num in num_list:
        result.append(num * num)
    return result


my_nums = square_nums([1, 2, 3, 4, 5])
print(my_nums)


# Generator version
def square_nums_with_generator(num_list):
    for num in num_list:
        yield num * num


print(square_nums_with_generator([1, 2, 3, 4, 5]))  # Returns a generator object
# Iterating
my_nums_2 = square_nums_with_generator([1, 2, 3, 4, 5])
print(next(my_nums_2))
print(next(my_nums_2))
print(next(my_nums_2))
print(next(my_nums_2))
print(next(my_nums_2))
# print(next(my_nums_2)) #Error here
# ALternate way to use it
my_nums_2 = square_nums_with_generator([1, 2, 3, 4, 5])
for num in my_nums_2:
    print(num)
# Creating generators list comprehension style
my_nums_3 = [num * num for num in [1, 2, 3, 4, 5]]
print(my_nums_3)
my_nums_4 = (num * num for num in [1, 2, 3, 4, 5])
print(my_nums_4)
# Can again print it using the loop
# Convert to a list- Lose performance benefits of a generator
print(list(my_nums_4))
print(list(my_nums_4))  # Doing it a 2nd time will return empty list
# Generators help conserve memory
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print("Memory usage before:", str(mem_profile.memory_usage()), "MB")


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


# Same function using generators
def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
    yield person


t1 = time.time()
people = people_list(1000000)
t2 = time.time()
print("Memory usage after:", str(mem_profile.memory_usage()), "MB")
print('Time taken:', t2 - t1, "seconds")

# With the generator 
print("Memory usage before:", str(mem_profile.memory_usage()), "MB")
t1 = time.time()
people = people_generator(1000000)
t2 = time.time()
print("Memory usage after:", str(mem_profile.memory_usage()), "MB")
print('Time taken:', t2 - t1, "seconds")
