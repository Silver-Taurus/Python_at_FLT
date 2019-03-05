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



# A side note on tuples
#   - What defines a tuple in Python is not `()` but `,`
#     1,2,3 is also a tuple --> (1,2,3) --> The () are used to make the tuple clearer.
# To create a tuple with a single element:
#   - (1) will not work as intnded  --> int
#   - 1, or (1, ) --> tuple
# The only exception is when creating an empty tuple: () or tuple()



# Packed Values
#   - packed values are referred to those values that are bundled together. These are tuples,
#     lists, strings, sets and dictionaries, etc. In genereal, any iterable container is a packed value.

# Unpacking packed Values
#   - Unpacking is the act of splitting packed values into individual variables contained in a list or tuple.
#       a, b, c = [1, 2, 3]  --> 3 elements in [1, 2, 3] need 3 variables to unpack. Here a, b, c is the tuple.
#     The unpacking into individual variables is based on the relative positions of each element.
#   - Unpacking a tuple into another tuple.
#       a, b = (10, 20)
#   - Unpacking a string.
#       a, b, c = 'XYZ'  --> a = 'X'  b = 'Y'  c = 'Z'
#   - Instead of writing,
#       a = 10
#       b = 20
#     we can write, a, b = 10, 20

# Simple Application of Unpacking
#   - swapping values of two variables
#       a, b = b, a
#   This works because in Python, the entire RHS is evaluated first and completely,
#   then assignments are made to the LHS.

# Unpacking Sets and Dictionaries
#   d = {'key1': 1, 'key2': 2, 'key3': 3}
#   for k in d  -->  k iterates through the keys: 'key1', 'key2', 'key3'
# So, when unpacking d, we are actually unpacking the keys of d.
# Then, a, b, c = d may result in following cases:
#    --> a = 'key1', b = 'key2', c = 'key3'
# or --> a = 'key2', b = 'key1', c = 'key3'
# or --> a = 'key3', b = 'key1', c = 'key2'
# etc...

# Since, Dictionaries (and Sets) are unpacked types.
# They can be iterated, but there is no guarantee the order of the results will match your case.
# So, we rarely need to unpack the dictionaries and sets.



# Extended Unpacking (* operator)
#   - Using simple unpacking for l = [1, 2, 3, 4, 5, 6]
#       a, b = l[0], l[1:]  --> aka `parallel assignment`
#   - We can also use the * operator:
#       a, *b = l
#      Apart from cleaner syntax, it also works with any iterable, not just sequence types (slicables).
#   - The following also works:
#       a, b, *c = l    --> a = 1, b = 2, c = [3, 4, 5, 6]
#       a, b, *c, d = l --> a = 1, b = 2, c = [3, 4, 5], d = 6
# Since the * operator can only be used once in LHS as unpacking assignment, as it denotes the assignmnet
# of the rest of the values from the packed values.
#   - Another way it can be used with ordered types is:
#       l1 = [1, 2, 3]
#       l2 = [4, 5, 6]
#       l = [*l1, *l2]  --> l = [1, 2, 3, 4, 5, 6]

# Usage with unordered types
#  - It is useful though in a situation where you might want to create single collection containing all the items
#    of multiple sets, or all the keys of multiple dictionaries.
# Example:
#   d1 = {'p': 1, 'y': 2}
#   d2 = {'t': 3, 'h': 4}
#   d3 = {'h': 5, 'o': 6, 'n': 7}
# Note that the key 'h' is in both d2 and d3.
#   l = [*d1, *d2, *d3]  --> ['p', 'y', 't', 'h', 'h', 'o', 'n']
#   s = {*d1, *d2, *d3}  --> {'p', 'y', 't', 'h', 'o', 'n'}   (order is not guaranteed).


# ** operator
#   d1 = {'p': 1, 'y': 2}
#   d2 = {'t': 3, 'h': 4}
#   d3 = {'h': 5, 'o': 6, 'n': 7}
# Note that the key 'h' is in both d2 and d3.
#   d = {**d1, **d2, **d3}  (note that the ** operator cannot be used in the LHS of an assignment),
#   d  --> {'p': 1, 'y': 2, 't': 3, 'h': 5, 'o': 6, 'n': 7}
# Hence it is useful in merging the dictionaries.
# Here is caveat, that since d3 is merged at last so the value of h will get overwritten by the value
# of h in the d3 dictionary.

# This can come in handy when you have a default configuration settings and then the user changed, so the default
# one will get overwritten by the user given settings.

# You can even use it to add key-value pairs from one (or more) dictionary into a dictionary literal:
#   d1 = {'a': 1, 'b': 2}
#   {'a': 10, 'c': 3, **d1}  --> {'a': 1, 'b':2 ,'c':3} 
#   {**d1, 'a': 10, ' c': 3} --> {'a': 10, 'b':2, 'c': 3}
#  (order not guaranteed)


# Nested Unpacking
#   - Python support nested unpacking as well
#       l = [1, 2, [3, 4]]
#   We can certainly unpack it this way: a, b, c = l  then,  d, e = c  and this gives us: a = 1, b = 2, d = 3, e = 4
#   Or, we could simply do it this way: a,  b, (c, d) = l

# The * operator can only be used once in the LHS an unpacking assignment
#   - but nested * operator are allowed
# Example:
#   a, *b, (c, *d) = [1, 2, 3, 'python']
#  will give us,  a = 1, b = [2, 3], c = 'p', d = ['y', 't', 'h', 'o', 'n']
# So, the unpacked values are collected in a list format for the rest of the values (i.e., using * operator).



# *args
#   - Iterable unpacking is something similar to what happens positional arguments are passed to a function:
#   -   a, b, c = (10, 20, 30)  -->  a = 10, b = 20, c = 30
#   -   def func1(x, y, z):
#           # code
#       func1(10 ,20, 30)   --> Then inside function we get, x = 10, b = 20, y = 30

# Beacuse of this the functions also support *args parameter
# As we know  a, b, *c = 10, 20, 'a', 'b'   --> a = 10  b = 20  c = ['a','b']
# Something similar happens when positional arguments are passed to function:
#       def func1(a, b, *c):
#           # code
#       func1(10, 20, 'a', 'b')  --> a = 10  b = 20  c = ('a','b')
# The * parameter name is arbitary - you can make it whatever you want. It is customary (but not required)
# to name it *args.

# *args exhausts positional arguments
#   - You cannot add more positional arguments after *args
#       def func1(a, b, *args, d):
#           # code
#   The above defined function is OK.

#   But, This will not work!!
#       func1(10, 20, 'a', 'b', 100)



# Unpacking argumets
#   def func1(a, b, c):
#       # code
#   l = [10, 20, 30]

# This will not work like the assignment case:
#   func1(l)    --> wrong!!!
# But we can unpack the list and then pass it to the function,
#   func1(*l)   --> a = 10  b = 20  c = 30.

# Example:
def avg(*args):
    count, total = len(args), sum(args)
    return count and total/count

print(avg(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))



# Mandatory Keyword Arguments
#   - We can make keyword arguments mandatory.
# To do so, we create parameters after the positional parameters have been exhausted.
# Example:
#   def func(a, b, *args, d):
#       # code
# In this case, *args effectively exhausts all postional arguments and d must be passed as a keyword
# (named) argument.
#   func(1, 2, 'x', 'y', d=100)  -->  Here, d can only be passed through named mapping.
# or,
#   func(1, 2, d=100)
# while,
#   func(1, 2) will five an exception sice it does not get the required named argument.

# We can even omit any mandatory positional arguments:
#   def func(*args, d):
#       # code
# So we can call this functions in the following possible ways:
#   func(1, 2, 3, d=100)
#   func(d=100)

# In fact, we can force no positonal arguments at all:
#   def func(*, d):
#       # code
# Here, * indicates the 'end' of positional arguments and no positional parameters are provided before the end,
# Then,
#   func(1, 2, 3, d=100) will give an exception, since there are no positional arguments to be passed in the function.
#   func(d=100) will run perfectly fine.

# Example:
#---- Code-1 ----
#   def func(a, b=1, *args, d, e=True):
#       # code
#---- Code-2 ----
#   def func(a, b=1, *, d, e=True):
#       # code

# For Code-1:
#   - a: mandatory positional argument (may be specified using a named argument).
#   - b: optional positional argument (may be specified positionally, as a named argument, or not at all),
#        defaults to 1.
#   - args: catch-all for any (optional) additional positional arguments
# This mean it will atlest have two positional arguments.
#   - d: mandatory keyword argument
#   - e: optional keyword argument, defaults to True

# For Code-2:
#   - a: mandatory positional argument (may be specified using a named argument).
#   - b: optional positional argument (may be specified positionally, as a named argument, or not at all),
#        defaults to 1.
#   - *: no additional positional arguments allowed
# This mean it will have atmost 2 positional arguments.
#   - d: mandatory keyword argument
#   - e: optional keyword argument, defaults to True

# Note (Refer line-35):
#   - Now as we know that, if any positional parameter is provided with a default value then any other paramter after
#     it will also be having a default value. But this can be avoided if we make them the mandatory keyword parameters.
# Example:
#   def func(a, b=20, *args, d):
#       # code
# In this case, the d is not needed to have a default value, since the ambiguity of passing the value is resolved as `d`
# is the keyword parameter.



# **kwargs
#   - *args is used to scoop up variable amount of remaining positional arguments   --> tuple
#     The parameter name args is arbitary - * is the real performer here.
#   - **kwargs is used to scoop up a variable amount of remaining keyword arguments --> dictionary
#     The parameter name kwargs is arbitary - ** is the real performer here.

# **kwargs can be specified even if the positional arguments have not been exhausted (unlike keyword-only arguments).
# No parameters can come after **kwargs, this is because keyword-only parameter are the last possible paramter that can
# come at last and **kwargs scoop out that also, so left with nothing more.

# Example:
#   def func(*, d, **kwargs):
#       # code
#   func(d=1, a=2, b=3)  --> d = 1, kwargs = {'a': 2, 'b': 3}
#   func(d=1)   --> d=1 is also right, since **kwargs doesn't mandate any parameter.

# Example:
#   def func(**kwargs):
#       # code
#   func(a=1, b=2, c=3)  --> kwargs = {'a': 1. 'b': 2, 'c': 3}
#   func()  --> kwargs = {}

# Example:
#   def func(*args, **kwargs):
#       # code
#   func(1, 2, a=10, b=20)  --> args = (1,2), kwargs = {'a': 10, 'b': 20}
 
# Note:
#   def func(a, b, *, **kwargs):
#       # code
# The above code will give an exception, as * must be followed by a keyword-only argument, So, the following will be valid:
#   def func(a, b, *, d, **kwargs):
#       # code

# Typical Use Cases:
#   - Often, keyword-only arguments are used to modify the default behaviour of a fucntion
#     example: print() function.

# Caveat case:
#   def func(a, b=2, *args, c=3, d):
#       # code
#   func(1, 'x', 'y', 'z', b=5, d=10) will give the error, that b having multiple values.
# This is beacause 'x' is already given to b via postional argument passing.
# So, if we are gonna give the keyword argument for a positional paramter than it should be done before the positional passing
# occurs.



# Application-1: A Simple Function Timer (generic)
import time

def time_it(fn, *args, rep=1, **kwargs):   # here, * and ** scoops out all the postional and keyword arguments
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)             # here, * and ** unpacks all the positional and keyword arguments (with their value also) and hace gets passed in the function
    end = time.perf_counter()
    return (end -start) / rep

print(time_it(print, 1, 2, 3, sep=' - ', end=' $\n'))
print(time_it(print, 1, 2, 3, sep=' - ', end=' $\n', rep=2))

def compute_powers_1(n, *, start=1, end):
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results

def compute_powers_2(n, *, start=1, end):
    return [n**i for i in range(start, end)]

def compute_powers_3(n, *, start=1, end):
    return (n**i for i in range(start, end))

print(compute_powers_1(2, end=5))
print(compute_powers_2(2, end=5))
print(list(compute_powers_3(2, end=5)))

print(time_it(compute_powers_1, 2, start=0, end=20000, rep=5))
print(time_it(compute_powers_2, n=2, start=0, end=20000, rep=5))
print(time_it(compute_powers_3, 2, start=0, end=20000, rep=5))



# Deafult Values issue
#   - At run time, when a module is loaded, all code is executed immediately.

#---- Module code ----
#   a = 10          --> the integer object 10 is created and a references it
#   def func(a):    --> the function object is created and func references it
#       print(a)
#   func(a)         --> the function is executed

#---- Module code (for default values) ----
#   def func(a=10):     --> the function object is created, and func references it and the integer object
#       print(a)            10 is evaluated/created and is assigned as the default for a.
#   func()              --> the function is executed, by the time this happens, the default value for a has
#                           already been evaluated and assigned - it is not re-evaluated when the function is called.



# Example:
#   - We want to create a function that will write a log entry to the console with a user-specified event date/time.
#     If the user does not supply a date/time, we want to set it to the current date/time.
#---- Module code ----
#   from datetime import datetime
#   def log(msg, *, dt=datetime.utcnow()):
#       print('{}: {}'.format(dt, msg))
#   log('message 1')                        --> some time t-1
#   ................... a few minutes later ....................
#   log('message 2')                        --> some time t-1

# So, even though the log('message 2') runs at a gap of few minutes from log('message 1'), they both will gonna show same
# time as, the `dt` is once evaluated at the time of function defining.

# Solution Pattern:
#   - We set a defaut for dt to None and inside the function, we test to see it dt is still None.
#     if dt is None, set it to the current date/time, otherwise use what the caller specified for dt.
#     By this the default is going to evaluate in the function code that is, when the function is being called.
#---- Module code ----
#   from datetime import datetime
#   def log(msg, *, dt=None):
#       dt = dt or datetime.utcnow()
#       print('{}: {}'.format(dt, msg))

# In general, always beware of using a mutable object (or a callable) for an argument default.



# Problem with Mutable as a default value
def add_to(num, target=[]):
    target.append(num)
    return target
print(add_to(1))
print(add_to(2))
print(add_to(3))
# Expected result should be [1] then [2] and then [3] rather than the real output i.e [1] then [1, 2] and then [1, 2, 3].
# Again this is the result of the mutability of lists which causes the change in the output. In Python the default arguments are evaluated
# once when the function is defined, not each time the function is called (equivalent to static). So never define default arguments of mutable type
# unless you know what you are doing.

# Edit in the above to code to avoid static property
def add(ele, target=None):
    target = target or []
    target.append(ele)
    return target
print(add(1))
print(add(2))



# Use of Mutatble as a deafult value
#   - Now if we want to calculate the factorial of n, we have the following code:
#---- Module code ----
def factorial_1(n):
    if n < 1:
        return 1
    else:
#       print('calculating {}!'.format(n))
        return n * factorial_1(n-1)

print(factorial_1(5))
print(factorial_1(6))
print(factorial_1(7))
# Now, in this case the factorial for the same number will gonna repeat multiple times, if though it is calculated before.

# More better way of doing this, is to store the once evaluated values in a dictionary and then reuse them (Memoisation).
# Way-1 (Normal way):
cache = {}
def factorial_2(n, *, cache):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
#        print('calculating {}!'.format(n))
        result = n * factorial_2(n-1, cache=cache)
        cache[n] = result
        return result

print(factorial_2(5, cache=cache))
print(factorial_2(6, cache=cache))
print(factorial_2(7, cache=cache))

# Way-2 (Using the benefits of Mutability Problem of default values)
def factorial_3(n, *, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
#        print('calculating {}!'.format(n))
        result = n * factorial_3(n-1)
        cache[n] = result
        return result

print(factorial_3(5))
print(factorial_3(6))
print(factorial_3(7))

# Checking performance
factorial_1(599)
print(time_it(factorial_1, 600))

temp_cache = {}
factorial_2(599, cache=temp_cache)
print(time_it(factorial_2, 600, cache=temp_cache))

factorial_3(599)
print(time_it(factorial_3, 600))