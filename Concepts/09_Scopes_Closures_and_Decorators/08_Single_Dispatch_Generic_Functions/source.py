#! /usr/bin/env python3

''' Python Script to understand the Python topics Scopes, Closures and Decorators '''

#--- Single Dispatch Generic Function ---- 
#   - Use case (where we have to format/handle the data for html)



#---- Code-1 ----
from html import escape

def html_escape(arg):
    return escape(str(arg))

def html_int(a):
    return '{}(<i>{}</i>)'.format(a, str(hex(a))) 

def html_real(a):
    return '{:.2f}'.format(round(a, 2))

def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')

def html_list(l):
    items = ('<li>{}</li>'.format(html_escape(item)) for item in l)
    return '<ul>\n' + '\n'.join(items) + '</ul'

def html_dict(d):
    items = ('<li>{}={}</li>'.format(k, v) for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '</ul>'

print('---- Code-1 ----')
print(html_str('''this is
multi-line strings with special characters: 10 < 100 '''))
print(html_int(255))
print(html_escape(3+10j))

# Single Dispatcher Fucntion (but is not generic)
def htmlize(arg):
    from decimal import Decimal

    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        return html_escape(arg)

print(htmlize(100))
print(htmlize(['Python rocks!!!', (100, 200, 300), 100]))
# Now the above implementation for our use case, gives us a output that's little off... as we have passed the list
# as a arg, which is is received by the htmlize and the hmtl_list is called which is escaping the contents of the list.
# But we want is, that the html_list function will again check inside the list taht is passed as arg so for that, we can use
# htlmize fucntion in place of html_escape in line-22.

# Note: In python, we can reference or call a function (say f-2) in a body of another fucntion (f-1) even if that f-2 is not defined yet.
# And it is toatally fine as long as, the f-2 function will be created or defined before the the another function f-1 is beign called.

del html_list
del html_dict
del htmlize



#---- Code-2 ----
# So the improved version of above code is:
def html_list(l):
    items = ('<li>{}</li>'.format(htmlize(item)) for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul'

def html_dict(d):
    items = ('<li>{}={}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def htmlize(arg):
    from decimal import Decimal

    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        return html_escape(arg)

print('\n---- Code-2 ----')
print(htmlize(100))
print(htmlize(['''Python 
rocks!!!''', (100, 200, 300), 100]))

# Now, if we want to format the set we have to add html_set and than edit the htmlize fucntion again.
# So every time we add some functionality we have to change the code and the code itself will loke 
# much more untidy as it keeps on increasing in text-size.

del htmlize



#---- Code-3 ----
# So a much better approach is to maintain a dictionary...
def html_set(arg):
    return html_list(arg)

def htmlize(arg):
    from decimal import Decimal

    registry = {
        object: html_escape,
        int: html_int,
        float: html_real,
        Decimal: html_real,
        str: html_str,
        list: html_list,
        tuple: html_list,
        dict: html_dict,
        set: html_set
        }

    fn = registry.get(type(arg), registry[object])  # But in this case, if some class is inherited from the list
                                                    # but since it is not list the case will fail
    return fn(arg)

print('\n---- Code-3 ----')
print(htmlize(100))
print(htmlize([1, 2, 3]))

# Now the code seems tidy but there is still the problem of re-writing the code every time we add a new function.

del html_escape
del html_int
del html_real
del html_str
del html_list
del html_dict
del html_set
del htmlize



#--- Code-4 ---
#   - Using a decorator/closure to make a single dispatcher `generic` function, so that instead of hard-coding we
#     can just inject the new fucntions.
from decimal import Decimal

def single_dispatch(fn):
    registry = {}
    registry[object] = fn
    
    def decorated_function(arg):
        return registry.get(type(arg), registry[object])(arg)
    
    # Decorator-Factory (or Paramterized decorator)
    def register(type_):
        # register_decorator is a decorator that does not modify the the functionality of other function (fn).
        def register_decorator(fn):
            registry[type_] = fn    # In place of this there can be a, register_decorated_function also which can have its own implementation.
            return fn    # We are simply returning the fucntion back.
        return register_decorator

    # Making the Decorator Factory, an attribute of a decorated functions, so we can access it.
    decorated_function.register = register

    # In order to view the registry we will make a dispatch function
    def dispatch_registry(type_):
        return registry.get(type_, registry[object])

    # Making the getter fucntion as an attribute
    decorated_function.dispatch_registry = dispatch_registry

    return decorated_function

@single_dispatch
def htmlize(arg):
    return escape(str(arg))

print('\n---- Code-4 ----')
print(htmlize('1 < 100'))
print(htmlize(100))

# Calling a decorator factory (register) and getting a decorator back (register_decorator) from inside a decorated function (htmlize).
from numbers import Integral    # Integral is for all non-decimal number types (including - int, Bool, etc.) 
@htmlize.register(Integral)
def html_integral(a):
    return '{}(<i>{}<i>)'.format(a, str(hex(a)))

from numbers import Real        # Real is for all real numbers types (including - flaot, Decimal, Fraction, etc.) 
@htmlize.register(Real)
def html_real(a):
    return '{:.2f}'.format(round(a, 2))

@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/>\n')

from collections.abc import Sequence
@htmlize.register(Sequence)
def html_sequence(l):
    items = ('<li>{}</li>'.format(htmlize(item)) for item in l)
    return '<ul>\n' + '\n'.join(items) + '</ul'

@htmlize.register(dict)
def html_dict(d):
    items = ('<li>{}={}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

print('...After Registering...')
print(htmlize.dispatch_registry(int))
print(htmlize(100))

# So, if we go for more generic approach then there can be multiple bugs related to our program as our code is also being getting complex.
# From the above codes, we got a understanding about the the working of a single_dispatch_generic_function and now we can directly implement
# the Python version of it.

del htmlize



#---- Code-5 ----
from functools import singledispatch

@singledispatch
def htmlize(arg):
    return escape(str(arg))

print('\n---- Code-5 ----')
print(htmlize.registry)
print(htmlize.dispatch(str))

@htmlize.register(Integral)
def html_integral(a):
    return '{}(<i>{}<i>)'.format(a, str(hex(a)))

print(htmlize.dispatch(int))
print(htmlize.dispatch(bool))
print(htmlize.dispatch(Integral))

@htmlize.register(Sequence)
def html_sequence(l):
    items = ('<li>{}</li>'.format(htmlize(item)) for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul'

print(htmlize([1, 2, 3]))
print(htmlize((1, 2, 3)))

# print(htmlize('python'))
#   - But their is a problem: `str` is also a Sequence type. Here in the above code we will get a RecursionError.
#     This is because the 'python' is also a sequence we will get the items in it - 'p', 'y', 't', 'h', 'o', 'n'
#     which are also strings, so we will recurse again... and hence max-recursion-limit crosses and we get an error.

print(htmlize.dispatch(list))
print(htmlize.dispatch(tuple))
print(htmlize.dispatch(str))

# To remove the above bug, we will defined a specific str functionality
@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/>\n')

print(htmlize.dispatch(str))
print(htmlize('''python
rocks!!!'''))