#!/usr/bin/env python3

# 3
# overloading methods

from math import sqrt

print(7-3)
print((7).__add__(3))
print((7).__sub__(3))

class point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)
        
    def move(self, x, y):
        self.x += x
        self.y += y
        
    def length(self):
        return sqrt(self.x**2+self.y**2)
    
    # arithmetic ooperations    
    def __add__(self,p):
        return point(self.x+p.x , self.y+p.y)
    
    def __sub__(self,p):
        return point(self.x-p.x , self.y-p.y)
    
    def __mul__(self, p):
        return self.x*p.x + self.y*p.y
    
    # comparisons
    def __gt__(self, p):
        return self.length > p.length
    
    def __ge__(self, p):
        return self.length() >= p.length()        
        
    def __lt__(self, p):
        return self.length() < p.length()        
        
    def __le__(self, p):
        return self.length() <= p.length()        
        
    def __eq__(self, p):
        return self.length() == p.length()
    
    # printing style
    def __str__(self):
        return '('+ str(self.x) + ',' + str(self.y) + ')'       
    
    
p1 = point()
p2 = point(2,3)
p3 = point(-3,7)

print(p1, p1.x, p1.y, p1.coords)
print(p2, p2.x, p2.y, p2.coords)
print(p3)
print(p2+p3)
print(p2-p3)
print(p2+p3)
print(p2<p3)
print(p2.length())
print(p2==p3)