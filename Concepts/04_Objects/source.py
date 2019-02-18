#! /usr/bin/env python3

''' Script for info about the Objects '''

# Everything in python is object
#   --> In python everything we use whether data types or data structures
#       or operators or functions or classes etc. have one thing in common
#       all thses things, is that they are all objects (instances of classes).
# Functions (function)
# Classes (class)
# Types (type)

# This mean they all have memory addresses!

# Example:
#   def my_func():
#       pass

#   --> In this case, my_func() is a function and hence an object of class function
#       Thus, as a consequence, any object can be assigned to a variable.
#   --> Also any object can be passed to a function (a function itself).
#   --> Any object can be returned from a function.

# Note: my_func without the parenthesis is the name of the function which gives the reference
#       to the memory address. While with parenthesis it invokes the function.

# Example for int
print('Int Object example...')
a = int(5)
b = int('101', base=2)
print(a)
print(b)

# Example for function
print('\nFunction Object example...')
def square(x):
    return x**2
f = square
print(f is square)
print(f(5))

# Example for mutliple function returning
print('\nFunction Object returning example...')
def cube(x):
    return x**3
def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube
f = select_function(1)
print(f is square)
print(f is cube)
print(f(5))
f = select_function(5)
print(f is square)
print(f is cube)
print(f(5))

# Example for executing function
print('\nExectuing function through a function example...')
def exec_function(fn, n):
    return fn(n)
print(exec_function(cube, 4))
print(exec_function(square, 6))



# Object introspection

# In computer programming, introspection is the ability to determine the type of  an object at runtime. It is one of python's strengths. Everything in 
# python is an object and we can examine those objects.

# dir
print('\ndir(list) example...')
my_list = [1,2,3]
dir(my_list)

print('\ntype example...')
print(type(' '))

print(type([]))

print(type(()))

print(type({}))

print(type(dict))

print(type(3))

print(type(3.5))

name = "Silver"
print(id(name))



# inspect module
#   - The inspect module also provides several useful functions to get information about live projects.
import inspect
print('\nInspect example...')
print(inspect.getmembers(str))