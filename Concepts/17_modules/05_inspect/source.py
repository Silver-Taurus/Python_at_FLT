#! /usr/bi/env python3

''' Python script to test-use inspect module/library '''

import inspect
import requests
import module
from module import Planet

# Uses:
#   - Helps in knowing, how to use a brand-new python package
#   - Helps in knowing, what methods/classes does this package provide

# The inspect module which let us inspect any complex python program, As we know that any 
# program contains many classes or methods which provide different functionality to the program.
# These logical sections can be inspected easily using the inspect module.
planet = Planet('Naboo', 300000, 8, 'Naboo System')
print('Name: {}'.format(planet.name))
print(planet.spin('a very high speed'))

# Inspecting the module
print()
print(inspect.getmembers(planet))
print()
print(inspect.ismodule(planet))
print()
print(inspect.ismodule(module))
print()
print(inspect.isclass(Planet))
# and many others...


# The interpreter stack
#   - When the following function return 'frame records', each record is a tuple of six items.
#       - frame object
#       - the filename
#       - the line number of the current file
#       - the function name
#       - a list of lines of context from the source code
#       - the index of the current line within that list