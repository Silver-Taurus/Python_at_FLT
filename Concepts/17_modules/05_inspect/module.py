#! /usr/bin/env python3

''' A Python Script to be inspected '''

class Planet:
    
    shape = 'round'

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system
    
    def orbit(self):
        return '{} is orbiting in the {}'.format(self.name, self.system)
    
    @classmethod
    def commons(cls):
        return 'All Planets are {} becuase of gravity'.format(cls.shape)
    
    @staticmethod
    def spin(speed='2000 miles per hour'):
        return 'The planet spins at {}'.format(speed)
    
    