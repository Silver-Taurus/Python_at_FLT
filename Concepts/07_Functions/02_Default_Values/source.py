#! /usr/bin/env python3

''' Python script for understanding functions and function parameters '''

# Default Values
#   - A positional arguments can be made optional by specifyinga default value for the corresponding parameter.
# Example:
#   def my_func(a. b=100):
#       # code
# Then,
#   my_func(10, 20)     --> a = 10, b = 20
#   my_func(5)          --> a = 5, b = 100

# Example: Consider a case where we have three arguments, and we want to make one of them optional:
#   def my_func(a, b=100, c):
#       # code
# Then, the above code will create an exception, as the rule is:
#   - If a positional parameter is defined with a default value then every postional parameter after it
#     must also be given a default value

# Example:
#   def my_func(a, b=5, c=10):
#       # code
# Then,
#   my_func(1)          --> a = 1, b = 5, c = 10
#   my_func(2, 6)       --> a = 2, b = 6, c =10
#   my_func(5, 10, 15)  --> a = 5, b = 10, c = 15

# Now if we want to specify the 1st ad 3rd arguments, but omit the 2nd argument:
#   - This can be done with the help of keyword arguments (or named arguments)
# Then,
#   my_func(a=1, c=2)   --> a = 1, b = 5, c = 2
# or,
#   my_func(1, c=2)     --> a = 1, b = 5, c = 2

# Named Arguments can be used without default value also.
# Hence, Positional arguments can optionally, be specified by using the paramter name.

# Also with the named arguments there is the same rule as that of the default values:
#   - Once a named argument is used, all arguments thereafter be named too.

# Example:
#   def my_func(a, b=2, c=3):
#       # code
# Then,
#   my_func(1)          --> a = 1, b = 2, c = 3
#   my_func(a=1, b=5)   --> a = 1, b = 5, c = 3
#   my_func(c=0, a=1)   --> a = 1, b = 2, c = 0.
