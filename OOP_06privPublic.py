#!/usr/bin/env python3

# 6
# private and public classes 

'''
there are no private class or method in python
they are sumply indicated to be used as private by naminig them with a beginning underscore
e.g. "class _private:" or "def _privateMethod():"
'''

class _private: # private class
    def __init__(self, name):
        self.name = namae
        
class notPrivate: # nat a private class
    def __init__(self, name):
        self.name = name
        self.priv = _private(name)
        
    def _display(self): # private method
        print('hello')
        
    def display(self): # not private method
        print('hi')
    