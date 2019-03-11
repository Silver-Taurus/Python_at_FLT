#! /usr/bin/env python3

''' Description on Numbers '''

import sys
import time
from fractions import Fraction
import math
import decimal
from decimal import Decimal
import cmath

# Compelx Numbers
# Costructors
#	- complex(x, y)
# 	x -> real part and y -> imaginary part
#	literals: x + yj or x + yJ
# Here, x and y are stores as floats
print('\n\n----Complex----')
a = complex(1, 2)
b = 1 + 2j
print('complex(1, 2) == 1 + 2j', a == b)

# Some instance property and methods
print('Real part of a: ', a.real)
print('Img part of a: ', a.imag)
print('Conjugate of a: ', a.conjugate())

# Equality operators (==, !=) are supported
# Comparison operators such as <, >, <= and >= are not supported

# Functions in math module will not work
# 	- Instead we have to use cmath module

# cmath methods
print('Rectangular to Polar: ', cmath.phase(a))
print('Polar to rect: ', cmath.rect(math.sqrt(2), math.pi/4)) 

# Euler's Identity
#	e^(i * pi) + 1 = 0
print('Euler\'s Identity: ', cmath.exp(cmath.pi * 1j) + 1)
print('Euler\'s Identity: ', cmath.isclose(cmath.exp(cmath.pi * 1j) + 1, 0, abs_tol=0.00001))
