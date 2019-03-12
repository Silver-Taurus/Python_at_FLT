#! /usr/bin/env python3

''' Python Script to understand the Python topics Scopes, Closures and Decorators '''

# Decorator Application - Decorator Class
#   - This is because we can an object can be made callable
def dec_fac(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('Decorated function called: a={}, b={}'.format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec

@dec_fac(10, 20)
def my_func(s):
    print('Hello {}'.format(s))
my_func('World')

#   class MyClass:
#       def __init__(self, a, b):
#           self.a = a
#           self.b = b
#       def __call__(self, c):
#           print('called a={}, b={}, c={}'.format(self.a, self.b, c))
#   obj = MyClass(10, 20)
#   obj(30)
# will give the output:
#   called a=10, b=20, c=30

# Here we can make the class MyClass as a decorator factory and function __call__ as a decorator which means the callable
# object itself will be a decorator.
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self, fn):
        def inner(*args, **kwargs):
            print('Decorated fucntion called a={}, b={}'.format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner

@MyClass(10, 20)
def my_func(s):
    print('Hello {}'.format(s))
print('\n\n---- Decorator Application ----')
print('---- Decorator Class ----')
my_func('World')



# Decorator Application - Decorating Class
#---- Exmaple-1 ----
from fractions import Fraction
f = Fraction(2, 3)
print('---- Decorating Class ----')
print(f.denominator)
print(f.numerator)
#   Fraction.is_integer = lambda self: self.denominator == 1      
# This way, we can add the instance method dynamically at the run time. This is also called as Monkey-Patching.
#   print(f.is_integer())   --> will give false.

# Now doing the above code (Monkey Patching) as an external fucntion (decorator)
def dec_is_integer(cls):
    cls.is_integer = lambda self: self.denominator == 1
    return cls

Fraction = dec_is_integer(Fraction)
print(f.is_integer())

#---- Eaxmple-2 ----
from datetime import datetime

def info(self):
    results = []
    results.append('time: {}'.format(datetime.now()))
    results.append('Class: {}'.format(self.__class__.__name__))
    results.append('id: {}'.format(hex(id(self))))
    
    for k,v in vars(self).items():
        results.append('{}: {}'.format(k, v))  
    return results

def debug_info(cls):
    cls.debug = info
    return cls

@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    def say_hi(self):
        return 'Hello {}'.format(self.name)

p = Person('Silver', 1999)
p.debug()

# As from the above two example we can see that in first exmaple rather than using decorator, we can directly add the property,
# while when are needed to reuse it we can make a decorator like in exmple-2.
