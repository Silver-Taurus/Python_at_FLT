#! /usr/bin/env python3

''' Python Script to understand the Python topics Scopes, Closures and Decorators '''

# Scopes and Namespaces
#   - When an object is assigned to a variable --> a = 10
#     that variable points to some object and we say that the variable (name) is bound to that object.
#     That object can be accessed using that name in various parts of our code.
# But not just anywhere!!!
# The variable name and it's binding (name and object) only 'exist in specific parts of our code, the
# portion of code where that name/binding is defined, is called the lexical scope of the variable and
# these bindings are stored in namespaces.



# The Global Scope
#   - The global scope is essentially the module scope.
#     It spans a single file only.
# There is no concept of a truly global (across all the modulesin our entire app) scope in Python.
# The only exception to this are some of the built-in globally available objects, such as:
#   True, False, None, dict, print, etc...
# The built-in and global va riables can be used anywhere inside our module, including inside any function.
#   - Global scopes are nested inside the built-in scope.

# If you reference a variable name inside a scope and Python does not find it in that scope's namespace then
# it will go and search in the namespace of super/enclosing scope and the process repeats till the built-in
# scope is achieved.

# Examples:
#   - module1.py
#       print(True)
#     Python does not find True or print in the current (module/global) scope. So, it looks for them in the
#     enclosing scope --> built-in and Finds them there.
#
#   - module2.py
#       print(a)
#     Python does not find a or print in the current (module/global) scope. So, it looks for them in the enclosing
#     scope --> built-in and Finds print, but not a --> run-time error.
#
#   - module3.py
#       print = lambda x: 'hello {}!'.format(x)
#       s = print('world')
#     Python finds print in the module scope, so it uses it !!!
#     s --> hello world!
#     This change of the functioning of a built-in function is called as Masking.
#     In order to use the built-in print we have to delete the global/module scope print function.



# The Local Scope
#   - When we create functions, we create variable names inside those function (using assignments).
#     Variables defined inside a function are not created until the function is called, hence, there will be no scope
#     created for the function at its time of defining or creation. The scope for the function is created every time
#     the function is called. 

# Example:
#   def my_func(a, b):
#       c = a*b
#       return c
# At the time of compile when the function is created, the compile just determines that a, b and c will go to the local scope
# but the scope itself is created when the function is called.
# So when we call the functuion at different times the different local scopes are created for the same function.    



# Namespace lookups
#   - When requesting the object bound to a variable name:
#     e.g. print(a)
#   - Python will try to find the object bound to the variable:
#       - in the current local space first
#       - works up the chain of enclosing scopes



# Nested Scope
#   - Scopes are often nested. Since, there can be multiple local scopes inside a local scope itself.

# Example:
a = 10
def my_func(b):
    print(True)     # built-in scope
    print(a)        # global (or module) scope
    print(b)        # local scope
my_func(100)

# Reference counting concept with scopes
#   - When my_func(var) finishes running, the scope is gone too! and the referece count of the object
#     var was bound to (referenced) is decremented. We can also say that var goes out of scope.



# Accesing the global scope from a local scope
#   - When retrieving the value of a glboal variable from inside a function, Python automatically searches
#     the local scope's namespace, and up the chain of all enclosing scope namespaces.

# Now modifying a global variables value form inside the function:
print('---- Accessing the global scope from a local scope ----')
b = 0
def test_func():
    b = 100     # assignment --> Python interprets this as a local variable (at compile-time)
    print(b)    # so the local variable b masks the global variable b.              
test_func()
print(b)

# The global keyword
#   - We can tell Python that a variable is mant to be scoped in the global scope by using the global keyword.
# Example:
a = 0
def my_func2():
    global a
    a = 100
my_func2()
print(a)

# Global and Local Scoping
#   - When python encounters a function definition at compile time it will scan for any labels (variables) that
#     have values assigned to them (anywhere in the function) if the label has not been specified as global,
#     then it will be local.
#   - Variables that are referenced but not assigned a value anywhere in the function will not be local, and Python
#     will, at run-time, look for them in enclosing scopes.
print('---- Global and Local Scoping')
a = 10
def func1():
    print(a)        # a is referenced only in entire function, at compile time --> `a` non-local
func1()
print(a)

def func2():
    a = 100         # assignment, at compile time --> `a` local
    print(a)
func2()
print(a)

def func3():
    global a        # assignment, at compile time --> `a` global
    a = 100
    print(a)
func3()
print(a)

def func4():
    print(a)        # assignment, at compile time --> `a` local but we are trying to reference it before we have declare or define it
    a = 100         # so it will gonna give a run-time error, when we call func4()

# Example:
def var_create():
    global var              # since the var variable is not declared and assigned in the global scope, it will create one.
    var = 'hello world'    
    return
# print(var) --> will give the run-time error as the variable var is not present in the glboal scope (and in built-in scope) yet.
var_create()
print(var)

# Re-defining built-in functions
def print(x):
    return 'hello {}'.format(x)
string = print('world')     # calls the global print() function
del print                   # removing the global scope print() function
print(string)               # calls the built-in print() function



# Additional Scopes: code within code-blocks
# Like in C++:
#   for(int i = 0; i < 10; i++) {
#       int x = 2 * i ;   
#   }
#   std::cout<<x;
#
# This will give an error as for the above code x has a scope within the for code-block and not in the global scope.

# While in Python:
print('---- Additional Scopes ----')
for i in range(10):
    x = 2*i
print(x)
# The x variable is available in the global scope as in Python the variables don't go in or out of scope in the code-blocks.



# Non-local Scopes
#   - This happens when we start defining a function within another function.
# Example:
#   def outer_func():
#       # code
#       def inner_func():
#           # code
#       inner_func()
#   outer_func()

# Now in the above example, both functions have access to the global and built-in scopes as well as their respective local scopes.
# But the inner function also has access to its enclosing scope - the scope of the outer function. That scope is neither local (to inner_func)
# nor global - it is called a nonlocal scope.
print('---- Non-Local Scopes ----')
a = 0
def outer_func():
    a = 10
    def inner_func():
        print(a)
    inner_func()
outer_func()
# In this case the a that is to be printed will neither have a local scope or global scope but will have a non-local scope.



# Modifying nonlocal variables
def outer_func2():
    x = 'hello'
    def inner_func2():
        nonlocal x
        x = 'python'
    inner_func2()
    print(x)
outer_func2()
# In the above example the inner_func2() will modify its enclosing (nonlcal) scope variable x from 'hello' to 'python', using nonlocal keyword.

# Nonlocal Variables
#   - Whenever Python is told that a variable is nonlocal, it will look for it in the enclosing local scopes chain until ir first encounters the
#     specified variable name.
# Beware: It will only look in local scopes, it will not look in the global scope.
def outer():
    x = 'hello'
    def inner1():
        def inner2():
            nonlocal x
            x = 'python'
        inner2()
    inner1()
    print(x)
outer()
# In this case, the nonlocal x refers the outer() function's x, so the x will change from 'hello' to 'python'.

del outer

def outer():
    x = 'hello'
    def inner1():
        x = 'python'
        def inner2():
            nonlocal x
            x = 'Silver'
        print('inner1 (before): ', x)
        inner2()
        print('inner1 (after): ', x)
    inner1()
    print('outer: ', x)
outer()
# In this case, the nonlocal x from inner2() refers to x of inner1() so the value of inner1() function's x will chagne from 'python' to 'Silver' but there
# will be no change in the value of x of the outer function.



# Free Variables and Closures
#   - Functions defined inside another function can access the outer (nonlocal) variables
#
#       def outer():
#           x = 'python'
#           def inner():
#               print('{} rocks!'.format(x))    --> this x refers to the one in the outer's scope, this nonlocal variable x is called a free variable.
#           inner()
#       outer()
# This will give the output: python rocks!
# In the above case of inner functions, the inner function will not be created till the outer function is called.
#
# When we consider inner, we really are looking at:
#   - the function inner
#   - the free variable x
# So both the function and the free variable should be bound together and this is called a Closure.

del outer

# Returning the inner function (it will be a higher order function)
def outer():
    a = 100
    x = 'python'
    def inner():
        a = 10      # will have a direct reference
        print('{} rocks!'.format(x))
    return inner    # So, in this case we are not returning the inner function but the inner closure.
fn = outer()    # Then, here fn is a closure and outer function finished its running.
print('---- Closures ----')
fn()    # Will give the output --> python rocks!
# When we called fn, at that time Python determined the value of x in the extended scope, but notice that outer had finished running before we called fn,
# it's scope was gone.
# But still it works, this is because of closure.

# Python Cells and Multi-Scoped Variables
#   - In the above code the value of x is shared between two scopes:
#       - outer
#       - closure (inner)
# The label x is in two different scopes but always reference the same 'value', Python does this by creating a `cell` as an intermediary object.
# Cell is an object that has memory address like any other object, but what it does is it basically contains a reference to another object, which is in this
# case is str object, x.
# In the above case, x in the outer function is a direct reference to the str object containing 'python' under normal circumstances but here we have a closure
# when python sees a closure in the outer function, it creates a cell object, to which x of the outer and x of the inner both points which inturns point to the 
# str object. This is also the case with the nonlocal scope variables (and not just with the closures).
# In effect, both variables x (in outer and inner), point to the same cell, When requesting the value of the variable, Python will 'double-hop' to get to the final value,
# as python know that we are dealing with cells.

# Closures
#   - You can think of the closures as function plus an extended scope that contains the free variables.
# The free variable's value is the object the cell points to - so thata could change over time! Every time the function in the closure is called and the free variable is 
# referenced: Python looks up the cell object, and then whatever the cell is pointing to.
# Whenever you create the outer function it creates a cell object and references it. It look for value when you call it.

# Introspection
print('---- Closure introspection ----')
print(fn.__code__.co_freevars)      # will give the tuple containing the free varaibles associated with the closure
print(fn.__closure__)       # It gives us a tuple of cell object which tells us the address of cell object and the address to which it is pointing.

del outer

def outer():
    x = 'python'
    print(hex(id(x)))
    def inner():
        print(hex(id(x)))
        print('{} rocks!'.format(x))
    return inner

fn = outer()
fn()
# In this case also, python do some heavy work for and gives us the indirect reference back, i.e., the address of str object in the above case.
# Though we don't need of dealing with memory addresses but it is many times helpful in debugging.

# Modifying the free variables
def counter():
    count = 0
    def inc():
        nonlocal count      # count is a free variable, it is bound to the cell count
        count += 1
        return count
    return inc
print('---- Modifying Free variables ----')
fn = counter()      # fn --> inc + count --> 0
print(fn())    #  output --> 1     count's (indirect) reference changed from the object 0 to the object 1
print(fn())    #  output --> 2     count's (indirect) refernce changes again!

# Multiple instances of Closures
#   - Every time we run a function, a new scope is created. If that function generates a closure, a new closure is created every time as well.
f1 = counter()
f2 = counter()
# Since f1 and f2 have their own scopes for counter function, then the closures generated by them will have their different cell objects at different
# memory locations.
print('---- Multiple instances of Closures ----')
print(fn.__closure__)
print(f1.__closure__)
print(f2.__closure__)
# Though the indirect reference will be same for all three of the instances of closures as 0 or 1 are the singleton objects.

del outer

# Shared Extended Scopes
def outer():
    count = 0
    def inc1():
        nonlocal count      # count is a free variable - bound to count in the extended scope
        count += 1
        return count
    def inc2():
        nonlocal count      # count is a free variale, here also - bound to the same count
        count += 1
        return count
    return inc1, inc2
# So in the above case the extended scope is shared between two closures. The above two closures have the shared free variable count.
print('---- Shared Extended Scopes ----')
f1, f2 = outer()
print(f1())
print(f2())
# We may think this shared extended scope is highly unusual... but it's not!

# Example (Three different closures - no shared scopes):
def adder(n):
    def inner(x):
        return x + n
    return inner
add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)
print(add_1(10))
print(add_2(10))
print(add_3(10))

# Caveat-Example (using loop for reducing repetition):
print('---- Caveat Example ----')
adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)      # here n is free variable, so we created a closure.
# In the above case, we will get three closures to be generated with each iteration as the free variable n will gonna point to the same
# cell object for all three closures but the value that cell object pointing to will change with each iteration.

# So, in above example we are doing the same functionality as that of the previous example but using Shared extended scope between the three
# closures generated with every iteration as they all have same cell object whose value is changing with iteration.
# But because of this there comes a caveat, that the value of n will be changed to 3 with the last iteration and when we call any of the
# closure it will have the shared indirect reference to that changed value 3 which will create a logical error.
print(adders[0](10))
print(adders[1](10))
print(adders[2](10))

# But we want to capture the value of n for each closure separately, so what we can do is:
print('---- Caveat solution ----')
adders = []
for n in range(1, 4):
    adders.append(lambda x, y=n: x + y)     # In this case we deal with caveat with another caveat of default cases, since we know the default values
                                            # are evaluated only once. So, in this case we are not even creating a closure but a function.
print(adders[0](10))
print(adders[1](10))
print(adders[2](10))


# Nested Closures
# Example: we have to give the start value and the step value
def incrememter(n):
    # inner + n is a closure
    def inner(start):
        cur = start
        # inc + cur + n is a closure
        def inc():
            nonlocal cur    # free variable (cur)
            cur += n        # free variable (n)
            return cur
        return inc
    return inner
print('---- Nested Closures ----')
fn = incrememter(2)                 # it gives the inner 
print(fn.__code__.co_freevars)      # gives 'n', n = 2
inc_2 = fn(100)                     # it gives the inc
print(inc_2.__code__.co_freevars)   # gives 'cur' and 'n'
print(inc_2())
print(inc_2())
# In the above example inner function has a free variable n even though we dont have declared it directly inside the fucntion, but it has the
# n varaible contained in it, indirectly via inc function.



# Closure - Applications (Example)

# Non-Closure Code (Using Class)
#   - Class have overheads for storage, methods, initialisation, self, etc...
class Averager:
    def __init__(self):
        self.numbers = []
    
    def add(self, number):
        self.numbers.append(number)
        return sum(self.numbers) / len(self.numbers)

print('\n\n---- Closure Application ----')
print('---- Application-1 ----')
a = Averager()
print(a.add(10))
print(a.add(20))
print(a.add(15))
b = Averager()
print(b.add(20))
print(b.add(30))
print(b.add(25))

# Closure Code
#   - Here also, we can make separate instances of closure as a and b, as we know that each time the function is called it has a different scope. So, 
#     the address of cell object a and b will be different in the output.
def averager():
    numbers = []
    def add(number):
        numbers.append(number)
        return sum(numbers) / len(numbers)
    return add

a = averager()
print(a.__closure__)
print(a(10))
print(a(20))
print(a(15))
b = averager()
print(b.__closure__)
print(b(20))
print(b(30))
print(b(25))

# More Efficient Closure Code 
#   - (Same can also be used for improvement of Non-Closure Code)
def averager2():
    total, count = 0, 0
    def add(number):
        nonlocal total, count
        total += number
        count += 1
        return total/count
    return add

a = averager2()
print(a.__closure__)
print(a(10))
print(a(20))
print(a(15))



# Making Timer for getting the performance using Non-Closure (Class) and Closure way
from time import perf_counter
from time import sleep
class Timer:
    def __init__(self):
        self.start = perf_counter()
    def poll(self):
        return perf_counter() - self.start

print('---- Application-2 ----')
t1 = Timer()
sleep(1)
print(t1.poll())
sleep(2)
print(t1.poll())

# But, since we are only interested in the single function poll, then there is no use of calling it specifically every time,
# rather we can make our object callable to that functioning.
class Timer2:
    def __init__(self):
        self.start = perf_counter()
    def __call__(self):
        return perf_counter() - self.start

t1 = Timer2()
sleep(1)
print(t1())
sleep(2)
print(t1())

# Closure way
def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll

t2 = timer()
sleep(1)
print(t2())
sleep(2)
print(t2())



# Making a counter to count how many times a function is called in a program
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('{} has been called {} times.'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

print('---- Application-3 ----')
counter_add = counter(add)
print(counter_add.__closure__)
print(counter_add.__code__.co_freevars)
print(counter_add(10, 20))
print(counter_add(152434, 234234))

counter_mul = counter(mul)
print(counter_mul.__closure__)
print(counter_mul.__code__.co_freevars)
print(counter_mul(10, 20))
print(counter_mul(1524, 234))

del counter

# Storing the result for above code rather than displaying it
counters = dict()
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        counters[fn.__name__] = count
        return fn(*args, **kwargs)
    return inner

counter_add = counter(add)
counter_mul = counter(mul)
print(counter_add(10, 20))
print(counter_add(152434, 234234))
print(counters)
print(counter_mul(10, 20))
print(counter_mul(1524, 234))
print(counters)

del counter

# Improving the function, so that we can have a generalised counter function
def counter(fn, counters):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        counters[fn.__name__] = count
        return fn(*args, **kwargs)
    return inner

c = dict()
counter_add = counter(add, c)
counter_mul = counter(mul, c)
print(counter_add(10, 20))
print(counter_add(40, 50))
print(counter_add(152434, 234234))
print(c)
print(counter_mul(2, 5))
print(counter_mul(10, 20))
print(counter_mul(1524, 234))
print(c)

# Now, we can also update the `c` for any other function also
def fact(n):
    product = 1
    for i in range(2, n+1):
        product *= i
    return product

def fact2(n):
    return 1 if n < 2 else n * fact2(n-1)

counter_fact = counter(fact, c)
print(counter_fact(5))
print(counter_fact(6))
counter_fact2 = counter(fact2, c)
print(counter_fact2(5))
print(counter_fact2(6))
print(c)



# Upgrading Functions
#   - We can also upgrade the function code by replacing it with it's closure code

#---- Way-1 (Overwirting functions) ----
add = counter(add, c)
mul = counter(mul, c)
fact = counter(fact, c)
fact2 = counter(fact2, c)

# Here the counts will be reseted as, the function's have been changed actually
print('\n\n---- Upgrading Function ----')
print('---- Way-1 (Overwriting functions) ----')
print(add(100, 200))
print(mul(121, 11))
print(fact(10))
print(fact2(5))
print(c)

# In the above upgraded case, the fact will work same as that of, in the case of non-upgraded version of it, but the fact2 will behave a bit differently
# as before the count was for the fact2 - recursive function in the closure which works similar to the fact-1 function in closure, i.e., just counting it 
# for one whole evaluation. But after upgrading fact2 to its closure, we have updated the fn paramter to the closure function due to which in case of recursion
# every time the function calls itself a new count is added. 

del add
del mul
del fact
del fact2
del Timer
del Timer2
del timer
del counter
del counters
del c

#---- Way-2 (Decoratoring Using @) ----
#   - We essentially modify or upgrade our function by wrpping it inside another fucntion that added some functionality to it, so we can also that we decorated our
#     fucntion with another function and we call that another function as decorator function.
#   - In general a decorator function:
#       - takes a function as an argument
#       - returns a closure
#       - the closure usually accepts any combination of parameters
#       - runs some code in the inner function (closure)
#       - the closure function calls the original fucntion using the arguments passed to the closure
#       - returns whatever is returned by that function call

# Decorators and @ symbol
#   - As we have the counter function which is a decorator and we can decorate our add, mul, fact and fact2 functions with it, using: add = counter(add, c)
#
#   - In general, if func is a decorator fucntion, we decorate another fucntion say my_func using:
#       my_func = func(my_func)
#     after defining the my_func function.
#
#   - This is so common that Python provides a convenient way of writing that as:
#       @func
#       def my_func():
#           # code
#
# Hence with the help of @ we can define and decorate the my_func at the same time, but both of the ways will give you the same thing.
#
#   - When we decorate the my_func with the func decorator the function name (my_func.__name__) will change from my_func to inner.
#     Similar problem will occur with help(my_func) and we would have lost all the information and docstring of my_func and we left with the info of inner.
#     Even using the inspect module's signature does not yield better results.
#
#   - One approach of fixing it is:
#       def counter(fn):
#           count = 0
#           def inner(*args, **kwargs):
#               nonlocal count
#               count += 1
#               counters[fn.__name__] = count
#               return fn(*args, **kwargs)
#           inner.__name__ = fn.__name__
#           inner.__doc__ = fn.__doc__
#           inner.__annotations__ = fn.__annotations__
#           return inner
#     But this doesn't fix losing the function signature - doing so would be quite comlicated.
#
#   - Instead, Python provides us with a special function that we can use to fix this (The functools.wrap function). The functools module has a wraps function that
#     we can use to fix the metadata of our inner fucntion in our decorator. In fact, the wraps function itself is a decorator. But it needs to know what was our 'original'
#     function - in this case - fn.
#
#       from functools import wraps
#       def counter(fn):
#           count = 0
#           def inner(*args, **kwargs):
#               nonlocal count
#               count += 1
#               counters[fn.__name__] = count
#               return fn(*args, **kwargs)
#           inner = wraps(fn)(inner)
#           return inner
#     or,
#
#       from functools import wraps
#       def counter(fn):
#           count = 0
#           @wraps(fn)
#           def inner(*args, **kwargs):
#               nonlocal count
#               count += 1
#               counters[fn.__name__] = count
#               return fn(*args, **kwargs)
#           return inner
#            

print('---- Way-2 (Decorating Using @) ----')
def counter(fn):
    from functools import wraps
    count = 0
    @wraps(fn)      # fixing metadata using decorator wraps
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {} (id={}) has been called {} times.'.format(fn.__name__, id(fn), count))
        return fn(*args, **kwargs)
    return inner

@counter        # using decorator
def add(a:int, b:int = 0):
    ''' adds two values '''
    return a + b

@counter        # using decorator
def mul(a:int, b:int = 1):
    ''' multiplies two values '''
    return a * b

print(add(2, 3))
print(add(100, 200))
print(mul(3, 5))
print(mul(324, 23))

del counter



# Decorator Application (Timing)
def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        elapsed = perf_counter() - start

        args_ = [str(x) for x in args]
        kwargs_ = ['{}={}'.format(k,v) for (k,v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print('{}({}) took {:.6f}s to run.'.format(fn.__name__, args_str, elapsed))

        return result
    return inner

print('\n\n---- Decorator Application (Timing) ----')

# fibonacci function
#   - recursion
#   - loop
#   - reduce

#---- Way-1 (Recursion)----
#   @timed
#   def calc_recursive_fib(n):
#        return 1 if n <= 2 else calc_recursive_fib(n-1) + calc_recursive_fib(n-2)
#   print(calc_recursive_fib(3))
#
# Since, we have used recursion for a decorated function it will time the decorated fucntion for each step. So to make it correct
# we will time a container for recursive function.
def calc_recursive_fib(n):
    return 1 if n <= 2 else calc_recursive_fib(n-1) + calc_recursive_fib(n-2)

@timed
def recursive_fib(n):
    return calc_recursive_fib(n)
print(recursive_fib(35))

#---- Way-2 (Loop)----
@timed
def fib_loop(fn):
    fib_1, fib_2 = 1, 1
    for i in range(3, n+1):
        fib_1 , fib_2 = fib_2, fib_1 + fib_2
    return fib_2
print(fib_loop(35))

#---- Way-3 (Reduce)----
@timed
def fib_reduce(n):
    from functools import reduce
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]) ,dummy, initial)
    return fib_n[0]
# Here, we are not using the iterable (and so as n)
print(fib_reduce(35))

del fib_reduce



# Decorator Application (Logger, Stacked Decorators)
def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now()
        result = fn(*args, **kwargs)
        print('{}: called {}'.format(run_dt, fn.__name__))
        return result
    
    return inner

@logged
def func1():
    pass

@logged
def func2():
    pass

print('\n\n---- Decorator Application (Logger, Stacked Decorators) ----')
print('---- Logger ----')
func1()
func2()

# We can also stack decorators (for example: fib_reduce is decorated by @timed and @logged)
@logged
@timed
def fib_reduce(n):
    from functools import reduce
    initial = (1, 0)
    dummy = range(n)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]) ,dummy, initial)
    return fib_n[0]
print('---- Stacked Decorators ----')
print(fib_reduce(30))
# In the above case the timed output comes first, that is because before getting the output in the logged decorator the timed
# function is executed. This all happens because of the placement of the print function. So in reality the logged decorator 
# executes first and not the timed decorator.

# Example-1 (for understanding the calling of stacked Decorators)
def dec_1(fn):
    def inner():
        print('Running dec_1')
        return fn()
    return inner

def dec_2(fn):
    def inner():
        print('Running dec_2')
        return fn()
    return inner

# Here, both the decorators dec_1 and dec_2 will work for the functions that do not take any arguments.
@dec_1
@dec_2
def my_func():
    print('Running my_func')
# Also be written as, my_func = dec_1(dec_2(my_func))
print('---- Example-1 ----')
my_func()

del dec_1
del dec_2
del my_func

# Example-2 (for understanding the calling of stacked Decorators)
def dec_1(fn):
    def inner():
        result = fn()
        print('Running dec_1')
        return result
    return inner

def dec_2(fn):
    def inner():
        result = fn()
        print('Running dec_2')
        return result
    return inner

# Here, also both the decorators dec_1 and dec_2 will work for the functions that do not take any arguments.
# Also, we can stack decorators as much as we want.
@dec_1
@dec_2
@logged
@timed
def my_func():
    print('Running my_func') 
# Also be written as, my_func = dec_1(dec_2(my_func))
print('---- Example-2 ----')
my_func()

del timed

# Exmaple-3 (Memoization)
#   - Decorators can do a lot more than just providing some extra stuff to the function, i.e., they can also modify the behaviour function.
def fib_memoize():
    cache = {1: 1, 2: 1}
    def calc_fib(n):
        if n not in cache:
            print('Caclulating fib({})'.format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib

f = fib_memoize()
print('---- Example-3 ----')
print(f(10))

# Now rewriting the above code such a way, tha twe can use a decorator. The above code is very close to decorator but is implemented as a closure only.
def memoize(fn):
    cache = dict()
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner 

@memoize
def fib(n):
    print('Calculating the fib({})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(10))
print(fib(11))  

# In the above case, the function to be decorated (or to be cached in this case), can be any function which needs to be memoized and takes one argument.
# So it is very generalised now.
# Hence, we can use it for fatorial also.

@memoize
def fact(n):
    print('Calculating fact({})'.format(n))
    return 1 if n < 2 else n*fact(n-1)

print(fact(6))
print(fact(7))

del fib

# So what we have not done here is to limit the size of the cache. If the size goes very large then the tradeoff between the space and computation will no longer hold.
# In this case we can limit the size of the cache and apply the Least-Recent-Used (LRU) approach to maintain the cache. So, as we go on more generalise approach
# of memoization he complexity of the decorator code increases, and hence there comes the Python, having it for us in its functools module.
from functools import lru_cache
@lru_cache(maxsize=8)    # since lru_cache is a paramterized decorator, which takes the max size of cache (by default - 128), so we have to call it.
def fib(n):
    print('Calculating the fib({})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(8))
print(fib(16))
print(fib(8))
print(fib(9))
# Generally, we should keep the cache sie in the power of 3 it is more efficient. We can also keep it None, which in turns means unlimited cache size, i.e., until it runs
# out of memory.

del fib



# Decorator Parameter and Decorator Factories
#   - Now as we know the timing for each time may differ, so we can take average tiem for n number of tiems
#     entered by the user but for that, we will have a parameterised decorator.

# Now, this timed decorator will calcaulate average time to be taken for the function to execute.
#   def timed(fn):
#       from time import perf_counter
#       from functools import wraps
#
#       @wraps(fn)
#       def inner(*args, **kwargs):
#           total_elapsed = 0
#           for i in range(10):
#               start = perf_counter()
#              result = fn(*args, **kwargs)
#               total_elapsed += (perf_counter() - start)
#           avg_elapsed = total_elapsed / 10
#           print(avg_elapsed)
#           return result
#       return inner
#
# The problem with the above code is that repetition 10 is hardcoded. So what we can try is to take reps argument.

#   def timed(fn, reps=10):
#       from time import perf_counter
#       from functools import wraps
#
#       @wraps(fn)
#       def inner(*args, **kwargs):
#           total_elapsed = 0
#           for _ in range(reps):
#               start = perf_counter()
#               result = fn(*args, **kwargs)
#               total_elapsed += (perf_counter() - start)
#           avg_elapsed = total_elapsed / reps
#           print(avg_elapsed)
#          return result
#       return inner
#
# In this we call the decorator this way:
#   my_func = timed(my_func, 5)
# will work. But,
#   @timed(5)
#   def my_func():
#       ...
# Will not gonna work. Because, it is calling timed(10) first and timed is expecting two parameters not one. So this syntax will fail.

# So, what we an do is to provide a outer decorator for timed which takes the value of reps and give the timed decorator back.
# Nested Closures to rescue!
#   - Here, the outer function (timed) is not itself a decorator, instead it returns a decorator when called and any arguments passed to outer
#     (timed) can be referenced (as free variables) inside our decorator. Hence, it is called a Decorator Factory.
def timed(reps=10):
    def timed_dec(fn):
        from time import perf_counter
        from functools import wraps

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for _ in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / reps
            print(avg_elapsed)
            return result
        return inner
    return timed_dec

print('\n\n---- Decorator Paramter ----')

@timed()
def fib_loop(fn):
    fib_1, fib_2 = 1, 1
    for i in range(3, n+1):
        fib_1 , fib_2 = fib_2, fib_1 + fib_2
    return fib_2
print(fib_loop(12))



# Decorator Application - Decorator Class
#   - This is because we can an object can be made callable
def dec_fac(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('Decorated function called: a={}, b={}'.format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec

@dec_fac(10, 20)
def my_func(s):
    print('Hello {}'.format(s))
my_func('World')

#   class MyClass:
#       def __init__(self, a, b):
#           self.a = a
#           self.b = b
#       def __call__(self, c):
#           print('called a={}, b={}, c={}'.format(self.a, self.b, c))
#   obj = MyClass(10, 20)
#   obj(30)
# will give the output:
#   called a=10, b=20, c=30

# Here we can make the class MyClass as a decorator factory and function __call__ as a decorator which means the callable
# object itself will be a decorator.
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self, fn):
        def inner(*args, **kwargs):
            print('Decorated fucntion called a={}, b={}'.format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner

@MyClass(10, 20)
def my_func(s):
    print('Hello {}'.format(s))
print('\n\n---- Decorator Application ----')
print('---- Decorator Class ----')
my_func('World')



# Decorator Application - Decorating Class
#---- Exmaple-1 ----
from fractions import Fraction
f = Fraction(2, 3)
print('---- Decorating Class ----')
print(f.denominator)
print(f.numerator)
#   Fraction.is_integer = lambda self: self.denominator == 1      
# This way, we can add the instance method dynamically at the run time. This is also called as Monkey-Patching.
#   print(f.is_integer())   --> will give false.

# Now doing the above code (Monkey Patching) as an external fucntion (decorator)
def dec_is_integer(cls):
    cls.is_integer = lambda self: self.denominator == 1
    return cls

Fraction = dec_is_integer(Fraction)
print(f.is_integer())

#---- Eaxmple-2 ----
from datetime import datetime

def info(self):
    results = []
    results.append('time: {}'.format(datetime.now()))
    results.append('Class: {}'.format(self.__class__.__name__))
    results.append('id: {}'.format(hex(id(self))))
    
    for k,v in vars(self).items():
        results.append('{}: {}'.format(k, v))  
    return results

def debug_info(cls):
    cls.debug = info
    return cls

@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    def say_hi(self):
        return 'Hello {}'.format(self.name)

p = Person('Silver', 1999)
p.debug()

# As from the above two example we can see that in first exmaple rather than using decorator, we can directly add the property,
# while when are needed to reuse it we can make a decorator like in exmple-2.
