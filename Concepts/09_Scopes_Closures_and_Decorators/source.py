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



# Accesing the global scope form a local scope
#   - When retrieving the value of a glboal variable from inside a function, Python automatically searches
#     the local scope's namespace, and up the chain of all enclosing scope namespaces.

# Now modifying a global variables value form inside the function:
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
    print(a)        # assinment, at compile time --> `a` local but we are trying to reference it before we have declare or define it
    a = 100         # so it will gonna give a run-time error, when we call func4()
