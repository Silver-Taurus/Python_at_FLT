#! /usr/bin/env python3

''' Python script for understanding functions and function parameters '''

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