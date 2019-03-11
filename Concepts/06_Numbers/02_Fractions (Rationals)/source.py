#! /usr/bin/env python3

''' Description on Numbers '''

import sys
import time
from fractions import Fraction
import math
import decimal
from decimal import Decimal
import cmath

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
