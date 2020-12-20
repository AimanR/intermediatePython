#!/usr/bin/env python3

# 2 
# creating classes

class dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("A dog is made.")
        
    
    def speak(self):
        print('hi i m', self.name,'and i am', self.age, 'years old')
    
    def add_weight(self, weight):
        self.weight = weight
        
aiman = dog('aiman',22) 
daiman = dog('daiman',33)

aiman.speak()
daiman.speak()

print(aiman.age)

aiman.add_weight(67)
print(aiman.weight)