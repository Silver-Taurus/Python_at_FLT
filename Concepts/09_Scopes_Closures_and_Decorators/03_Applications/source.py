#! /usr/bin/env python3

''' Python Script to understand the Python topics Scopes, Closures and Decorators '''

# Closure - Applications (Example)

# Non-Closure Code (Using Class)
#   - Class have overheads for storage, methods, initialisation, self, etc...
class Averager:
    def __init__(self):
        self.numbers = []
    
    def add(self, number):
        self.numbers.append(number)
        return sum(self.numbers) / len(self.numbers)

print('\n\n---- Closure Application ----')
print('---- Application-1 ----')
a = Averager()
print(a.add(10))
print(a.add(20))
print(a.add(15))
b = Averager()
print(b.add(20))
print(b.add(30))
print(b.add(25))

# Closure Code
#   - Here also, we can make separate instances of closure as a and b, as we know that each time the function is called it has a different scope. So, 
#     the address of cell object a and b will be different in the output.
def averager():
    numbers = []
    def add(number):
        numbers.append(number)
        return sum(numbers) / len(numbers)
    return add

a = averager()
print(a.__closure__)
print(a(10))
print(a(20))
print(a(15))
b = averager()
print(b.__closure__)
print(b(20))
print(b(30))
print(b(25))

# More Efficient Closure Code 
#   - (Same can also be used for improvement of Non-Closure Code)
def averager2():
    total, count = 0, 0
    def add(number):
        nonlocal total, count
        total += number
        count += 1
        return total/count
    return add

a = averager2()
print(a.__closure__)
print(a(10))
print(a(20))
print(a(15))



# Making Timer for getting the performance using Non-Closure (Class) and Closure way
from time import perf_counter
from time import sleep
class Timer:
    def __init__(self):
        self.start = perf_counter()
    def poll(self):
        return perf_counter() - self.start

print('---- Application-2 ----')
t1 = Timer()
sleep(1)
print(t1.poll())
sleep(2)
print(t1.poll())

# But, since we are only interested in the single function poll, then there is no use of calling it specifically every time,
# rather we can make our object callable to that functioning.
class Timer2:
    def __init__(self):
        self.start = perf_counter()
    def __call__(self):
        return perf_counter() - self.start

t1 = Timer2()
sleep(1)
print(t1())
sleep(2)
print(t1())

# Closure way
def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll

t2 = timer()
sleep(1)
print(t2())
sleep(2)
print(t2())



# Making a counter to count how many times a function is called in a program
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('{} has been called {} times.'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

print('---- Application-3 ----')
counter_add = counter(add)
print(counter_add.__closure__)
print(counter_add.__code__.co_freevars)
print(counter_add(10, 20))
print(counter_add(152434, 234234))

counter_mul = counter(mul)
print(counter_mul.__closure__)
print(counter_mul.__code__.co_freevars)
print(counter_mul(10, 20))
print(counter_mul(1524, 234))

del counter

# Storing the result for above code rather than displaying it
counters = dict()
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        counters[fn.__name__] = count
        return fn(*args, **kwargs)
    return inner

counter_add = counter(add)
counter_mul = counter(mul)
print(counter_add(10, 20))
print(counter_add(152434, 234234))
print(counters)
print(counter_mul(10, 20))
print(counter_mul(1524, 234))
print(counters)

del counter

# Improving the function, so that we can have a generalised counter function
def counter(fn, counters):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        counters[fn.__name__] = count
        return fn(*args, **kwargs)
    return inner

c = dict()
counter_add = counter(add, c)
counter_mul = counter(mul, c)
print(counter_add(10, 20))
print(counter_add(40, 50))
print(counter_add(152434, 234234))
print(c)
print(counter_mul(2, 5))
print(counter_mul(10, 20))
print(counter_mul(1524, 234))
print(c)

# Now, we can also update the `c` for any other function also
def fact(n):
    product = 1
    for i in range(2, n+1):
        product *= i
    return product

def fact2(n):
    return 1 if n < 2 else n * fact2(n-1)

counter_fact = counter(fact, c)
print(counter_fact(5))
print(counter_fact(6))
counter_fact2 = counter(fact2, c)
print(counter_fact2(5))
print(counter_fact2(6))
print(c)
