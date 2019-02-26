#! /usr/bin/env python3

''' Description on Numbers '''

import sys
import time
from fractions import Fraction
import math
import decimal
from decimal import Decimal

# Four main types of numbers:
#   --> Integer Numbers (Z) - 0, +1, -1, +2, -2, ...    -   int
#   --> Rational Numbers (Q) - {p/q | p,q --> Z, q not 0}   -   fractions.Fraction
#   --> Real Numbers (R) - 0, -1, 0.125, 1/3, pi, ...   -   float, decimal.Decimal
#   --> Complex Numbers (C) - {a+bi | a,b --> R}    -   Complex

# In python, there exists an additional fifth type:
#   --> Boolean truth values - 0(False), 1(True)    -   bool



# Integers: the `int` data type
# Integers are represented internally using base-2(binary) digits, not decimal.

# The largest (base-10) integer number that can be represented using 8 bit:
# for unsigned it is 2**8 - 1 = 255
# for signed, the 8th bit is used to denote the positive or negative number, then,
# the largest value is 2**7 - 1 = 127

# In a 32-bit Os:
#   --> memory spaces (bytes) are limited by their address number -> 32 bits
#       so we get 4294,967,296 bytes of addressable memory
#           =  4GB , which is theoretical limit.

# Some languages (such as Java, C, ....) provide multiple distinct integer data types that use
# a fixed number of bits.
# Python does not work this way, The int object uses a variable number of bits.
# In python we can use 4 bytes, 8 bytes, 12 bytes, etc.
# Since int are actually objects, there is a further fixed overhead per integer.
#Theoretically limited only by the amount of memory available.

# In a 32-bit OS if we are adding two integers having the size larger than the 32-bit than it will
# gonna take more than one operation to perform it, so we will do it in chunks. But this is seamless to us.
 
# displaying integer overhead and size taken after the overhead
print('Integer overhead (for 0): ', sys.getsizeof(0))
print('Integer overhead (for 1): ', sys.getsizeof(1))
print('Size taken by int (for value = 1): ', sys.getsizeof(1) - sys.getsizeof(0))
print('Integer overhead (for 2**1000): ', sys.getsizeof(2**1000))
print('Size taken by int (for value = 2**1000): ', sys.getsizeof(2**1000) - sys.getsizeof(0))

# Performace checking
def calc(a):
    ''' Arbitary function for calculating Search or enter a cloud sourced URLtime '''
    for i in range(10000000):
        a * 2
start = time.perf_counter()
calc(10)
end = time.perf_counter()
print('Operation time (for 10): ', end-start)

start = time.perf_counter()
calc(2**10000)
end = time.perf_counter()
print('Operation time (for 2**10000): ', end-start)



# Integer support all the standard arithmetic operations:
#   - addition (+)
#   - subtraction (-)
#   - multiplication (*)
#   - division (/)
#   - exponent (**)

# When we do the operations other than division we get the integer back, but in case of division of
# two int we get the float as the result.

# So we get two more operators for performing the operations on the integers:
#   - floor division (//)
#   - modulo or remainder (%)


# Floor division
#   - The floor of a real number 'a' is the largest integer <= a
#   floor(3.14) -> 3
#   floor(1.999) -> 1
#   floor(-3.1) -> -4
# So, --> a // b = floor(a/b).



# Integer Constructors and Bases
#	- int class provides multiple constructors
# Type-1: Takes number
print('\nInteger Constructors and Bases')
print('----Type-1----')
a = int(10)
b = int(-10)
c = int(10.9)	# truncation
d = int(-10.9)	# truncation
print(a, b, c, d)

# Type-2: Takes string
print('----Type-2----')
e = int('10')	# int('123')	--> (123) of base-10
print(e)
# When we ue a string, constructor has an optional second parameter: base --> 2 <= base <= 36.
# If base is not specified, the default is base-10, as in the example above.
f = int('1010', base=2)		# or int('1010', 2)
g = int('534',   base=8)
h = int('A12F', base=16)
i = int('a12f', base=16)
j = int('A', base=11)
print(f, g, h, i, j)

# But for int('B', 11) --> ValueError: invalid literal for int() with base 11: 'B'.
# This is because for base-11 the highest value is A.


# Reverse-Process: changing an integer from base 10 to another base.
# built-in functions: bin()

# Type-3: Direct initialisation
print('----Type-3----')
num = 0b101
print(num)

# A function to give the digits of a number in a base from base10
def from_base10(n, b):
	if b < 2:
		raise ValueError('Base b must be >=2')
	if n < 0:
		raise ValueError('Number must be >= 0')
	if n == 0:
		return [0]
	digits = []
	while  n > 0:
		# m, n = n%b, n//b	--> Tuple notation
		n, m = divmod(n, b)
		digits.insert(0, m)
	return digits

print('\n----Testing User Defined Function to give the digits of a number in a base from base10----')
print(from_base10(10, 2))

# A function to give the equivalent value for the digits of a number using digit map
def encode(digits, digit_map):
	if max(digits) >= len(digit_map):
		raise ValueError('digit_map is not long enough to encode the digits...')
	# encoding = ''
	# for d in digits:
	#	encoding += digit_map[d]
	# return encoding
	return ''.join([digit_map[d] for d in digits])

print('\n----Testing User Defined Function to give the equivalent value for the digits of a number using digit map----')
print(encode([15,15], '0123456789ABCDEF'))

# Hard Code the function for conversion of a number from base 10 to any other base
def rebase_from10(number, base):
	digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	if base < 2 or base > 36:
		raise ValueError('Invalid base: 2 <= base <= 36')
	sign = -1 if number < 0 else 1
	number *= sign

	digits = from_base10(number, base)
	encoding = encode(digits, digit_map)
	if sign == -1:
		encoding = '-' + encoding
	return encoding
print('\n----Testing User Defined Function to convert a number from base 10---')
test_num = rebase_from10(10, 2)
print(test_num)
print(int(test_num, base=2))



# Rational Numbers (Fractions)
x = Fraction(3, 4)
y = Fraction(6, 10)
print('\n\n----Fractions----')
print('x = {}, y = {}'.format(x, y))		# --> Fractions are automaticaly reduced.

# Constructor of Fraction class
#	- Fraction(numerator=0, denominator=1)
#	- Fraction(other_fraction)
#	- Fraction(float)
#	- Fraction(decimal)
#	- Fraction(string)		--> Fraction('22/7')

# Fractions support arithmetic operators: +, -, *, / and result in Fraction objects as well.
# We can also get the numerator and denominator of Fractions
print('Numerator of x = ', x.numerator)
# Float objects have finite precision --> any float object can be written as a fraction

# Even though pi and sq.root(2) are both irrational but interanally they are stored as float so
# we can convert them into the fractions as a very precise approximate value of the pi or sq.root(2)
# but not the actual value.

# Converting a float to a Fraction has an important caveat
# 1/8 has an exact float representation --> Fraction(0.125) = Fraction(1, 8)
# 3/10 does not have exact float representation,
# format(0.3, '.5f')	--> 	0.30000
# format0.3, '.25f')	-->		0.299999999999999888977698

# Given a Fraction object, we can find an approximate equivalent fraction with a constrained denominator
# using --> limit_denominator(max_denominator=1000000) instance method
# we can find the closest rational number (which could be precisely equal) with a denominator that
# does not exceeds max_denominator.
print('\n----Float caveat exmaple----')
print('Normally --> Fraction(0.3) is: ')
print(Fraction(0.3))
print('After using the limit_denominator method: ')
print(Fraction(0.3).limit_denominator(max_denominator=100))

# Checking for pi
print('\n----Fraction for pi----')
x = Fraction(math.pi)
print('Normal Fraction of pi in python: ', x, float(x))
print('Rational approximation for max_denominator = 10: ', x.limit_denominator(10), float(x.limit_denominator(10)))
print('Rational approximation for max_denominator = 100: ', x.limit_denominator(100), float(x.limit_denominator(100)))
print('Rational approximation for max_denominator = 500: ', x.limit_denominator(500), float(x.limit_denominator(500)))
print('Rational approximation for max_denominator = 1000: ', x.limit_denominator(1000), float(x.limit_denominator(1000)))
print('Rational approximation for max_denominator = 5000: ', x.limit_denominator(5000), float(x.limit_denominator(5000)))
print('Rational approximation for max_denominator = 10000: ', x.limit_denominator(10000), float(x.limit_denominator(10000)))
print('Rational approximation for max_denominator = 50000: ', x.limit_denominator(50000), float(x.limit_denominator(50000)))

# Using Constructors for Fraction
a = Fraction()
b = Fraction(5)
c = Fraction(5, 7)
d = Fraction(c)
e = Fraction(0.125)
f = Fraction('0.125')
g = Fraction('22/7')
print('\n----Testing the Fraction constructors----')
print(a, b, c, d, e ,f ,g)



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
# 	- this deals with the way of dealing with the data loss
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



# Decimals
#	- It is used to remove the shortcomings of the float class
# 	Fraction class can also do the work here, but it is much slow than float due to more number of computations.
# 	- Decimals have a context that controls certain aspects of working with decimals, like:
#		- precision during arithmetic operations
#		- rounding algorithm
#	This context can be global	--> the default context re temporary (local)  --> sets temporary settings without
# 	affecting the global settings.
# 	This can be done as:
#		- default context --> decimal.getcontet()
#		- local context --> decimal.localcontext(ctx=None) --> returns a context manager (use a with statement)

# Precision and Rounding
# ctx = decimal.getcontext()	--> context (global in the case)
# ctx.prec	--> get or set the precision (value is in int)
# ctx.rounding()  --> get or set the rounding mechanism (value is a string)
#	--> In this we have the following rounding algorithms:
#			- ROUND_UP (rounds away from zero)
#			- ROUND_DOWN (rounds towards zero)
# 			- ROUND_CEILING (round to ceiling, towards + inf)
# 			- ROUND_FLOOR (round to floor, towards -inf)
# 			- ROUND_HALF_UP (rounds to nearest, ties away from zero)
# 			- ROUND_HALF_DOWN (rounds to nearest, ties towards zero)
#			- ROUND_HALF_EVEN (rounds to nearest, ties to even)
print('\n\n----Decimals----')
print('----Context----')
g_ctx = decimal.getcontext()
print(g_ctx)
g_ctx.rounding = decimal.ROUND_HALF_DOWN
# or g_ctx.rounrding = 'ROUND_HALF_UP'
print(g_ctx)
print('type(decimal.getcontext()): ',type(g_ctx))
print('type(decimal.localcontext()): ',type(decimal.localcontext()))
# which is similar to default (or global) context in this case

x = Decimal('1.25')
y = Decimal('1.35')

# using context manager of localcontext
print('----Context Manager----')
with decimal.localcontext() as ctx:
	ctx.prec = 6
	ctx.rounding = decimal.ROUND_HALF_UP
	print(ctx)
	print(decimal.getcontext())
	print(round(x, 1))
	print(round(y, 1))
print(round(x, 1))
print(round(y, 1))

# Constructors and Contexts
#	- The following type of constructors are available:
#		- Decimal(int)
#		- Decimal(other Decimal object)
# 		- Decimal(strings)
#		- Decimal(tuples)
#		- Decimal(float), but not preferable since the float gives an approximate values in many cases.

# Using the tuple constructor
#	- In this, there are three pieces --> sign, digits and exponent
#	Then, we give the value as (s, (d1,d2,d3,...), exp), where s = 0 when value is +ve and s = 1 when value is -ve.

# Context precision and the Constructor
#	- Context precision affects mathematical operations
#	- Context precision does not affect the constructor
print('----Context manager and Constructor----')
decimal.getcontext().prec = 2
a = Decimal('0.12345')
b = Decimal((0, (1,2,3,4,5), 5))
c = a + b
print(c)

# Mathematical Operations
# 	- Normally -10//3  --> -4 while Decimal(-10)//Decimal(3)  --> Decimal(-3)

# The Algorithm used to actually perform integer division
#	- a: dividend	b: divisor
#	- figure out the sign of the result
#	- use absolute values for divisor and dividend
#	- keep subtracting b from a as long as a >= b
#	- return the signed number of times this was performed.

# Example: n = -135 and d = 4
#					Integer					Decimal
#	-135//4			-34						-33
#	-135%4			 1						-3

# Not all functions defined in math module are defined in Decimal class.
# Though we can use the math module with decimal object, then, it will first convert Decimal object
# to the float object and then apply the function. But it will lose the whole main reason of using
# the Decimal class for precision system. 

print('----Mathematical Operations----')
decimal.getcontext().prec = 28
x = 0.01
x_dec = Decimal('0.01')

root = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root, '1.27f'), format(root_mixed, '1.27f'), root_dec)
print(format(root * root, '.27f'), format(root_mixed * root_mixed, '.27f'), root_dec * root_dec)

x = -10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))

x = Decimal(-10)
y = Decimal(3)
print(x//y, x%y)
print(divmod(x, y))
print(x == y * (x//y) + (x%y))

# The Decimal class doesn't have trignometric functions