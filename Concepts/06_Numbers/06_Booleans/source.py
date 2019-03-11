#! /usr/bin/env python3

''' Description on Numbers '''

import sys
import time
from fractions import Fraction
import math
import decimal
from decimal import Decimal
import cmath

# Bool class
#	- It is the subclass of int
# Python has concrete bool class that it used to represent Boolean values. Being a subclass of int class it possess
# all the functionality of the int class.
print('\n\n----Bool class----')
print('is bool a subclass of int: ', issubclass(bool, int))

# Two constants are defined: True or False which are instances of bool class
print('is True an instance of bool class: ', isinstance(True, bool))
print('is True an instance of int class: ', isinstance(True, bool))

# They are singleton objects of type bool and hence they will gonna have some fixed memory address
# As, True denotes int 1 and False denotes int 0, the memory address reference they are going to have
# is different that of int 1 and int 0 which are also singleton objects of class int.

# So, we can use both is and == equality operator

# Strange behaviour
#	- True > False -> False
#	- (1 == 2) == False -> True
#	- (1 == 2) == 0	- True
#	- True + True + True -> 3
#	- (True + True + True) % 2 -> 1
#	- -True	-> -1
#	- 100 * False -> 0

# Boolean constructor
#	- bool(x) returns True when x is True and False when x is False

# What really happens is that many classes contain a definition of how to cast instances of themselves
# to Boolean - this is sometimes called the truth value (or truthyness) of an object
# Integers have a truth value defined according to this rule:
#	- bool(0) -> False
#	- bool(x) -> True for any int x != 0

# Object Truth Values
#	- Every object has a True truth value, except:
# 		- None
#		- False
# 		- 0
# 		- empty sequences
# 		- empty mapping types
# 		- custom classes that implement __bool__ or __len__

# Class define their truth values by defining a special instance method:
# __bool__(self) (or __len__)
# Then, when we call bool(x), Python will actually executes x.__bool__(), if __bool__() not present
# it will find x.__len__(). If both of them are not defined then by default it will return True.

# Boolean operators
#	- and, or, not
# Now , we have different properties:
#	- Commutativity
#		A or B == B or A
#		A and B == B and A
#	- Distributivity
#		A and (B or C) == (A and B) or (A and C)
#		A or (B and C) == (A or B) and (A or C)
#	- Associativity
#		A or (B or C) == (A or B) or == A or B or C
#		A and (B and C) == (A and B) and C == A and B and C
#	Here, left to right evalutaion takes place.
#	- De Morgan's Theorem
#		not(A or B) == (not A) and (not B)
#		not(A and B) == (not A) or (not B
#	- Miscellaneous
#		not(x < y) == (x >= y)
#		not(x > y) == (x <= y)
#		not(x >= y) == (x < y)
#		not(x <= y) == (x > y)

# Operator Precedence
# ()
# < > <= >= == != in is
# not
# and
# or

# Short-Circuit Evaulation or ShortHand Ternary
# x or y	--> if x is True answer is True irrespective of y
# x and y	--> if x is False answer is False irrespective of y

# Example-1 of Short-Circuit Evaluation
# 	if symbol in watch_list:
# 		if price(symbol) > threshold:
#			# do something
# since calling the price() method has a cost, we would only want to call if the symbol was on our watch_list.
# But because of short-circuit evaluation we could write this equivalently as:
#	if symbol in watch_list and price(symbol) > threshold:
#		# do something

# Example-2 of Short-Circuit Evaluation
#	if name[0] is string.digits:
#		# do something
# this code will break if name is None or an empty string
# because of short-circuiting and truth values:
# 	if name and name[0] in string.digits:
#		# do something

# Example of truth values and short-circuit evalutaion
a = 10
b = 2

def example(a, b):
	if b and a/b > 2:
		print('a is atleast twice b')

print('----Truth Value and Short-Circuit Evaluation----')
example(a, b)
b = 0
example(a, b)
b = None
example(a, b)

# Boolean Operators and Truth Values and Short-Circuit Evaulation
# 	- Normally, Boolean operators are defined to operate on  and return Boolean values
# 	  But every object in Python has a truth value, So, for any object X and Y, we could also write,
# 		bool(X) and bool(Y)    bool(X) or bool(Y)
# 	  In fact, we don't need to use bool(), 
# 		X and Y		X or Y

# So, what is returned when evaluating these operations:
#	- for X or Y
#		if X is true, returns X, otherwise evaluates Y and returns Y.
#	- for X and Y
#		if X is false, returns X, otherwise evaluates Y and returns Y.

# Consequence of `or`
# Example-1:
# 	var = string or 'N/A'
#		- if string is None		var = N/A
# 		- if string is ''		var = N/A
# 		- if string contains	var = string 
# 	  	  characters	

# Example-2:
# 	var = s1 or s2 or s3 or 'N/A'

# Consequence of `and`
# Example-1:
#	var = a and total/a
#		- if a is 0		 var = 0
#		- if a is not 0  var = total/a

# Example-2:
# 	avg = n and sum/n

# Example-3:
#	return s and s[0] or ''

# Boolean `not`
#	not x will gives the boolean value in return.

# True or "Some" --> True
# False or "Some" --> Some
output1 = None
output2 = "Hello"
msg1 = output1 or "No data returned"
msg = ouput2 or "No data returned"
print(MSG1)
print(MSG2)



# Categories of Comparison Operators
#	- binary operators
#	- evaluate to a bool value
# Identity Operations	-->	is	is not	--> compares memory address - any type
# Value Comparisons		-->	==	!=		--> compares values - diiferent types OK, but must be compatible
# Ordering Comparisons	--> < 	<= 	> 	>=		--> doesn't work for all types

# Chained Comparisons
#	- a == b == c	--> a== b and b == c
#	- a < b < c		--> a < b and b < c


# Ternary Operators
# Ternary operators are more commonly known as conditional expressions in Python.
# These operators evaluate something based on condition being true or not.

# first way
# statement_if_true if condition else statement_if_false
is_nice = True
state = "nice" if is_nice else "not nice"
print(state)

# second way
# (if_test_is_false, if_test_is_true)[test]
nice = True
personality = ('mean', 'nice')[nice]
print("The cat is", personality)
# This works simply because True == 1 and False == 0, and so can be done with lists in addition to
# tuples.

# Reason to avoid using a tupled ternery is that it results in both elements of the tuple being
# evaluated, whereas the if-else ternary operator does not.

#Example:
#   condition = True
#   print(2 if condition else 1/0)

#   Output is 2

#   print((1/0, 2)[condition])
#   ZeroDivisionError is raised

# This happens because with the tupled ternary technique, the tuple is first built, then an index
# is found. For the if-else ternary operator, it follows the normal if-else logic tree. Thus, if
# one case could raise an exception based on the condition, or if either case is a
# computation-heavy method, using tuples is best avoided.