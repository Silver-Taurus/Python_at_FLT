#! /usr/bin/env python3

''' Python script on Tuples as a Data Structures (or Data Records) '''

# Tuples are:
#   - Read only lists that can also be interpreted as data records (where psition of value has meaning).

# Tuples vs Lists vs Strings
#             Tuples                    |                Lists                  |       Strings
#   ------------------------------------|---------------------------------------|----------------------------
#     - containers                      |      containers                       |    containers
#                                       |                                       |
#     - order matters                   |      order matters                    |    order matters
#                                       |                                       |
#     - can be heterogeneous or         |      heterogeneous                    |    homogeneous
#       homogeneous                     |      or homogenous                    |
#                                       |                                       |
#     - indexable                       |      indexable                        |    indexable
#                                       |                                       |
#     - iterable                        |      iterable                         |    iterable
#                                       |                                       |
#     - immutable                       |      mutable                          |    immutable
#        - fixed length                 |       - length can change             |     - fixed length
#        - fixed order                  |       - order of elements can change  |     - fixed order
#        - cannot do in-place sorts     |       - can do in-place sorts         |     - cannot do in-place sorts
#        - cannot do in-place reversals |       - can do in-place reversals     |     - cannot do in-place reversals

# Mostly, Tuple contains heterogenous data and lists contain homogenous data.



# Tuples as Data Records
#   - Thinking of tuple as data record
#   - Because tupls, strings, integers are immutable we are guaranteed that the data and the data structure for lodon,
#     new_york and beijing will never change.

london = ('London', 'UK', 8_780_000)
new_york = ('New York', 'USA', 8_500_000)
beijing = ('Beijing', 'China', 21_000_000)

# Making a city record
cities = [london, new_york, beijing]
print('---- Tuples as Data Records ----')
print(cities)



# Extracting data from Tuple
# One-Way is - Indexing:
#   - city = london[0], country = london[1], population = london[2]
# Another way is - Unpacking:
#   - city, country, population = new_york



# Dummy Variables
#   - This is just a convention which is used for denoting the data we are not interested in.
#       city, _, population = beijing
#   - It's also used in extended unpacking too as shown in below examples.

record = ('DJIA', 2018, 1, 19, 25987.35, 26071.71, 25942.83, 26071.72)

#   symbol, year, moth, day, open, high, low, close = record
#
# But what if we are only intereste in the symbol, year, month, day and close fields
#
#---- Way-1 ----
#   symbol = record[0]
#   year = record[1]
#   month = record[2]
#   day = record[3]
#   close = record[7]
# But this looks really bad!!!
#
#---- Way-2 ----
#   symbol, year, moth, day, close = record[0], record[1], record[2], record[3], record[7]
# It looks good but is a bad code to be implemented as in this case, we are first packing the values and then unpacking them!!!
#
#---- Way-3 ----
symbol, year, month, day, *_, close = record
print('\n---- Dummy Variable ----')
print(symbol, year, month, day, close)
print(_)
# Much cleaner code and good to implement.



# Named Tuple
#   - Since we have seen, how we interpreted tuples as data records. The position of the object
#      contained in the tuple gave it meaning
# For ex: Representing a 2D co-ordinate as: (10, 20)
#   Then, we can use, 
#                   pt = (10, 20) and 
#                   x, y = pt     (or x = pt[0], y = pt[1])
# This is not very transparent.
#
# So, Another way of doing this - using Class for 2D-Point. But then there can be many method that we need to override
# like - __repr__, __eq__, __lt__, __str__ and many more, even though in this case there is not much need of it.
#
# So, the much better approach to do it is - Named Tuple
#   - It is located in the `collections` standard library module
#   - namedtuple is a function which generated a new class, so it is also known as class factory.
#       - that new class inherits from tuple
#       - and that new class provides named properties to access elements of the tuple.
#       - but instance of that class is tuple.
#   - nametuple needs a few things to generate the class:
#       - the class name we want to use
#       - a seq. of field names we want to assign, in the order of the elements in the tuple
#         (field names can be any valid variable name except that they cannot start with an underscore).

from collections import namedtuple

Point2D = namedtuple('Point2D', ['x', 'y'])     # Here, Point2D is a assigned as a alias to class (namedtuple(...)) derived from tuple
pt = Point2D(10, 20)
print('\n---- namedtuple ----')
print(pt)

# We can provide name for our tuples with any sequence of strings (i.e., using lists or tuples or even a single string separated by spaces).
#   namedtuple('Point2D', 'x y')
#   namedtuple('Point2D', 'x, y')
# or, we can even use multi-line strings.

# We can also use keyword arguments
pt2 = Point2D(y=10, x=3)
print(pt2)



# Accessingg Data in a Named Tuples
#   - by index
#   - slice
#   - iterate
#   - using named properties

# Now, since namedtuples are generated classes inherited from tuple, so pt1 is a tuple and is therefore immutable.

# `rename` in namedtuple is used to rename the field name if it is invalid. It replaces the invalid field name with _field-no.
#   for ex: namedtuple('Point2D', ['x', '_y'], rename=True) - will give you a named tuple with the fields: x and _1. 



# Introspection
#   - We can easily find out the field names in a named tuple generated class using the class propery --> _fields.
print('\n---- Introspection ----')
print(Point2D._fields)
#   - We can actually see the code for the generated class, using the class property _source.
print(Point2D._source)



# Extracting Named Tuple Values to a Dictionary
#   - using instance method: _asdict()
print('\n---- Extracting namedtuple values as a dictionary ----')
print(pt._asdict())     # Will give an ordered dictionary



# Named Tuples - Modifying and Extending
#   - So how can we change one or more values inside the tuple --> Just like with strings, we have to create a new tuple, with the modified values.
#   - This can be done using the four accessing techniques.
Stock = namedtuple('Stock', ['symbol', 'year', 'month', 'day', 'open', 'high', 'low', 'close'])
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
print('\n---- Modifying and Extending Named Tuples ----')
print(djia)

#---- Way-1 for Modifying ----
#   - The simple approach --> djia = Stock(djia.symbol, djia.year, ..., 26_394) has a obvious drawback of writing such a horrible code

#---- Way-2 for Modifying ----
#   - Getting the required values that do not change using `Slicing`
current1 = djia[:7]
print(current1)
djia2 = Stock(*current1, 26_394)
print(djia2)

#---- Way-3 for Modifying ----
#   - Use of extended unpacking
*current2, _ = djia
print(current2)
print(current1 == current2)
# Making new namedtuple using the values that remain same (extracted before) and the new value(s)
djia3 = Stock(*current2, 26_394)    # we can also use current2 instead of current1
print(djia3)

# Note: When we use a slice we get a tuple back and when we unpack, we get a list back.

#---- Way-4 ----
#   - We can also use the _make class method - but we need to create an iterable that combines all the values first.
new_values = current1 + (26_394, )   # or we can use --> current2.append(26_394) if we have used slicing
djia3 = Stock._make(new_values)
print(djia3)

# But the above mentioned methods also has drawbacks:
#   - That is, if we wanted to change a value in the middle (say, `day`). So, we cannot use extending unpacking.
#     Although Slicing will still work in this case, where we want to change one middle value day.
#       pre = djia[:3]
#       post = djia[4:]
#       new_values = pre + (26,) + post
#       new_djia = Stock(*new_values)
#   - But the slicing will also have a drawback, say for the case when we want to search for more than one values in
#     the middle, the code will become little unreadable and pain to write extra bit of code!!!
#
# For this we have `_replace` instance method - it will copy the maned tuple into a new one, replacing any values from
# keyword arguments. The keyword arguments are simple the field names in the tuple and the new values. Also the keyword
# name must match an existing field name.
djia4 = djia._replace(day=26, high=26_459, close=26_394)
print(djia4)

# Extending a Named Tuple
#   - Something we want to create named tuple that extends another tuple, appending one or more fields.
# Suppose we want to create a new named tuple class, StockExt that adds a single field, previous_close. When dealig with
# classes, this is sometimes done by using subclassing but for namedtuple it is not so simple to use this concept.
# Ex:
#   Point2D = namedtuple('Point2D', 'x y')
#   new_fields = Point2D._fields + ('z',)
#   Point3D = namedtuple('Point3D'. new_fields)

new_fields = Stock._fields + ('previous_close',)
StockExt = namedtuple('StockExt', new_fields)
print(StockExt._fields)

# We can also easily use an existing Stock instance to create a new StockExt instance with the same common values, adding in
# our new previous_close value:
djia_ext = StockExt(*djia, 26_000)
print(djia_ext)     # or we can also use _make method



# Deafult Values and Default Docs for Named Tuple
#   - when we create a named tuple class, default dcstrings are created
print('\n---- Default Docs for Named Tuple ----')
print(Point2D.__doc__)
print(Point2D.x.__doc__)
print(Point2D.y.__doc__)
help(Point2D)

Point2D.__doc__ = 'Represents a 2D Cartesian coordinate.'
Point2D.x.__doc__ = 'x coordinate'
Point2D.y.__doc__ = 'y coordinate'
help(Point2D)

#   - The namedtuple function does not provide us a way to define default values for each field
# The two approaches are:
#   --> Using a prototype: Create an instance of the named tuple with default values - the prototype
#                          Create any additional instances of the named tuple using the prototype._replace method.
#                          But for this type of default you have to provide the default values for all the fields
#                          though they can be None. 
#   --> Using the __defaults__ property: It Directly set the defautls of the named tuple constructor (the __new__) method.
#                                        So, in this case we don't have to give default values for every field.
#
# Note: That we cannot have non-defaulted parameters after the first defaulted parameter.

#---- Using Prototype ----
Vector2D = namedtuple('Vector2D', 'x1 y1 x2 y2 origin_x origin_y')
vector_zero = Vector2D(0, 0, 0, 0 ,0, 0)    # Prototype
print('---- Default Values ----')
print('Prototype: ', vector_zero)
v1 = vector_zero._replace(x1=10, y1=10, x2=20, y2=20) 
print('v1: ', v1)

#---- Using __defaults__ methods ----
#   - The __defaults__ property is writable, so, we can set it to a tuple of our choice, just don't provide more defaults than parameters
#     (extras are ignored). We need to provide defaults to the constructor of our named tuple class.
Vector2D.__new__.__defaults__ = (0, 0)   # In this the default values start from the last due to above mentioned note.
v2 = Vector2D(10, 10, 20, 20)
print('v2: ', v2)
print(v1 == v2)

# The __default__ approach can also use with other normal functions and classes.

# __defaults__ method is much more cleaner way to use than the protype way.
 


# Named Tuples - Application - Returning Multiple Values
from random import randint, random
# randint --> gives the random integer between two end points while random gives random float between 0 and 1 (including 0).

#---- Using normal tuple ----
def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return red, green, blue, alpha

print('\n---- Named Tuple - Application - Returning Multiple Values ----')
color = random_color()      # First gets the packed return values - tuple
print(color)
red, green, blue, aplha = color     # Then unpacks it into respective varaibles

del random_color

#---- Using Named Tuple ----
Color = namedtuple('Color', 'red green blue alpha')
def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)

color = random_color()
print(color)
print(color.red, color.green, color.blue, color.alpha)      # Here, we can easily access the values in the tuple



# Named Tuple - Application - as a alternative to Dictionary
#---- Dict way ----
dict_data = dict(key1=100, key2=200, key3=300)
print(dict_data['key1'])

#---- Named Tuple way ----
#       data = namedtuple('Data', 'key1 key2 key3')
#
# But if we have an existing dictionary and want to convert it's keys to the namedtuple's fields, then:
Data = namedtuple('Data', dict_data.keys()) 
print(Data._fields)
d1 = Data(*dict_data.values())
print(d1)

# Note: From python 3.6/3.7+ it is guaranteed to have the order of dictionary to be preserved.
# So, the above way will work, in our case since the order will be preserved but it is not a very robust way of doing.
#
# But, as we know that we can also pass keyword arguments in the namedtuple class alias, so:
d2 = Data(**dict_data)
print(d2)
print(d1 == d2)
# The above way will ensure, that the right value will go to the right field.

# We also use the built-in `getattr` function with namedtuple intance to get the value
print(d2.key2)
print(getattr(d2, 'key2'))
print(getattr(d2, 'key10', None))   # which is similar to the dictionaries' `get` method

# So the namedtuple gets a little more advantage in this case as we have almost the same functionalty
# but with ease of calling method in comparison to dictionary.(i.e., calling field using `.` and the auto-completion in editor).

#---- Converting a list of dictonaries of named tuples ----
data_list = [
    {'key2': 1, 'key1': 2},
    {'key1': 3, 'key2': 3},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}]           # Here, in the above code we have a lot of duplicate text

keys = {key for d in data_list for key in d.keys()}     # Set Comprehension (by this way we elminate duplicate data/keys)
print(keys)
Struct = namedtuple('Struct', sorted(keys))     # By this, there is not guaranteed that the order is same
print(Struct._fields)

# Now, we have unequal lengths of dictionaries corresponding to the available keys
#   - So, we can use the default values.
Struct.__new__.__defaults__ = (None, ) * len(Struct._fields)
data = [Struct(**d) for d in data_list]
print(data)

# Making a general function to convert the list of dictionaries into the list of namedtuples
def dict_to_named_tuple(dict_list):
    keys = {key for d in dict_list for key in d.keys()}
    Struct = namedtuple('Struct', sorted(keys), rename=True)
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    return [Struct(**d) for d in dict_list]
named_tuple_list = dict_to_named_tuple(data_list)
print(named_tuple_list)
