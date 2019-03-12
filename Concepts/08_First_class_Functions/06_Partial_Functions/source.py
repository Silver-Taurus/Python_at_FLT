#! /usr/bin/env python3

''' First Class Functions '''

# Partial Functions
#   - It is used for Reducing Function Arguments
print('\n\n---- Partial Functions ----')
def my_func(a, b, c):
    print(a, b, c)
def func(b, c):
    return my_func(10, b, c)
func2 = lambda x, y: my_func(10, x, y)
func(20, 30)
func2(20, 30)

# Another way is by using partial from functools
from functools import partial
f = partial(my_func, 10)
f(20, 30)

# Handling more complex aguments
def test_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)
g = partial(test_func, 10, k1='a')
g(20, 100, 200, 300, k2='b', k3='c', k4='d')

def pow(base, exponent):
    return base**exponent
sqaure = partial(pow, exponent=2)
print(sqaure(5))

# Though, square(5, exponent=3) is still possible.

# Beware!!!
#   - We can use variables when creating partials but there arises a similar issue to argument default values
# Example:
#   def my_func(a, b, c):
#       print(a, b, c)
#   
#   a = 10
#   f = partial(my_func, a)     -->  The memory address of 10 is baked in to the partial
#   f(20,30)    --> 10, 20 , 30
#
#   a = 100     -->  a now points to a different memory address but the patial still points to the original object (10).
#   f(20, 30)   --> 10, 20, 30
# If a is mutable, then it's content can be changed.

# Example:
def mutable_test_func(a, b):
    print(a, b)
a = [1, 2]
f = partial(mutable_test_func, a)
f(100)
a.append(3)
f(100)



# Partial function Example
origin = (0,0)
l = [(1, 1), (0, 2), (-3, 2), (0, 0), (10, 10)]
dist = lambda x, y: (x[0]-y[0])**2 + (x[1]-y[1])**2
# Here, sorted(l) will not give the desires results.
# so we can use, sorted(l, key=dist2(i, origin))    --> but it will not gonna work since, it is a function call and not function itself
# and for a key we need a function which performs operation on single paramter.
# So, we can utilise the already defined dist function as follows:
dist_from_origin = partial(dist, origin)
print(sorted(l, key=dist_from_origin))