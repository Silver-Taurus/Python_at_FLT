#! /usr/bin/env python3

''' First class Functions '''

# Docstrings
#   - We have seen the help(x) function before  --> returns some documentation (if available) for x
# We can document our functions (and modules, classes, etc.) to achieve the same result using docstrings.

# If the first line in the function body is a string (not an assignment, not a comment, just a string by itself)
# it will be interpreted as a docstring.

# Example:
def my_func(a):
    ' documentation for my func '
    return a
# Strings and comments are different. '' or ''' ''' are strings and can be used as comments where ''' ''' being
# multiline string can be used as a multiline comment.
print(help(my_func))

# Where are docstrings stored?
#   - in the function's __doc__ property

# help(my_func) returns the function header and my_func.__doc__



# Function Annotations
#   - Function annotations give us additional way to document our functions.
#   def func(a: <expression>, b: <expression>) -> <expression>:
#       pass
def func(a: 'a string', b: 'a positive integer') -> 'a string':
    return a*b
print(help(func))   
print(func.__doc__)     # prints epmty string

# So, the annotations doesn't stores in docstring. Annotations can be any expression, so:

# Example:
#   def func(a: str, b: 'int > 0') -> str:
#       return a*b

# Example:
#   x = 3
#   y = 5
#   def my_func(a: str) -> 'a repeated ' + str(max(x, y)) + ' times':
#       return a*max(x,y)
#   help(my_func) --> my_func(a: str) -> 'a repeated 5 times'

# In the above case, annotation will only be evaluated once, when the function is being defined
# while the return expression will update if the value of x and y changes.

# Where are annotations stored?
#   - In the __annotations__ property of the function and is stored in the format of dictionary (and not a string).

# Where does Python use docstrings and annotations?
#   - It doesn't really! Mainly used by external tools and modules.
# Example: apps that generate documentation from your code  (Sphinx)

# At an enhanced version of annotations we can force the function variable to type check it and give a warning!!!



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



# Function Introspection
#   - Functions are first-class objects and thus, they have attributes like: __doc__ and __annotations__
# We can attach our own attributes, for example:
print('\n\n---- Function Introspection ----')
def my_func(a, b):
    return a+b
my_func.category = 'math'
my_func.sub_category = 'arithmetic'
print(my_func.category, my_func.sub_category)

# The dir() function
#   - dir() is a built-in function that, given an object as an argument, will return a list of valid attributes
#     for that object.
print(dir(my_func))
print(my_func.__name__)

# Exmaple:
#   def func(a, b=1, *args, **kwrgs):
#       i = 10
#       b = min(i, b)
#       return a * b
# Here, __name__        -->  gives the name of the function
#       __defaults__    -->  tuple containing positional parameter defaults
#       __kwdefaults__  -->  dictionary containing keyword-only parameter defaults
#       __code__        --> returns code object
# This __code__ object itself has various properties, which include:
#   co_varnames     --> gives parameter and local variables --> ('a', 'b', 'args', 'kwargs', 'i')
#                       parameter names first, followed by local variable names.
#   co_argcount     --> number of parameters which does not include *args and **kwargs!!!

# Another way is `inspect module` - covered in modules folder

# Difference between a function and method?
#   - They both are callables. Classes and objects have attributes (An attribute is an object that is bound to class or an object).
#     So an attribute that is callable is call method.
#
# Example:
#   def my_func():
#       pass
#
#   class MyClass:
#       def func(self):
#           pass
#
#   my_obj = MyClass()
#
# Here, func is bound to the instance of the class (or object) so it is a method while my_func is function as it is bound to any class or object.
#
# using insepct module:
#   isfunction(my_func) --> True
#   ismethod(my_func)   --> False
#   isfunction(my_obj.func) --> False
#   ismethod(my_obj.func)   --> True

# Code Introspection
#   - We can recover the source code of our function/methods
#       inspect.getsource(my_func)  --> a string containing our entire def statement, including annotations, docstrings, etc.
#     We can find out in which module our function was created
#       inspect.getmodule(my_func)  --> <module '__main__'>
#       inspect.getmodule(print)    --> <module 'builtins' (built-in)>
#       inspect.getmodule(math.sin) --> <module 'math' (built-in)>

# Function Comments
#   - We can use inspect.getcomments(my_func) to get the 'TODO:' comments as well as comments preceding the fucntion.

# Callable Signatures
#   - We can do that using inspect.signature(my_func) --> Signature instance (object of signature class)
# Contain an attribute called paramters.
#   - Essentially a dictionary of parameter names (keys), and metadata about the paramters (values)
#       keys --> parameter name
#       values --> object with attribute such as name, default, annotations, kind
#       (kind tells POSITIONAL_OR_KEYWORD or VAR_POSITIONAL or KEYWORD_ONLY or VAR_KEYWORD or POSITIONAL_ONLY).
# We cannot make any function paramter as a POSITIONAL_ONLY by ourselves but Python do have some of these functions internally.
import inspect
print('---- inspect.signature ----')

def test_func(
    a: 'a string',
    b: int = 1,
    *args: 'additional positional args',
    kw1: 'first keyword-only arg',
    kw2: 'second keyword-only arg' = 10,
    **kwargs: 'additional keyword-only args') -> str:
    '''does something
        or other '''
    pass

for param in inspect.signature(test_func).parameters.values():
    print('Name: ', param.name)
    print('Default: ', param.default)
    print('Annotation: ', param.annotation)
    print('Kind: ', param.kind)



# Callables
#   - Any object that can be called using the () operator
#   - callables always return a value
#   - this includes functions and methods, but it goes beyond just those two...
#     many other objects in Python are also callable

# To see if an object is callable, we can use the built-in function: callable
print('\n\n---- Callables ----')
print(callable(print))
print(callable('abc'.upper))
print(callable(str.upper))
print(callable(callable))
print(callable(10))

# Different types of callables
#   - built-in functions    (print, len, callable)
#   - built-in methods      (a_str.upper, a_list.append)
#   - user-defined functions    (created using def or lambda expressions)
#   - methods       (functions bound to object)
#   - classes       (MyClass(x, y, z)   
#                       --> __new__(x, y, z) -> creates the new object
#                       --> __init__(self, x, y, z) -> initialises the object
#                       --> returns the object (reference))
#   - class instances   (if the class implements __call__ method)
#   - generators
#   - coroutines
#   - asynchronous generators

# Example:
print('---- Example ----')
class MyClass:
    def __init__(self, x=10):
        print('initialising...')
        self.counter = x
print(callable(MyClass))
a = MyClass(100)
print(a.counter)
print(callable(a))
class MyNewClass:
    def __init__(self, x=0):
        print('initialising...')
        self.counter = x
    def __call__(self, x=1):
        print('updating counter...')
        self.counter += x
b = MyNewClass()
MyNewClass.__call__(b, 10)
print(b.counter)
b()
print(b.counter)
print(callable(b))



# Higher order functions
#   - A function that takes a function as a parameter and/or returns a function as its return value.
#   - example: sorted, map, filter (mordern alternative for map and filter is list comprehensions and 
#              generator expressions).

# The map function
#   - map(func, *iterables)
#  Here, *iterables --> a variable number of iterable objects 
#        func --> some function that takes as many arguments as 
#                 there are iterable objects passed to iterables

# map(func, *iterables) will then return an iterator that calculates the function applied to each element of the iterables.
# Hence, the work is done parallely here.
# The iterator stops as soon as one of the iterables has been exhausted so, unequal length iterables can be used.

# Example:
l = [1, 2, 3, 4]

def sq(x):
    return x**2

print('\n\n---- Higher Order Function')
print('---- map function ----')
print(list(map(sq, l)))
print(list(map(lambda x: x**2, l)))

def mul(x):
    return x*x
def add(x):
    return x+x

funcs = [mul, add]
for i in range(5):
    val = list(map(lambda x: x(i), funcs))
    print(val)



# The filter function
#   - filter(func, iterable)
# Here, iterable --> a single iterable
#       func --> some function that takes a single argument

# filter(func, iterable) will then return an iterator that contains all the elements of the iterable for which the function
# called on it is true.
# If the function is None, it simply returns the elements of iterable that are true.

# Example:
print('---- filter Function ----')
print(list(filter(None, l)))
print(list(filter(lambda x: x%2 == 0, l)))



# The zip function
#   - It is not a higher order function, but is very useful with higher order functions and with list comprehensions and 
#     generator expressions.
#   - zip(*iterables)   --> iterable
#     It takes multiple iterables and return a single iterable.

# Example:
print('\n\n----zip Function ----')
p = [1, 2, 3, 4]
q = [10, 20, 30, 40]
r = [100, 200, 300, 400, 500]
print(list(zip(p, q)))
print(list(zip(p, q, r)))   # In case of iterables of uneven length, the zip function stops at the shortest length 
                            # (we can say that, zip function stops as soon as any of the iterable gets exhausted).



# List Comprehension Alternative to map
#   - In general: [<expression> for <varname> in <iterable>]
print('\n\n---- List Comprehension Alternative to map ----')
l = [1, 2, 3, 4]
print([x**2 for x in l])
l1 = [1, 2, 3]
l2 = [10, 20 ,30]
print(list(map(lambda x, y: x+y, l1, l2)))
print([x + y for x, y in zip(l1, l2)])



# List Comprehension Alternative to filter
#   - In general: [<expression1> for <varname> in <iterable> if <expression2>]
print('\n\n---- List Comprehension Alternative to filter ----')
print(list([x for x in l if x%2 == 0]))



# Combining map and filter
l = range(10)
print('\n\n---- Combining map an filter ----')
print(list(filter(lambda y: y < 25, map(lambda x: x**2, l))))
print([x**2 for x in range(10) if x**2 < 25])



# Note:
def fact(n):
    return 1 if n < 2 else n * fact(n-1)

results = map(fact, range(6))
print('\n\n---- Working of map (or filter or zip) ----')
print(results)

# Will gives the output
for x in results:
    print(x)        

# Will not give any output
for x in results:
    print(x)

# The above case is with python 3, as in this the map functions returns generator.
# So, the calculations havn't done previously until we have called it for the first time.
# This is useful as in this case, the calculations were done at the time of need (or calling), but
# if we want to reuse it we cannot. In order to reuse the data, we can store it in a list.

# Similar is the case with filter and zip function, they both also return a generator.

# So in the list comprehension we get a list back with all the calculations done and saved while we get
# a generator with map, filter and zip in which the calculations are done at the time of calling. We can
# also make a generation expression (or generator comprehension).

# Example:
print('\n\n---- Generator Expression (or Comprehension) ----')
results = (fact(n) for n in range(10))
print(results)

for x in results:
    print(x)

for x in results:
    print(x)



# Reducing Functions
#   - These are functions that recombine an iterable recursively, ending up with a single return value
#     Also called accumulators, aggregators or folding functions
#     In general terms, it is essentially a mapping from an iterable to a value which happens in a very specific way.

# Example: Finding the maximum value in an iterable
# Way-1: Using loops
l = [5, 8, 6, 10, 9]
max_value = lambda a, b: a if a > b else b
min_value = lambda a, b: a if a < b else b
def reduce_(fn, seq, initial=None):
    result = seq[0]
    for i in seq[1:]:
        result = fn(result, i)
    return result
print('\n\n---- Reducing Functions ----')
print(reduce_(max_value, l))
print(reduce_(min_value, l))

# Way-2: Using reduce()
from functools import reduce
print(reduce(lambda a, b: a if a > b else b, l))
print(reduce(lambda a, b: a if a < b else b, l))

# Example: Using reduce to reproduce join() 
print(reduce(lambda a, b: a + ' ' + b, ('python', 'is', 'awsome!')))

# Built-in Reducing Fucntions
#   - min
#   - max
#   - sum
#   - any
#   - all 
#   - join

# Example: Using reduce to reproduce any()
l = [0, '', None, 100]
print(reduce_(lambda x, y: bool(x) or bool(y), l))

# Example: Using reduce to reproduce factorial
print(reduce(lambda x, y: x*y, range(1, 6)))    # 5!

# The reduce initialiser
#   - The reduce function has a third (optional) parameter: initialiser (default to None)
#     If it is specified, it is essentially like adding it to the front of the iterable. It is often used to provide some kind of
#     default in case the iterable is empty.
l = []
print(reduce(lambda x, y: x*y, l, 1))
l = [1, 2, 3]
print(reduce(lambda x, y: x + y, l, 100))



# Partial Functions
#   - It is used for Reducing Function Arguments
print('\n\n---- Partial Functions ----')
def my_func(a, b, c):
    print(a, b, c)
def func(b, c):
    return my_func(10, b, c)
func(20, 30)

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