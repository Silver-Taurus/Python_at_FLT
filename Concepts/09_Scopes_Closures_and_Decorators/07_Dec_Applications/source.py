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
print('\n\n---- Decorating Class ----')
print('---- Example-1 ----')
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
print('---- Example-2 ----')
p.debug()

# As from the above two example we can see that in first exmaple rather than using decorator, we can directly add the property,
# while when are needed to reuse it we can make a decorator like in example-2. Since, debug_info can be used for many different classes.

@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError('Speed cannot exceed top_speed.')
        else:
            self._speed = new_speed

favourite = Automobile('Ford', 'Model T', 1908, 45)
print(favourite.debug())
# favourite.speed = 50  --> will give you the ValueError - Speed cannot exceed top_speed.
favourite.speed = 40
print(favourite.speed)  # Returning speed property that is in-turn the self._speed

#---- Example-3 ----
#   - Monkey Patching the ordering method in our class with the decorator `total_ordering` that is provided by the Python
from math import sqrt

# complete_ordering - our equivalent of total_ordering decorator - but is not such a good python code to be used
# and is just for reference.
#   def complete_ordering(cls):
#       if '__eq__' in dir(cls) and '__lt__' in dir(cls):
#           cls.__le__ = lambda self, other: self < other or self == other
#           cls.__ge__ = lambda self, other: not(self < other) and not(self == other)
#           cls.__gt__ = lambda self, other: not(self < other)
#       return cls

from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    
    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return False

p1, p2, p3 = Point(2,3), Point(2,3), Point(0,0)
print('---- Example-3 ----')
print('Abs: ', abs(p1))
print('is')
print(p1 is p2)
print(p2 is p3)
print('==')
print(p1 == p2)
print(p1 == p3)
print('<')
print(p2 < p1)
print(p3 < p1)
print('>=')
print(p1 >= p2)

# For toatl_ordering to be working, only one of the >, <, >= or <= should be a defined method.
