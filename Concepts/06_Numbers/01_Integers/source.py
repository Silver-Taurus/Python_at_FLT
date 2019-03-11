#! /usr/bin/env python3

''' Description on Numbers '''

import sys
import time
from fractions import Fraction
import math
import decimal
from decimal import Decimal
import cmath

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
