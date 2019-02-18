#! /usr/bin/env python3

''' About the Python Optimization Interning'''

import sys
import time
import string

# Interning: reusing objects on demand 

# At start-up, Python (CPython), pre-loads (caches) a global list of integers in the
# range [-5, 256]. Any time an integer is referenced in that range, Python will ue the
# cached version of that object. Hence, the integers in the range [-5, 256] are singletons.

# Singletons: These are the classes which can be instantiated once.

# Example1:
#   >> a = 10
#   >> b = 10
#   >> a is b   --> True
#   >> a = 257
#   >> b = 257
#   >> a is b   --> False
# Run this example in python interpreter and see the result.

# This is done for optimistation strategy - as small integers show up often and hence can be
# initally the value from -5 to 256 are cahced in the memory.

# So, when we write
#   a = 10
# Python just has to point to the existing reference for 10.
# But if we write
#   a = 257
# Python does not use that global list and a new object is created every time.

# So, we can conclude that python create singleton integer objects from -5 to 256.

# Example2:
#   >> a = 100
#   >> a is 100  --> True
#   >> a = 500
#   >> a is 500     --> False
# In this we can see that the address for the 500 and 'a' is not same as a new 'a' int object is created
# everytime whereas, in case of of 'a' and 100 it is true.

# Example3:
#   >> a = int('1010', 2)
#   >> a is 10  --> True



# Python - String Interning

# As the Python code is compiled, identifiers are interned:
#   --> variable names
#   --> function names
#   --> class names

# Some string literals may also be automatically interned:
#   --> string literals that look like identifiers (eg: 'hello_world')
#   --> although, if it starts with a digit, even though that is not a valid identifuer it may still get interened.
#       But don't count on it.

# Identifiers: Start with _ or letter and contains _ or letter or numbers.

# So python do this because:
# It's all about the speed and memory optimisation.
# Python, both internally, and in the code you write, deals with lots and lots of dictionary type lookups on
# string keys, which means a lot of string equality testing.

# Let's say we want to see if two strings are equal:
# a = 'some_long_string' and b = 'some_long_string'
# Using a == b, we need to compare the two strings character by character.
# But if we know that 'some_long_string' has been interned, then a and b are the same thing and if they both
# point to the same memory address then they are also equal.
# So we can use a is b instead - which compares two integers (memory address) and this is much faster than the
# character by character comparison.

# Not all the strings are interned by Python
# But you can force strings to be interned by using the sys.intern()method.
# Example:
#   >> import sys
#   >> a = sys.intern('the quick brown fox')
#   >> b = sys.intern('the qucik brown fox')
#   >> a is b   --> True (much faster than a == b)

# When should you do this?
#   --> dealing with a large number of stirngs that could have high repetition
#       ex: tokenising a large corpus of text (NLP).
#   --> lots of string comparisons.


# Example1:
#   >> a = 'hello_world_we_are_going_to_try_the_interning_stuff'
#   >> b = 'hello_world_we_are_going_to_try_the_interning_stuff'
#   >> a is b   --> True.
# While,
#   >> c = 'Hello World'
#   >> d = 'Hello World'
#   >> c is d   --> False.

# Exmaple2:
#   >> import sys
#   >> a = sys.intern('hello world')
#   >> b = sys.intern('hello world')
#   >> c = 'hello world'
#   >> a is b   --> True
#   >> a is c   --> False
# So, if we want to intern a string then we have to use intern method at all the places where that
# string variable is defined or else it will not intern the string variable.



# Benchmarking
def compare_using_equals(n):
    ''' Compares two long strings for n times using equal operator '''
    a = 'a long string that is not intern' * 200
    b = 'a long string that is not intern' * 200
    for i in range(n):
        if a == b:
            pass

def compare_using_interning(n):
    ''' Compares two long strings for n times using identity operator after interning '''
    a = sys.intern('a long string that is not intern' * 200)
    b = sys.intern('a long string that is not intern' * 200)
    for i in range(n):
        if a is b:
            pass
VAL = 100000000
start = time.perf_counter()
compare_using_equals(VAL)
end = time.perf_counter()
print('Using equality: ', end-start)

start = time.perf_counter()
compare_using_interning(VAL)
end = time.perf_counter()
print('Using identity: ', end-start)


# Python initially compiles your code into the byte code which then runs in the python virtual machine
# as an interpretition.


# There is another variety of optimzation that can occur at compile time.
# Python optimizes the following way:
#   --> Constant Expr
#       - numeric calculations: 24 * 60, Python will actually pre-calculate 24*60 -> 1440.
#       - short sequences, length < 20
#           (1,2) * 5 -> (1,2,1,2,1,2,1,2,1,2)
#           'abc' * 3 -> 'abcabcabc'
#           'hello' + 'world' -> 'hello world'
#   But not, 'the quick brown fox' * 10 beacuse there is tradeoff between storage and computation.
#   And that tradeoff value is 20 characters.
#
#   --> Membership Tests: Mutables are replaced by Immutables
#       - When membership test such as:
#           if e in [1,2,3]:
#         are encountered, the [1,2,3] constant, is replaced by its immutables counterpart
#           if e in (1,2,3):    -> done internally
#   Then,
#       lists -> tuples
#       sets  -> frozensets

# Set memebership is much faster than list or tuple membership (sets are basically like dictionaries)
# So, instead of writing:
#   if e in [1,2,3]:  or  if e in (1,2,3):
# write
#   if e in {1,2,3}:
# and especially, if the expression is going to execute many times.

def my_func():
    ''' Arbitary function for checking the optimisation'''
    a = 24 * 60
    b = (1,2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 5
    f = ['a', 'b'] * 3 
# printing the constants associated with the function after compilation
print(my_func.__code__.co_consts)

def my_func1(e):
    if e in [1,2,3]:
        pass
print(my_func1.__code__.co_consts)



# Benchmark for list/tuple membership vs set membership
char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)
print(char_list)
print(char_tuple)
print(char_set)

def membership_test(n, container):
    ''' Arbitary function for benchmarking the list/tuple vs set membership test '''
    for i in range(n):
        if 'z' in container:
            pass

start = time.perf_counter()
membership_test(VAL, char_list)
end = time.perf_counter()
print('list: ', end-start)

start = time.perf_counter()
membership_test(VAL, char_tuple)
end = time.perf_counter()
print('tuple: ', end-start)

start = time.perf_counter()
membership_test(VAL, char_set)
end = time.perf_counter()
print('set: ', end-start)