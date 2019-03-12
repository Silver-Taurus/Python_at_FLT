#! /usr/bin/env python3

''' First Class Functions '''

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
