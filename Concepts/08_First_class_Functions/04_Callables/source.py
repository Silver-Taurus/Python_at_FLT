#! /usr/bin/env python3

''' First Class Functions '''

# Callables
#   - Any object that can be called using the () operator
#   - callables always return a value
#   - this includes functions and methods, but it goes beyond just those two...
#     many other objects in Python are also callable

# To see if an object is callable, we can use the built-in function: callable
print('\n\n---- Callables ----')
print(callable(print))
print(callable('abc'.upper))
print(callable(str.upper))
print(callable(callable))
print(callable(10))

# Different types of callables
#   - built-in functions    (print, len, callable)
#   - built-in methods      (a_str.upper, a_list.append)
#   - user-defined functions    (created using def or lambda expressions)
#   - methods       (functions bound to object)
#   - classes       (MyClass(x, y, z)   
#                       --> __new__(x, y, z) -> creates the new object
#                       --> __init__(self, x, y, z) -> initialises the object
#                       --> returns the object (reference))
#   - class instances   (if the class implements __call__ method)
#   - generators
#   - coroutines
#   - asynchronous generators

# Example:
print('---- Example ----')
class MyClass:
    def __init__(self, x=10):
        print('initialising...')
        self.counter = x
print(callable(MyClass))
a = MyClass(100)
print(a.counter)
print(callable(a))
class MyNewClass:
    def __init__(self, x=0):
        print('initialising...')
        self.counter = x
    def __call__(self, x=1):
        print('updating counter...')
        self.counter += x
b = MyNewClass()
MyNewClass.__call__(b, 10)
print(b.counter)
b()
print(b.counter)
print(callable(b))
