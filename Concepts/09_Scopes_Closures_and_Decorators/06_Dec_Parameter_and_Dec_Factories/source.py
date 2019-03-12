#! /usr/bin/env python3

''' Python Script to understand the Python topics Scopes, Closures and Decorators '''

# Decorator Parameter and Decorator Factories
#   - Now as we know the timing for each time may differ, so we can take average tiem for n number of tiems
#     entered by the user but for that, we will have a parameterised decorator.

# Now, this timed decorator will calcaulate average time to be taken for the function to execute.
#   def timed(fn):
#       from time import perf_counter
#       from functools import wraps
#
#       @wraps(fn)
#       def inner(*args, **kwargs):
#           total_elapsed = 0
#           for i in range(10):
#               start = perf_counter()
#              result = fn(*args, **kwargs)
#               total_elapsed += (perf_counter() - start)
#           avg_elapsed = total_elapsed / 10
#           print(avg_elapsed)
#           return result
#       return inner
#
# The problem with the above code is that repetition 10 is hardcoded. So what we can try is to take reps argument.

#   def timed(fn, reps=10):
#       from time import perf_counter
#       from functools import wraps
#
#       @wraps(fn)
#       def inner(*args, **kwargs):
#           total_elapsed = 0
#           for _ in range(reps):
#               start = perf_counter()
#               result = fn(*args, **kwargs)
#               total_elapsed += (perf_counter() - start)
#           avg_elapsed = total_elapsed / reps
#           print(avg_elapsed)
#          return result
#       return inner
#
# In this we call the decorator this way:
#   my_func = timed(my_func, 5)
# will work. But,
#   @timed(5)
#   def my_func():
#       ...
# Will not gonna work. Because, it is calling timed(10) first and timed is expecting two parameters not one. So this syntax will fail.

# So, what we an do is to provide a outer decorator for timed which takes the value of reps and give the timed decorator back.
# Nested Closures to rescue!
#   - Here, the outer function (timed) is not itself a decorator, instead it returns a decorator when called and any arguments passed to outer
#     (timed) can be referenced (as free variables) inside our decorator. Hence, it is called a Decorator Factory.
def timed(reps=10):
    def timed_dec(fn):
        from time import perf_counter
        from functools import wraps

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for _ in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / reps
            print(avg_elapsed)
            return result
        return inner
    return timed_dec

print('\n\n---- Decorator Paramter ----')

@timed()
def fib_loop(fn):
    fib_1, fib_2 = 1, 1
    for i in range(3, n+1):
        fib_1 , fib_2 = fib_2, fib_1 + fib_2
    return fib_2
print(fib_loop(12))
