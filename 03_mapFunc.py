#!/usr/bin/env python3

# map function #3

li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

students = ['aiman', 'onim', 'hasin']

def value(name):
    '''
    Returns the sum odf ascii value of the characters in the name.
    '''
    Sum = 0
    for c in name:
        Sum += ord(c)
    return Sum

newli = list(map(func,li))
print(newli)
print("Can also be done using list comprehension :")
newli2 = [func(x) for x in  li]
print(newli2)
print()

studentVal = list(map(value, students))
print(studentVal)
print("Can also be done using list comprehension :")
studentVal2 = [value(x) for x in  students]
print(studentVal2)
print()


# map function takes to things as parameters, a function and a list