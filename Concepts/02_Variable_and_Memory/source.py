#! /usr/bin/env python3

''' Describes about variables and memory '''
import sys
import ctypes
import gc

# variables in python are always references to addresses in memory
print('Memory-Address exmaples...')
my_var_1 = 10
# It creates an object in the memory and stores the value 10 in that memory
# and my_var_1 is the name or reference or alias given to that memory address
# so my_var_1 does not referred to 10 but the memory address (say 0x1000).

# The print() function works the way:
#   --> Firstly it will get the memory address the my_var_1 variable
#       refrencing at and then retrieve the data stored at the memory address.
print(my_var_1)

# In python, we can find out the memory address referenced by a variable by using
# the id() function. This will return a base-10 number. We can convert this base-10
# number to hexadecimal, by using the hex() function.
print(hex(id(my_var_1)))

greeting = 'hello'
print(greeting)
print(hex(id(greeting)))


# Reference Counting
#   --> This deals with, how many variables are referencing a particular memory
#       address and thus we keep a count of references for a memory address out of
#       memory allocated to python script.
other_var = my_var_1
# When the reference count drops to 0, then the python memory manager free that memory
# location for us.

# Finding the reference count for any referenced memory address using variable
#   --> sys.getrefcount(my_var_1)
# But using this function, also increases reference count for that memory location by one.

# Another way of finding the reference count for any referenced memory address
# using c library function:
#   --> ctypes.c_long.from_address(integer).value
# In this we pass address inside the from_address(integer) function and not the
# reference.

# Example for method-1
print('\nReference Counting...')
a = [1, 2, 3]
print(id(a))
print(sys.getrefcount(a))   
# this will give the output 2, so we need to remember to subtract one from the answer.

# Example for method-2
# Making a wrapper function
def ref_count(address: int):
    return ctypes.c_long.from_address(address).value
print(ref_count(id(a)))
# this will give the output 1, so we get the right answer for the reference.
# since the id(a) is evaluating first and then the address is getting passed.

# Further example of method 2
b = a
print(id(a))
print(id(b))
print(ref_count(id(a)))

b = 20
print(id(b))
print(ref_count(id(a)))

a_id = id(a)
a = None
print(ref_count(a_id))
# Now the memory count should be 0, but in real, since the address is being free
# for other processes, so it is possible that in place of being 0 it can be used by
# some other processes and thus some value accounts with the ref_count of that address.

 
 # Garbage Collection
# In this the unused memory is freed by garbage collector.
# This is used because in some cases, the python memory manager is
# not able to free the memory.

# Example: Circular references
#                Object1   .-->  Object2
# my_var --> .-> var_1   --'     var_2   --.     
#            '-----------------------------'
# In this case that even if my_var is destoryed both the objects
# will not be destroyed by the python memory manager of python because
# tbhe referecne count for the objects will not be 0.
# This is a memory leak.
# This problem is resolved by garbage collector.


# Garbage Collector
#   --> It can be controlled programmatically using the gc module
#   --> by default it is turned on
#   --> you may turn it off if you're sure your code does nt create
#       circular references - but beware!!!
#   --> We turn it off due to performance issues, since it runs periodically
#       on its own
#   --> you can call it manuall, and even do your own cleanup

# It generally works fine, but not always, for python <3.4:
#   --> if even one of the object in the circular reference has a destructor.
#       the destruction order of the objects may be important.
# The garbage collector mark those object as uncollectable and if that object has
# circular references then the memory leak will remain. But these problems are fixed
# above or in the 3.4 version.

# example of circular references when garbage collector is disabled
print('\nCircular Referencing...')
def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not Found"

class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {}, b: {}'.format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {}, a: {}'.format(hex(id(self)), hex(id(self.a))))

# disabling the garbage collector    
gc.disable()
my_var = A()
print(hex(id(my_var)))
print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))

a_id = id(my_var)
b_id = id(my_var.b)
print(hex(a_id))
print(hex(b_id))

print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))

# removing the reference from my_var
my_var = None
print(ref_count(a_id))
print(ref_count(b_id))
print(object_by_id(a_id))
print(object_by_id(b_id))

# running gc manually
gc.collect()
print(object_by_id(a_id))
print(object_by_id(b_id))
print(ref_count(a_id))
print(ref_count(b_id))


# Dynamic vs Static Typing

#  In a statically typed language like - java, etc. the variable name is the reference
# which has a particualr data type, so the reference will be set to store the fixed amount of
# memory in the heap.

# While in case of a dynamically typed language like python, the variable is purely a
# reference does not have any particular data type which will fix the size of the reference in the
# memory until we made it statically typed. In this case, the when we use type() function the python
# will look at the object or value it is referencing and tells the type of variable.
# Due to which in python we do not change the type of a variable but change the reference that the variable
# is referencing at.

# Example
print('\nType Checking...')
a = 10
print(a)
print(type(a))
a = [1, 2, 3]
print(a)
print(type(a))
a = lambda x: x**2
print(a(2))
print(type(a))


# Variable Re-Assignment
print('\nVariable Re-Assignment examples...')
my_var = 10
print(my_var)
print(id(my_var))
my_var = 15
print(my_var)
print(id(my_var))
# In the above case the value of my_var is not changed but what happens
# is that, new memory location is created with the value of 5 and the my_var
# is referenced to it.
my_var = my_var + 5
print(my_var)
print(id(my_var))
# Similar thing happens here, value 5 is not being added to the current my_var address
# but a new address is being allocated with the valye my_var + 5 and my_var is being then
# referenced to it.
my_var = my_var - 10
new_var = 10
print(my_var)
print(new_var)
print(id(my_var))
print(id(new_var))
# In this case, we have a different value for my_var = 10,
# my_var = 15 and my_var = 15 + 5 = 20. But when we subtract 10 out of 20
# we will get my_var = 10 which if not get destroyed by the memory manager
# till the time, my_var will be re-assigned to the initial memmory location.
# also if new variables are assigned the same value, the python we assign the same 
# memory address as reference to the new_var variable also.


# Variable Equality
#   --> We can think of variable equality in two fundamental ways:
#           1.  Memory Address
#           2.  Object state (data)
# For Comparing Memory Address:
# `is` operator also called as identity operator can be used to check
# the equality.
print('\nVariable Equality examples...')
var_1 = 10
var_2 = var_1
print(var_1 is var_2)
# Negation is done by `is not`
# `a is b` is equivalent to `id(a) == id(b)`

# For Comparing the Object state:
# we can use `==` operator
print(var_1 == var_2)
# Negation is done by `!=`

# Other Example:
a = 10
b = 10.0
print(a is b)
print(a == b)


# None Object
#   --> The None object can be assigned to variables to indicate that they are
#       not set (in the way we would expect them to be.) i.e. an empty value 
#       (or null pointer).
# But the None object is a real object that is managed by the python memory manager
# Furthermore, the memory manager will always use a shared reference when assigning
# a variable to None i.e. All the None variables in your module will have the reference
# to same memory address.
print('\nNone example...')
a = None
b = None
c = None
print(a is b)
print(a is c)
# Also we can check whether any variable is not set, as for a program the memory addres of
# the None will be same. So we can directly check the memort address of any variable we want
# to that of the None.
print(a is None)