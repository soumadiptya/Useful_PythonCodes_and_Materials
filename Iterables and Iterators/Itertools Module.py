# -*- coding: utf-8 -*-
"""
Created on Thu May 13 11:31:22 2021

@author: souma
"""
#%% Import libraries
import itertools
import operator
#%% Main
counter = itertools.count()
print(type(counter))
for num in counter:
    print(num)
    if num > 100:
        break
# This is an iterator so next works
print(next(counter))
# Index for a list of values
data = [100, 200, 300, 400]
daily_data = zip(itertools.count(), data)
print(type(list(daily_data)[0])) # tuple
print(list(daily_data))
print(type(list(daily_data)[0])) # This gives an error because daily_data has already been exhausted
# Arguments to count
counter = itertools.count(5, 2) # Can be negative or decimals etc
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# So it was my conception that the zip function simply creates tuples Lol. It clearly doesn't. 
# It operates on a pair of iterables and creates tuples from those iterables till the shortest one is exhausted
example_zip = zip(itertools.count(), [1,2,3,4,5], ['a', 'b', 'c'])
print(list(example_zip)) # This shows clearly that from the 2nd list 4 and 5 are not utilized
# Also tuples are not just a pair of values they can be any length combo
# There is a different version of zip which pairs the longest iterables
daily_data = itertools.zip_longest(range(10), data)
print(list(daily_data)) # Missing values filled with NA

# Itertools cycle
daily_cycle = itertools.cycle([1,2,3])
print(next(daily_cycle))
print(next(daily_cycle))
print(next(daily_cycle))
print(next(daily_cycle))
print(next(daily_cycle))
print(next(daily_cycle))
# Can be used to simulate a on off switch
switch_sim = itertools.cycle(('On', 'Off'))
print(next(switch_sim))
print(next(switch_sim))
print(next(switch_sim))
print(next(switch_sim))
print(next(switch_sim))
print(next(switch_sim))
# Itertools repeat
counter_repeat = itertools.repeat(2, times=3)
print(next(counter_repeat))
print(next(counter_repeat))
print(next(counter_repeat))
# Practical use
squares = map(pow, range(10), itertools.repeat(2))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
# An alternative to map
squares = itertools.starmap(pow, [(0,2), (1,2), (2,2), (3,2)])
print(list(squares))
# Permutations and combinations
letters = ['a', 'b', 'c', 'd']
numbers = [0,1,2,3]
names = ['Somu', 'Punni']
# Combination 
result = itertools.combinations(letters, 3)
for item in result:
    print(item)
# Permutation
result = itertools.permutations(letters, 2)
for item in result:
    print(item)
# Both of these dont allow repeats
# E.g. if you wanted to create a 4 digit code generator from 0,1,2,3 one combo is 0000
result = itertools.product(numbers, repeat=4)
for item in result:
    print(item)
# Combinations with replacement
result = itertools.combinations_with_replacement(numbers, r=4)
for item in result:
    print(item)
# Chain
combined = itertools.chain(letters, numbers, names)
for item in combined:
    print(item)
# Slice
result = itertools.islice(range(10), 5)
for item in result:
    print(item)
# Additional start and stop arguments
result = itertools.islice(range(10), 1, 5, 2)
for item in result:
    print(item)
# Islice example with reading a file and grabbing a few lines
# There is some sort of a fucking error in Spyder due to which only absolute paths can be used with open
with open(file='D:/Career Development/Wells Fargo specific Learning/Iterables and Iterators/Iterables and Iterators.py', mode='rb') as code_file:
    first_10 = itertools.islice(code_file, 10)
    for lines in first_10:
        print(lines)
# Compress- Used for filtering one iterable on the basis of other
selectors = [True, True, False, True]
result = itertools.compress(letters, selectors)
for item in result:
    print(item)
# It's similar to filter but filter needs a function as the definition
def filter_criteria(num):
    if num<2:
        return True
    return False
result = filter(filter_criteria, numbers)
for item in result:
    print(item)
# Exactly opposite to filter is itertools.filterfalse
# dropwhile
numbers = [0, 1, 2, 3, 2, 1, 0]
result = itertools.dropwhile(filter_criteria, numbers)
for item in result:
    print(item)
# As soon as the filter criteria is met for one item it stops filtering
# Opposite to this is takewhile
result = itertools.takewhile(filter_criteria, numbers)
for item in result:
    print(item)
# Accumulate- Cumulative sum? But different functions can be passed
result = itertools.accumulate(numbers)
for item in result:
    print(item)
# Multiply example
numbers = [1, 2, 3, 2, 1, 0]
result = itertools.accumulate(numbers, func=operator.mul)
for item in result:
    print(item)
# Groupby
people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]
def get_state(person):
    return person['state']
person_group = itertools.groupby(people, get_state)
for key, group in person_group:
    print(key)
    for person in group:
        print(person)
# This groupby expects values to be sorted by key (in this case state) so its pretty useless
# Replicating an iterator- tee
person_group = itertools.groupby(people, get_state)
copy1, copy2 = itertools.tee(person_group) 
for item in copy1:
    print(copy1)