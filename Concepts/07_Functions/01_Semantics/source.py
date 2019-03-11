#! /usr/bin/env python3

''' Python script for understanding functions and function parameters '''

# Semantics for function:
#   def my_func(a, b):
#       # code
# In this context, a and b are called parameters of my_func. Also note that a and b are variables, local to my_func.
# When we call the function:
#   x = 10
#   y = 'a'
#   my_func(x, y)
# Here, the values giving to the function are called arguments. Also, note that x and y are passed by reference.

# Positional Arguments
#   - Most common way of assigning arguments to parameters: via the order in which they are passed, i.e., their position.
# Example:
#   def my_func(a, b):
#       # code
# Then,
#   my_func(10, 20)     --> a = 10, b = 20
#   my_func(20, 10)     --> a = 20, b = 10
