#! /usr/bin/env python3

''' First class Functions '''

# Lambda Expressions
#   - lambda expressions are simply another way to create functions and are also called as anonymous functions.
#---- Syntax ----
#   lambda [parameter list]: expression
# Here, lambda is the keyword like def which marks the function and parameter list is optional but lamda keyword
# must be followed by a colon which marks the end of the parameter list and then it is followed my the expression
# and returned when the lambda function is called.
# The above syntactical expression returns a function object, that evaluates and returns the expression when it is called.
# This can be assigned to a variable or can be passed as an argument to another function.

# Lambdas or anonymous functions are not equivalent to closures.
print('---- Lambdas ----')
my_func = lambda x: x**2
print(my_func(3))
print(my_func(4))

# Pasing as an Argument to another function
def apply_func(x, fn):
    return fn(x)
print(apply_func(3, lambda  x: x**2))
print(apply_func(2, lambda  x: x+5))
print(apply_func('abc', lambda x: x[1:]*3))

# Limitations
#   - The body of lambda is limited to a single expression
#   - no assignments
#   - no annotations
#   - single logical line of code --> line-continuation is OK, but still just one expression

# Exmaples:
f = lambda x, y=0: x+y
print(f(5), f(5, 10))

g = lambda x, *args, y, **kwargs: (x, args, y, kwargs)
print(g(1, 'a', 'b', y=100, a=10, b=20))

def apply_fn(fn, *args, **kwargs):
    return fn(*args, **kwargs)

print(apply_fn(lambda x: x**2, 3))
print(apply_fn(lambda x, y: x+y, 1, 2))
print(apply_fn(lambda x, *, y: x+y, 1, y=20))
print(apply_fn(lambda *args: sum(args), 1, 2, 3, 4, 5))
print(apply_fn(sum, (1, 2, 3, 4, 5)))
print(sum((1, 2, 3, 4, 5)))

# Applications of lambdas in sorting
#   - sorted() function is also there in python but it is not an in-place sorting
print('---- Lambdas and Sorting ----')

l = ['c', 'B', 'D', 'a']
print(l, sorted(l), sorted(l, key=lambda s: s.upper()))

d = {'def': 300, 'abc': 200, 'ghi': 100}
print(d, sorted(d), sorted(d, key=lambda k: d[k]))

def dist_sq(x):
    return (x.real)**2 + (x.imag)**2
c = [3+3j, 1-1j, 0, 3+0j]
# sorted(l) --> will give an exception as their is no ordering defined for complex numbers
print(c, sorted(c, key=dist_sq))
print(c, sorted(c, key=lambda x: (x.real)**2 + (x.imag)**2))

names = ['Chapman', 'Cleese', 'Gilliam', 'Idle', 'Jones', 'Palin']
print(names, sorted(names, key=lambda s: s[-1]))
# The sorted function is stable sort (which retains the order).

# Randomising an Iterable using Sorted
import random
my_list = [1,2,3,4,5,6,7,8,9,10]
print(my_list, sorted(my_list, key=lambda x: random.random()))
