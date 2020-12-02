#!/usr/bin/env python3

# map function #3

li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

students = ['aiman', 'onim', 'hasin']

def value(name):
    Sum = 0
    for c in name:
        Sum += ord(c)
    return Sum

newli = list(map(func,li))
print(newli)

studentVal = list(map(value, students))
print(studentVal)

# map function takes to things as parameters, a function and a list