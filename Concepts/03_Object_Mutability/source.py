#! /usr/bin/env python3

''' Pytohn script for understanding the object mutability '''

# Object Mutability
#   --> An object whose internal state can be changed is called mutable.
#   --> An object whose internal state cannot be changed is called immutable.

# But we have to be careful with the container type immutable objects because they
# may or may not contain immutable objects inside them. Resulting in different
# behaviour then their expected immutable behaviour.

t = (1, 2, 3)
# Tuples are immutable: elements cannot be deleted, inserted or replaced.
# In this case, both the container(tuple) and all its elements(ints) are
# immutables.

# But consider this:
print('Tuple-Content Mutability situations...')
a = [1, 2]
b = [3, 4]
n = (a, b)
print(n)
# Tuples are immmutable but in this case, lists are mutable: elements can be
# deleted, inserted or replaced
a.append(3)
b.append(5)
print(n)
# So the value inside the tuple changes, even though the number of values inside
# a tuple do not change directly. So we have to be careful while using the immutability.


# Function arguments and mutability
#   --> immutable objects are safe from unintended side-effects
# Example:
print('\nString immutability example...')
def process1(s):
    print('Initial s # = {}'.format(id(s)))
    s = s + ' world'
    print('Final s # = {}'.format(id(s)))
my_var = 'hello'    # has a module scope
print(id(my_var))
print(my_var)
process1(my_var)      # passing my_var's reference to the process function
# And then store the refrence in the variable s, but since it is a string
# when modifying the string in the statement s = s + ' world' a reference to the
# new memory location is created and allocated to s and the original my_var
# reference's data remain safe and my_var will keep referencing to the original
# memory address.
print(id(my_var))
print(my_var)
# Thus we have the safety in this case.

#   --> mutable objects doesn't have safety
# Example:
print('\nList mutability example...')
def process2(lst):
    print('Initial lst = {}'.format(id(lst)))
    lst.append(100)
    print('Final lst = {}'.format(id(lst)))
my_list =   [1, 2, 3]
print(id(my_list))
print(my_list)
process2(my_list)
print(id(my_list))
print(my_list)
# Same thing is happening in this case, we are passing the reference that the variable
# my_list is storing to the function process but since the list is an immutable, the
# change that append performs will also change the internal value of my_list in the module
# scope.

#   --> The mutable object working can also take place with the tuple if it is containg a mutable
#       objects inside it.
# Example:
print('\nTuple immutability but content mutabiity situation...')
def process3(t):
    print('Initial t = {}'.format(id(t)))
    t[0].append(3)      # assuming the first element of the tuple is a list
    print('Final t = {}'.format(id(t)))
my_tuple = ([1, 2], 4, 5, 6)
print(id(my_tuple))
print(my_tuple)
process3(my_tuple)
print(id(my_tuple))
print(my_tuple)


# Shared References and Mutability
#   --> The term shared references is the concept of two variables referencing the
#       same object in memory (i.e. having the same memory address).

# In the case of immutables sharing a refernece the following happens:
# Example1:
# a = 10
# b = a

# Example2:
# def process(v):
#   ...
# t = 10
# process(t)
# Then, in this case v is also referencing the same address as the t.

# Example3:
# a = 10
# b = 10
# In this case also, the references for both a and b will be the same memory address
# until, we modify the value assigned to it (that is, by changeing the reference to new
# address having a different value for the immutable).
# This working is done by the Python Memory Manager. But this behaviour doesn't always happen
# Sometimes it does and sometimes it doesn't.
 
# In the case of mutables however we ahve to remain careful as if we are sharing the references
# between two or variables then, changing the value through one reference will modify the internal
# value at the reference itself and thus will be reflected through the shared references also.
# Example1:
# a = [1, 2, 3]
# b = a
# a.append(100)
# This will make b also --> [1, 2, 3, 100] as both are referencing to the same memory address and list
# are mutables, so the internal values can be changed and are refelected using both the variables.
# This is also known as Shallow Copy.

# Example2:
# The same effect is shown when the list is passed in the function as shown in the above examples.
# As the function make a shared reference for the list.

# Example3:
# a = [1, 2, 3]
# b = [1, 2, 3]
# In this case, both the variables will have different references as we have declared it separately,
# the python memory manager knows that they are mutables, hence should be allocated with different
# memory addresses. Unlike the immutables they will not have any chance of having same references.



# Mutation Problem
l1 = ["hi"]
print(l1)
l2 =  l1
l2 += ["bye"]
print(l2)
print(l1)
# It's Mutability in action. Whenever you assign a variable to another variable of mutable datatype, 
# any changes to the data are reflected by both variables. The new variable is just alias for the old variable.
# This is true for only mutable datatypes.
