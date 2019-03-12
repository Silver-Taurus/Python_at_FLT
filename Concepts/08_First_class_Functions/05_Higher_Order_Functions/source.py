#! /usr/bin/env python3

''' First Class Functions '''

# Higher order functions
#   - A function that takes a function as a parameter and/or returns a function as its return value.
#   - example: sorted, map, filter (mordern alternative for map and filter is list comprehensions and 
#              generator expressions).

# The map function
#   - map(func, *iterables)
#  Here, *iterables --> a variable number of iterable objects 
#        func --> some function that takes as many arguments as 
#                 there are iterable objects passed to iterables

# map(func, *iterables) will then return an iterator that calculates the function applied to each element of the iterables.
# Hence, the work is done parallely here.
# The iterator stops as soon as one of the iterables has been exhausted so, unequal length iterables can be used.

# Example:
l = [1, 2, 3, 4]

def sq(x):
    return x**2

print('\n\n---- Higher Order Function')
print('---- map function ----')
print(list(map(sq, l)))
print(list(map(lambda x: x**2, l)))

def mul(x):
    return x*x
def add(x):
    return x+x

funcs = [mul, add]
for i in range(5):
    val = list(map(lambda x: x(i), funcs))
    print(val)



# The filter function
#   - filter(func, iterable)
# Here, iterable --> a single iterable
#       func --> some function that takes a single argument

# filter(func, iterable) will then return an iterator that contains all the elements of the iterable for which the function
# called on it is true.
# If the function is None, it simply returns the elements of iterable that are true.

# Example:
print('---- filter Function ----')
print(list(filter(None, l)))
print(list(filter(lambda x: x%2 == 0, l)))



# The zip function
#   - It is not a higher order function, but is very useful with higher order functions and with list comprehensions and 
#     generator expressions.
#   - zip(*iterables)   --> iterable
#     It takes multiple iterables and return a single iterable.

# Example:
print('\n\n----zip Function ----')
p = [1, 2, 3, 4]
q = [10, 20, 30, 40]
r = [100, 200, 300, 400, 500]
print(list(zip(p, q)))
print(list(zip(p, q, r)))   # In case of iterables of uneven length, the zip function stops at the shortest length 
                            # (we can say that, zip function stops as soon as any of the iterable gets exhausted).



# List Comprehension Alternative to map
#   - In general: [<expression> for <varname> in <iterable>]
print('\n\n---- List Comprehension Alternative to map ----')
l = [1, 2, 3, 4]
print([x**2 for x in l])
l1 = [1, 2, 3]
l2 = [10, 20 ,30]
print(list(map(lambda x, y: x+y, l1, l2)))
print([x + y for x, y in zip(l1, l2)])



# List Comprehension Alternative to filter
#   - In general: [<expression1> for <varname> in <iterable> if <expression2>]
print('\n\n---- List Comprehension Alternative to filter ----')
print(list([x for x in l if x%2 == 0]))



# Combining map and filter
l = range(10)
print('\n\n---- Combining map an filter ----')
print(list(filter(lambda y: y < 25, map(lambda x: x**2, l))))
print([x**2 for x in range(10) if x**2 < 25])



# Note:
def fact(n):
    return 1 if n < 2 else n * fact(n-1)

results = map(fact, range(6))
print('\n\n---- Working of map (or filter or zip) ----')
print(results)

# Will gives the output
for x in results:
    print(x)        

# Will not give any output
for x in results:
    print(x)

# The above case is with python 3, as in this the map functions returns generator.
# So, the calculations havn't done previously until we have called it for the first time.
# This is useful as in this case, the calculations were done at the time of need (or calling), but
# if we want to reuse it we cannot. In order to reuse the data, we can store it in a list.

# Similar is the case with filter and zip function, they both also return a generator.

# So in the list comprehension we get a list back with all the calculations done and saved while we get
# a generator with map, filter and zip in which the calculations are done at the time of calling. We can
# also make a generation expression (or generator comprehension).

# Example:
print('\n\n---- Generator Expression (or Comprehension) ----')
results = (fact(n) for n in range(10))
print(results)

for x in results:
    print(x)

for x in results:
    print(x)



# Reducing Functions
#   - These are functions that recombine an iterable recursively, ending up with a single return value
#     Also called accumulators, aggregators or folding functions
#     In general terms, it is essentially a mapping from an iterable to a value which happens in a very specific way.

# Example: Finding the maximum value in an iterable
# Way-1: Using loops
l = [5, 8, 6, 10, 9]
max_value = lambda a, b: a if a > b else b
min_value = lambda a, b: a if a < b else b
def reduce_(fn, seq, initial=None):
    result = seq[0]
    for i in seq[1:]:
        result = fn(result, i)
    return result
print('\n\n---- Reducing Functions ----')
print(reduce_(max_value, l))
print(reduce_(min_value, l))

# Way-2: Using reduce()
from functools import reduce
print(reduce(lambda a, b: a if a > b else b, l))
print(reduce(lambda a, b: a if a < b else b, l))

# Example: Using reduce to reproduce join() 
print(reduce(lambda a, b: a + ' ' + b, ('python', 'is', 'awsome!')))

# Built-in Reducing Fucntions
#   - min
#   - max
#   - sum
#   - any
#   - all 
#   - join

# Example: Using reduce to reproduce any()
l = [0, '', None, 100]
print(reduce_(lambda x, y: bool(x) or bool(y), l))

# Example: Using reduce to reproduce factorial
print(reduce(lambda x, y: x*y, range(1, 6)))    # 5!

# The reduce initialiser
#   - The reduce function has a third (optional) parameter: initialiser (default to None)
#     If it is specified, it is essentially like adding it to the front of the iterable. It is often used to provide some kind of
#     default in case the iterable is empty.
l = []
print(reduce(lambda x, y: x*y, l, 1))
l = [1, 2, 3]
print(reduce(lambda x, y: x + y, l, 100))



# reduce() vs accumulate() 

#   Both reduce() and accumulate() can be used to calculate the summation of a sequence elements. But there are differences in the implementation aspects in both of these.
#   reduce() is defined in “functools” module, accumulate() in “itertools” module.
#   reduce() stores the intermediate result and only returns the final summation value. Whereas, accumulate() returns a list containing the intermediate results. The last number of the list returned is summation value of the list.
#   reduce(fun,seq) takes function as 1st and sequence as 2nd argument. In contrast accumulate(seq,fun) takes sequence as 1st argument and function as 2nd argument.
from itertools import accumulate
print(list(accumulate([1,2,3,4], lambda x,y: x*y)))
