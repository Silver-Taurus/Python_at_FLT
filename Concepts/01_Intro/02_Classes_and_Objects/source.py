#! /usr/bin/env python3

''' Python script for introduction to classes and objects '''

#---- Use of basic built-in functions and operator overloading ---- 
class Rectangle:
    def __init__(self, width, height):
        # here, self is customary used variable name and not a fixed usable keyword (hence we can write anything in place of self)
        self.width = width
        self.height = height       

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return 'Rectangle: width={}, height={}'.format(self.width, self.height)
    
    # Overloading built-in function repr()
    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.width, self.height)

    # Overloading the == operator
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False

    # Overloading the < operator
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            # we didn't raise NotImplemented, we returned it
            return NotImplemented

r1 = Rectangle(10, 20)
print('\n\n---- Classes and Objects ----')
print(r1.area())
print(r1.perimeter())
print(str(r1))
print(repr(r1))     # This is the case of - when we just write r1 in the interactive console and run it - and it gives the - repr(object).

r2 = Rectangle(10 ,20)
print(r1 == r2)
print(r1 == 100)
print(r1 < r2)
print(r1 > r2)      # will give the correct output even though __gt__ method is not defined, as in this case python first sees for __gt__ method when not found will
                    # find its negation that is __lt__ method which is implemented and hence will use the ouput from it and negate it and hance provide the correct output.
                    # But this will not gonna happen with >== or <== as their complement is not defined.
r1.width = 100
print(repr(r1))

del Rectangle



#---- Using getters and setters ----
class Rectangle:
    def __init__(self, width, height):
        self._width = width         # using one underscore is just customary to tell the other user that these are private and not use them directly
        self._height = height       # and in-place use the getters and setters method.

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive!!!')
        else:
            self._width = width
    
    def get_height(self):
        return self._height

    def set_heith(self, height):
        self._height = height
    def get_width(self):
        return self._width

    def set_width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive!!!')
        else:
            self._width = width
    
    def get_height(self):
        return self._height

    def set_heith(self, height):
        self._height = height

    def __str__(self):
        return 'Rectangle: width={}, height={}'.format(self._width, self._height)
    
    def __repr__(self):
        return 'Rectangle({}, {})'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self._width, self._height) == (other._width, other._height)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


# Now for controlling the access for our encapsulated data, we generally uses getters and setters. Suppose for this case we don't need negative value for width as it is not possible.

# As we have the getters and setters, so the people should be accessing the width and height using get_width and set_width methods and not directly by obj._width or obj_height.
# If here, we will try to get obj.width or obj.height it will give us `Attribute Error`, but if we will try to set value obj.width = -100 or obj.height= -100 then it will create a new attribute
# of these names. This process is called Monkey Patching.

# But if we have chagned the attributes to customary private notations, and forces to use getters ans setters then, if the people have written the code as obj.width = 100 or print(obj.width), then
# the code will break at those points and they have to change their code.

r = Rectangle(10, 20)
print(repr(r))
#   print(r.width) --> will give the `Attribute Error`
r.width = 100      # This is Monkey Patching and not setting of width attribute value as the attribute is _width whose value will remain same.
print(repr(r))
r.set_width = 100
print(repr(r))

del Rectangle



#---- Solution for breaking of code problem ----
#   - Don't force the getters and setters until they are providing some extra functionality like in this case of width and height we have extra functionalty that is, width and height cannot
#     be negative.
#   - Also for those attributes, for whom we need to use setters and getters we make it transparent without letting the user know that a setter is being used, as the user will be directly accessing
#     using name but in background the setter or getter will be runnig.
class Rectangle:
    def __init__(self, width, height):
        self._width = width         
        self._height = height 

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    # property is use to make the property to be passed through a getter
    @property
    def width(self):
        ''' This is a getter method which is marked as a property using property decorator'''
        return self._width

    @property
    def height(self):
        ''' This is getter method which is marked as property using property decorator '''
        return self._height

    # Now since we have the width and height as a property, we can use the proprty.setter to mark that the property
    # is now being set via setter
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive!!!')
        else:
            self._width = width

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive!!!')
        else:
            self._height= height

    def __str__(self):
        return 'Rectangle: width={}, height={}'.format(self._width, self._height)
    
    def __repr__(self):
        return 'Rectangle({}, {})'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self._width, self._height) == (other._width, other._height)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

# Since we have made the getters and setters as the property we can directly use them using object without calling them using paranthesis.
# So, if the name of the getters and setters method are same as that of property without _, then the problem of breaking of code will resolve as
# we can get or set the width and height using the getters and setters by using just the name of the property.

r = Rectangle(10, 20)
print(r.width)
r.width = 100
print(repr(r))

# Now the above code works fine for most of the things, but there is still a problem that initialisation method can take negative values of width or height.
# So what can i do is:
#   - Use exception handling
# or
#   - Use setters in __init__

del Rectangle



#---- Using Setters for initialisation ----
class Rectangle:
    def __init__(self, width, height):
        self.width = width         # setter is called
        self.height = height       # setter is called

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

    @property
    def width(self):
        ''' This is a getter method which is marked as a property using property decorator'''
        return self._width

    @property
    def height(self):
        ''' This is getter method which is marked as property using property decorator '''
        return self._height

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive!!!')
        else:
            self._width = width

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive!!!')
        else:
            self._height = height

    def __str__(self):
        return 'Rectangle: width={}, height={}'.format(self._width, self._height)
    
    def __repr__(self):
        return 'Rectangle({}, {})'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self._width, self._height) == (other._width, other._height)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

#   r =  Rectangle(10, -20)  --> will give you ValueError
r = Rectangle(10, 20)
print(r._width)
print(r.width)
print(r.area())