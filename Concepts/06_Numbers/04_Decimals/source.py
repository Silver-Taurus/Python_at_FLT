#! /usr/bin/env python3

''' Description on Numbers '''

import sys
import time
from fractions import Fraction
import math
import decimal
from decimal import Decimal
import cmath

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

# The Decimal class doesn't have trignometric functions

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

# Decimals: Performance Considertations
# There are some drawbacks to the Decimal class vs the float class
#	- not as easy to code: construction via strings or tuples
# 	- not all mathematical functios that exist in the math module have a Decimal counterpart
#	- more memory overhead (relatively)
#	- performance: much slower than floats (relatively)
print('----Decimals: PerformanceConsiderations----')
a = 3.1415
b = Decimal('3.1415')
print('float memory usage: ', sys.getsizeof(a))		# 24 bytes
print('decimal memory usage: ', sys.getsizeof(b))	# 104 bytes

def run_float(n=1):
	for i in range(n):
		a = 3.1415

def run_decimal(n=1):
	for i in range(n):
		a = Decimal('3.1415')

n = 10000000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float creation time: ', end - start)		# approx 0.14 sec

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal creation time: ', end - start)		# approx 1.3 sec

def run_float_op_add(n=1):
	a = 3.1415
	for i in range(n):
		a + a 

def run_decimal_op_add(n=1):
	a = Decimal('3.1415')
	for i in range(n):
		a + a

n = 10000000
start = time.perf_counter()
run_float_op_add(n)
end = time.perf_counter()
print('float addition operation time: ', end - start)	# approx 0.23 sec

start = time.perf_counter()
run_decimal_op_add(n)
end = time.perf_counter()
print('decimal addition operation time: ', end - start)		# approx 0.5 sec 

def run_float_op_div(n=1):
	a = 3.1415
	for i in range(n):
		a / a 

def run_decimal_op_div(n=1):
	a = Decimal('3.1415')
	for i in range(n):
		a / a

n = 10000000
start = time.perf_counter()
run_float_op_div(n)
end = time.perf_counter()
print('float division operation time: ', end - start)	# approx 0.23 sec

start = time.perf_counter()
run_decimal_op_div(n)
end = time.perf_counter()
print('decimal division operation time: ', end - start)		# approx 1 sec

def run_float_sqrt(n=1):
	a = 3.1415
	for i in range(n):
		math.sqrt(a) 

def run_decimal_sqrt(n=1):
	a = Decimal('3.1415')
	for i in range(n):
		a.sqrt()

n = 10000000
start = time.perf_counter()
run_float_sqrt(n)
end = time.perf_counter()
print('float sqrt time: ', end - start)		# approx 0.5 sec

start = time.perf_counter()
run_decimal_sqrt(n)
end = time.perf_counter()
print('decimal sqrt time: ', end - start)	# approx 24 sec
