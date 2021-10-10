# -*- coding: utf-8 -*-
"""
Created on Wed May 12 14:17:35 2021

@author: souma
"""
# Iterable
nums = [1,2,3]
for num in nums:
    print(num)

# If something is an iterable it needs to have the __iter__ method
print(dir(nums)) # An iterable does not have the next 
# Iterators on the other hand have a state that tells where they are during iteration. They also have a next
# method to get the next value of the iterable
# Calling the __iter__ method on a iterable returns an iterator
nums_iterator = nums.__iter__()
print(type(nums_iterator))
print(dir(nums_iterator)) # An iterator has the next method

# Better to use the iter function 
nums_iterator = iter(nums)
print(next(nums_iterator))
print(next(nums_iterator))
print(next(nums_iterator))
print(next(nums_iterator)) # Error
# A for loop is doing the same thing in background
nums_iterator = iter(nums)
while True:
    try:
        print(next(nums_iterator))
    except StopIteration:
        break
# Create a class that behaves like built in range function
class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

nums = MyRange(1, 10)
for num in nums:
    print(num)
# Check if the next method works
nums = MyRange(1, 10)
print(next(nums))
# Check with the actual range class
nums = range(1, 10)
for num in nums:
    print(num)
print(next(nums)) # TypeError: 'range' object is not an iterator. It must be implemented differently
print(dir(nums)) # It does have the iter method
nums_range = iter(nums)
print(next(nums_range))

# Generators are iterators but the iter and next methods are created automatically
def my_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1
nums_gen = my_range(1, 10)
print(next(nums_gen))
print(next(nums_gen))
for num in nums_gen:
    print(num)
# Generators come in handy for writing memory efficient programs
# Check out the itertools module