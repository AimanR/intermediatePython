#!/usr/bin/env python3

# 5
# static methods and class methods

class dog:
    # class variables
    dogs = []
    xc = 5
    
    def __init__(self, name):
        self.name = name
        self.dogs.append(self)
        
    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)
        
    @staticmethod
    def bark(n):
        '''barks n times'''
        for _ in range(n):
            print('bark!!')
            
class Math:
    @staticmethod
    def add(x1, x2):
        return x1 + x2
 
# using the class variables 
print("***Using the class variables:\n")            
aiman = dog("aiman")
daiman = dog("daiman")

print(dog.dogs)
print(dog.xc)
print(aiman.xc)
print(daiman.dogs)


# changing class variables through class objects
print("\n\n\n***Changing class variables through class objects:\n")
aiman.dogs.append(2)
print(aiman.dogs)
print(dog.dogs)

# using the classmethod
print("\n\n\n***using the classmethod:\n")
print(aiman.num_dogs())
print(dog.num_dogs())

# using the staticmethod
print("\n\n\n***using the staticmethod:\n")
dog.bark(2)
print(Math.add(2,33))