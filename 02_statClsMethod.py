#!/usr/bin/env python3

# Static and class methods #2

class person:
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def getPopulation(cls):
        return cls.population
    
    @staticmethod
    def isAdult(age):
        return age >= 18
    
    def display(self):
        print(self.name, ' is ', self.age, ' years old.')
        
newPerson = person('Aiman',25)

print(newPerson.population)
print(person.population)

print()

# using class method
print(newPerson.getPopulation())
print(person.getPopulation())

print()

# using static method
print(newPerson.isAdult(25))
print(person.isAdult(18))

# class method can access class variables
# static method cannot access calss variables