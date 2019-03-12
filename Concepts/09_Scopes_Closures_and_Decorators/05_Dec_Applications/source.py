#! /usr/bin/env python3

''' Python Script to understand the Python topics Scopes, Closures and Decorators '''



# Decorator Application (Timing)
def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        elapsed = perf_counter() - start

        args_ = [str(x) for x in args]
        kwargs_ = ['{}={}'.format(k,v) for (k,v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print('{}({}) took {:.6f}s to run.'.format(fn.__name__, args_str, elapsed))

        return result
    return inner

print('\n\n---- Decorator Application (Timing) ----')

# fibonacci function
#   - recursion
#   - loop
#   - reduce

#---- Way-1 (Recursion)----
#   @timed
#   def calc_recursive_fib(n):
#        return 1 if n <= 2 else calc_recursive_fib(n-1) + calc_recursive_fib(n-2)
#   print(calc_recursive_fib(3))
#
# Since, we have used recursion for a decorated function it will time the decorated fucntion for each step. So to make it correct
# we will time a container for recursive function.
def calc_recursive_fib(n):
    return 1 if n <= 2 else calc_recursive_fib(n-1) + calc_recursive_fib(n-2)

@timed
def recursive_fib(n):
    return calc_recursive_fib(n)
print(recursive_fib(35))

#---- Way-2 (Loop)----
@timed
def fib_loop(fn):
    fib_1, fib_2 = 1, 1
    for i in range(3, n+1):
        fib_1 , fib_2 = fib_2, fib_1 + fib_2
    return fib_2
print(fib_loop(35))

#---- Way-3 (Reduce)----
@timed
def fib_reduce(n):
    from functools import reduce
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]) ,dummy, initial)
    return fib_n[0]
# Here, we are not using the iterable (and so as n)
print(fib_reduce(35))

del fib_reduce



# Decorator Application (Logger, Stacked Decorators)
def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now()
        result = fn(*args, **kwargs)
        print('{}: called {}'.format(run_dt, fn.__name__))
        return result
    
    return inner

@logged
def func1():
    pass

@logged
def func2():
    pass

print('\n\n---- Decorator Application (Logger, Stacked Decorators) ----')
print('---- Logger ----')
func1()
func2()

# We can also stack decorators (for example: fib_reduce is decorated by @timed and @logged)
@logged
@timed
def fib_reduce(n):
    from functools import reduce
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]) ,dummy, initial)
    return fib_n[0]
print('---- Stacked Decorators ----')
print(fib_reduce(30))
# In the above case the timed output comes first, that is because before getting the output in the logged decorator the timed
# function is executed. This all happens because of the placement of the print function. So in reality the logged decorator 
# executes first and not the timed decorator.

# Example-1 (for understanding the calling of stacked Decorators)
def dec_1(fn):
    def inner():
        print('Running dec_1')
        return fn()
    return inner

def dec_2(fn):
    def inner():
        print('Running dec_2')
        return fn()
    return inner

# Here, both the decorators dec_1 and dec_2 will work for the functions that do not take any arguments.
@dec_1
@dec_2
def my_func():
    print('Running my_func')
# Also be written as, my_func = dec_1(dec_2(my_func))
print('---- Example-1 ----')
my_func()

del dec_1
del dec_2
del my_func

# Example-2 (for understanding the calling of stacked Decorators)
def dec_1(fn):
    def inner():
        result = fn()
        print('Running dec_1')
        return result
    return inner

def dec_2(fn):
    def inner():
        result = fn()
        print('Running dec_2')
        return result
    return inner

# Here, also both the decorators dec_1 and dec_2 will work for the functions that do not take any arguments.
# Also, we can stack decorators as much as we want.
@dec_1
@dec_2
@logged
@timed
def my_func():
    print('Running my_func') 
# Also be written as, my_func = dec_1(dec_2(my_func))
print('---- Example-2 ----')
my_func()

del timed

# Exmaple-3 (Memoization)
#   - Decorators can do a lot more than just providing some extra stuff to the function, i.e., they can also modify the behaviour function.
def fib_memoize():
    cache = {1: 1, 2: 1}
    def calc_fib(n):
        if n not in cache:
            print('Caclulating fib({})'.format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib

f = fib_memoize()
print('---- Example-3 ----')
print(f(10))

# Now rewriting the above code such a way, tha twe can use a decorator. The above code is very close to decorator but is implemented as a closure only.
def memoize(fn):
    cache = dict()
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner 

@memoize
def fib(n):
    print('Calculating the fib({})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(10))
print(fib(11))  

# In the above case, the function to be decorated (or to be cached in this case), can be any function which needs to be memoized and takes one argument.
# So it is very generalised now.
# Hence, we can use it for fatorial also.

@memoize
def fact(n):
    print('Calculating fact({})'.format(n))
    return 1 if n < 2 else n*fact(n-1)

print(fact(6))
print(fact(7))

del fib

# So what we have not done here is to limit the size of the cache. If the size goes very large then the tradeoff between the space and computation will no longer hold.
# In this case we can limit the size of the cache and apply the Least-Recent-Used (LRU) approach to maintain the cache. So, as we go on more generalise approach
# of memoization he complexity of the decorator code increases, and hence there comes the Python, having it for us in its functools module.
from functools import lru_cache
@lru_cache(maxsize=8)    # since lru_cache is a paramterized decorator, which takes the max size of cache (by default - 128), so we have to call it.
def fib(n):
    print('Calculating the fib({})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(8))
print(fib(16))
print(fib(8))
print(fib(9))
# Generally, we should keep the cache sie in the power of 3 it is more efficient. We can also keep it None, which in turns means unlimited cache size, i.e., until it runs
# out of memory.
