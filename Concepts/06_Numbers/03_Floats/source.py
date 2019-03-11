#! /usr/bin/env python3

''' Description on Numbers '''

import sys
import time
from fractions import Fraction
import math
import decimal
from decimal import Decimal
import cmath

# Floats
#	- The Float class is python's default implementation for representing real numbers
# The Python (CPython) float is implemented using the C double type which (usually!) implements the
# IEEE 754 double-precision binary float or also called binary64.

# Unlike int, float uses a fixed number of bytes --> 8 bytes (but Python objects have some overhead too)
# So, including the overhead the size of the float objects is 24 Bytes.

# The 8 bytes or 64 bits of a float are assigned to different parts of the float number:
# 	- sign	--> 1 bit
#	- exponent	--> 11 bits, having the range [-1022, 1023]
#	- significant digits  --> 52 bits, having 15-17 significant (base-10) digits

# Numbers can be represented as base-10 integers and fractions
# for ex:
#		0.75  -->  7/10 + 5/100  -->  7*10^-1 + 5*10^-2

# Some numbers (fractions like - 1/3) do not have a finite decimal representation, so we cannot given the
# exact value of those numbers in float but can give a precise approximation.

# While some numbers (fractions like - 1/10 = 0.1) do have a finite decimal representation but as we know
# that the numbers are to be stored in the computer which understands the binary representation and hence,
# those number may not have a finite binary representation and hence the float value of those numbers are
# stored as an approximate float representation if the precision is set to low, but if the precision is high
# (normally) then the float number will store the actual decimal number of the binary approximation of the
# given number which is not exactly equal to the decimal representation.

# Because of the above reasoning:
print('\n\n----Float Equality Testing Problems----')
print('is 0.1 + 0.1 + 0.1 = 0.3 True?')
print(0.1+0.1+0.1 == 0.3)

# In order to do Float equality
# Way-1 (using round):
print('----Way-1----')
print(round(0.1+0.1+0.1, 1) == round(0.3,1))
# while round(0.1,1) + round(0.1,1) + round(0.1,1) == round(0.3,1)	--> False

# Way-2 (using absolute tolerance):
print('----Way-2----')
x = 0.1 + 0.1 + 0.1
y = 0.3
print(format(x, '0.20f'))
print(format(y, '0.20f'))
print('abs tolerance: ', format(x-y, '0.20f'))
a = 10000.1 + 10000.1 + 10000.1
b = 30000.3
print(format(a, '0.20f'))
print(format(b, '0.20f'))
print('abs tolerance: ', format(a-b, '0.20f'))

abs_tol = 0.000000000000001
print(math.fabs(x-y) < abs_tol)
print(math.fabs(a-b) < abs_tol)

# In the way-2, it is true for case-1 but not for case-2, but we take in relative terms that the a and b are equal
# as the left hand side is large. This creates a less creditable method.

# Way-3 (using relative tolerance):
#	- maximum allowed difference between the two numbers, relative to the larger magnitude of the to numbers
# def is_equal(num1, num2, rel_tol = 0.00001):
# 	 abs_tol = 0.000000000000001
# 	 tol = max(rel_tol * max(math.fabs(num1), math.fabs(num2)), abs_tol)
#  	 return True if math.fabs(num1-num2) < tol else False
num1 = 30000.2
num2 = 30000.3
print('----Way-3----')
# print(is_equal(num1,num2))

# we already have a method is math module for that
print(math.isclose(1000.0000001, 1000.0000002))
print(math.isclose(0.00001, 0.00002, abs_tol=0.00001))
print(math.isclose(1000.01, 1000.02, rel_tol=0.01, abs_tol=0.00001))
print(math.isclose(0.01, 0.02, rel_tol=0.01, abs_tol=0.00001))

# Floats Coercing to Integers
# 	- this is the way of dealing with the data loss
# Few Method used are:
#	- math.trunc()
#	- math.floor()
#	- math.ceil()
#	- round()

# Rounding of floats
#	- round function can also helps in rounding the float to float
# Python provides a built-in function: round(x, n=0), This will round the number to the closest mulitple of 10^-n and you
# might think of this as rounding to a certain number of digits after the decimal point which would work for positive n.
# But n can also be negative! If n is not specified, then it defaults to zero and return an int.
# For float both + n and - n are useful but for int only - n values are useful and _ n values are useless.
a = 5435.256
print(
	round(a,3),
	round(a,2),
	round(a,1),
	round(a,0),
	round(a,-1),
	round(a,-2),
	round(a,-3),
	round(a,-4),
	round(a,-5)
	)
