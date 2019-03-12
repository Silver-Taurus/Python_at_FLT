#! /usr/bin/env python3

''' Python Script to understand the Python topics Scopes, Closures and Decorators '''

# Function Modifications
#   - We can also upgrade the function code by replacing it with it's closure code

#---- Way-1 (Overwirting functions) ----
add = counter(add, c)
mul = counter(mul, c)
fact = counter(fact, c)
fact2 = counter(fact2, c)

# Here the counts will be reseted as, the function's have been changed actually
print('\n\n---- Upgrading Function ----')
print('---- Way-1 (Overwriting functions) ----')
print(add(100, 200))
print(mul(121, 11))
print(fact(10))
print(fact2(5))
print(c)

# In the above upgraded case, the fact will work same as that of, in the case of non-upgraded version of it, but the fact2 will behave a bit differently
# as before the count was for the fact2 - recursive function in the closure which works similar to the fact-1 function in closure, i.e., just counting it 
# for one whole evaluation. But after upgrading fact2 to its closure, we have updated the fn paramter to the closure function due to which in case of recursion
# every time the function calls itself a new count is added. 


#---- Way-2 (Decoratoring Using @) ----
#   - We essentially modify or upgrade our function by wrpping it inside another fucntion that added some functionality to it, so we can also that we decorated our
#     fucntion with another function and we call that another function as decorator function.
#   - In general a decorator function:
#       - takes a function as an argument
#       - returns a closure
#       - the closure usually accepts any combination of parameters
#       - runs some code in the inner function (closure)
#       - the closure function calls the original fucntion using the arguments passed to the closure
#       - returns whatever is returned by that function call

# Decorators and @ symbol
#   - As we have the counter function which is a decorator and we can decorate our add, mul, fact and fact2 functions with it, using: add = counter(add, c)
#
#   - In general, if func is a decorator fucntion, we decorate another fucntion say my_func using:
#       my_func = func(my_func)
#     after defining the my_func function.
#
#   - This is so common that Python provides a convenient way of writing that as:
#       @func
#       def my_func():
#           # code
#
# Hence with the help of @ we can define and decorate the my_func at the same time, but both of the ways will give you the same thing.
#
#   - When we decorate the my_func with the func decorator the function name (my_func.__name__) will change from my_func to inner.
#     Similar problem will occur with help(my_func) and we would have lost all the information and docstring of my_func and we left with the info of inner.
#     Even using the inspect module's signature does not yield better results.
#
#   - One approach of fixing it is:
#       def counter(fn):
#           count = 0
#           def inner(*args, **kwargs):
#               nonlocal count
#               count += 1
#               counters[fn.__name__] = count
#               return fn(*args, **kwargs)
#           inner.__name__ = fn.__name__
#           inner.__doc__ = fn.__doc__
#           inner.__annotations__ = fn.__annotations__
#           return inner
#     But this doesn't fix losing the function signature - doing so would be quite comlicated.
#
#   - Instead, Python provides us with a special function that we can use to fix this (The functools.wrap function). The functools module has a wraps function that
#     we can use to fix the metadata of our inner fucntion in our decorator. In fact, the wraps function itself is a decorator. But it needs to know what was our 'original'
#     function - in this case - fn.
#
#       from functools import wraps
#       def counter(fn):
#           count = 0
#           def inner(*args, **kwargs):
#               nonlocal count
#               count += 1
#               counters[fn.__name__] = count
#               return fn(*args, **kwargs)
#           inner = wraps(fn)(inner)
#           return inner
#     or,
#
#       from functools import wraps
#       def counter(fn):
#           count = 0
#           @wraps(fn)
#           def inner(*args, **kwargs):
#               nonlocal count
#               count += 1
#               counters[fn.__name__] = count
#               return fn(*args, **kwargs)
#           return inner
#            

print('---- Way-2 (Decorating Using @) ----')
def counter(fn):
    from functools import wraps
    count = 0
    @wraps(fn)      # fixing metadata using decorator wraps
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {} (id={}) has been called {} times.'.format(fn.__name__, id(fn), count))
        return fn(*args, **kwargs)
    return inner

@counter        # using decorator
def add(a:int, b:int = 0):
    ''' adds two values '''
    return a + b

@counter        # using decorator
def mul(a:int, b:int = 1):
    ''' multiplies two values '''
    return a * b

print(add(2, 3))
print(add(100, 200))
print(mul(3, 5))
print(mul(324, 23))
