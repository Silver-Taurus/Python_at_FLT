#! /usr/bin/env python3

''' First class Functions '''

# Docstrings
#   - We have seen the help(x) function before  --> returns some documentation (if available) for x
# We can document our functions (and modules, classes, etc.) to achieve the same result using docstrings.

# If the first line in the function body is a string (not an assignment, not a comment, just a string by itself)
# it will be interpreted as a docstring.

# Example:
def my_func(a):
    ' documentation for my func '
    return a
# Strings and comments are different. '' or ''' ''' are strings and can be used as comments where ''' ''' being
# multiline string can be used as a multiline comment.
print(help(my_func))

# Where are docstrings stored?
#   - in the function's __doc__ property

# help(my_func) returns the function header and my_func.__doc__



# Function Annotations
#   - Function annotations give us additional way to document our functions.
#   def func(a: <expression>, b: <expression>) -> <expression>:
#       pass
def func(a: 'a string', b: 'a positive integer') -> 'a string':
    return a*b
print(help(func))   
print(func.__doc__)     # prints epmty string

# So, the annotations doesn't stores in docstring. Annotations can be any expression, so:

# Example:
#   def func(a: str, b: 'int > 0') -> str:
#       return a*b

# Example:
#   x = 3
#   y = 5
#   def my_func(a: str) -> 'a repeated ' + str(max(x, y)) + ' times':
#       return a*max(x,y)
#   help(my_func) --> my_func(a: str) -> 'a repeated 5 times'

# In the above case, annotation will only be evaluated once, when the function is being defined
# while the return expression will update if the value of x and y changes.

# Where are annotations stored?
#   - In the __annotations__ property of the function and is stored in the format of dictionary (and not a string).

# Where does Python use docstrings and annotations?
#   - It doesn't really! Mainly used by external tools and modules.
# Example: apps that generate documentation from your code  (Sphinx)

# At an enhanced version of annotations we can force the function variable to type check it and give a warning!!!
