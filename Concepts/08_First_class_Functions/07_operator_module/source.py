#! /usr/bin/env python3

''' First Class Functions '''

# The operator module
#   - As we have used reduce() function for l = [2, 3, 4] to give the mulitplication output of all the numbers in the list.
#     This is something that happens quite often, so the operator module was created. So, this module is a convenience module.
#     We can use our own function or lambda expressions as well in place of it.

# For Arithmetic Functions:
#   - add(iterable)
#   - mul(iterable)
#   - pow(iterable)
#   - mod(iterable)
#   - floordiv(iterable)
#   - neg(a)
#   and many more...

# If the work to be done using functions or lambdas expression are simple and related to operators it is there in operator module.
# As it only gives the function equivalent for the simple operator related expressions.

# For Comparison and Boolean Operators:
#   - lt(a, b)
#   - le(a, b)
#   - gt(a, b)
#   - ge(a, b)
#   - eq(a, b)
#   - ne(a, b)
#   - is_(a, b)
#   - is_not(a, b)
#   - and_(a, b)
#   - or_(a, b)
#   - not_(a)

# For Sequence/Mapping Operators:
#   - concat(s1, s2)
#   - contains(s, val)
#   - countOf(s, val)
#   - getitem(s, i)
#   - setitem(s, i, val)
#   - delitem(s, i)

# For Item Getters
#   - The itemgetter function returns a callable
#        getitem(s, i)  --> takes two paramters, and retusn a value: s[i]
# while, itemgetter(i)  --> returns a callable which takes one parameter: a sequence object
#                           this creates a partial function.
from operator import itemgetter
l = [1, 2, 3, 4, 5, 6]
s = 'python'
f = itemgetter(1)
print('\n\n---- Operator module ----')
print('-- itemgetter --')
print(f(l), f(s))

g = itemgetter(1, 3, 4)     #  In itemgetter, we can pass more than one index.
print(g(l), g(s))

# Attribute Getters
#   - The attrgetter function is similar to itemgetter, but is used to retrieve object attributes.
#   - It also returns a callable, that takes the object as an argument.
# Suppose my_obj is an object with three properties:
#   my_obj.a -> 10
#   my_obj.b -> 20
#   my_obj.c -> 30
#   
#   f = attrgetter('a')
#   f(my_obj)   --> 10
# Then, if the object or instance have that property it will return it no matter what it is.
# Similar, to itemgetter it can also take multiple values (or property/attribute names).
#   
#   f = attrgetter('a', 'c')
#   f(my_obj)   --> (10, 30)
#
# Can also be called directly:
#   attrgetter('a', 'b', 'c')(my_obj)

# Calling another Callable
#   - Consider the str class that provides the upper() method:
from operator import attrgetter
s = 'python'
f = attrgetter('upper')     # In this case, f is a callable and it will get the upper property of str instance, but will not call it.
print('-- attrgetter --')
print(f(s))     # gives the `upper` method after calling the f
print(f(s)())   # since we are getting back the method after calling f, we will have to call it once again to perform its functionality.
# or we can do that directly,
#   print(attrgetter('upper')(s)()) --> PYTHON

# Another way is to use: methodcaller function
#   - which wraps the extra calling in the attrgetter for us.
from operator import methodcaller
print('-- method caller --')
print(methodcaller('upper')(s))
# And it can also handle more than one arguments.

# Exmaples of operator module codes
from operator import mul
print('---- Exmaples ----')
print(mul(2, 3))
print(reduce(mul, [2,3,4,5]))

class OpTestClass:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def test(self, c=30):
        print('test method running...')
        print(self.a, self.b, c)

obj = OpTestClass()
obj.test()
print(obj.a)
print(obj.b)

prop_a = attrgetter('a')
print(prop_a(obj))

# we can use obj.a but if we are gonna take the property as an input or if we have to store the property to some variable
# then:
my_var = 'a'
# obj.my_var    --> will be wrong!!!
# so what we can do is:
print(attrgetter(my_var)(obj))
# or --> prop_a = attrgetter(my_var) and then, prop_a(obj).

# In the above case we have use the varaible name as prop_a because once the attrgetter gets evaluated its functioning will not gonna change even if
# the value of my var is changed !!!

# Another use case (sort the complex numbers based on the real part)
l = [5-10j, 3+3j, 2-100j]
print(sorted(l, key=lambda x: x.real))
print(sorted(l, key=attrgetter('real')))

# Another use case (sorting these tuples on the basis of the first number in these tuples)
l = [(2,3,4), (1,3,5), (6,), (4,100)]
print(sorted(l, key=lambda x: x[0]))
print(sorted(l, key=itemgetter(0)))

# Using methodcaller and attrgetter to pass arguments
obj.test(100)
methodcaller('test', 100)(obj)
attrgetter('test')(obj)(100)