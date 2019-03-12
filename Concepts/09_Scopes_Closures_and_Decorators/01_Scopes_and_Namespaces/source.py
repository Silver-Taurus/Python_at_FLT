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
