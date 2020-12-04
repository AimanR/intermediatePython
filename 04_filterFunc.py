#!/usr/bin/env python3

# Filter function # 4

def add7(x):
    return x+7

def isOdd(x):
    return x%2 == 1

a = [1,2,3,4,5,6,7,8,9,10]

b = list( filter( isOdd,a ) )
print(b)

c = list( map( add7,b ) )
print(c)

# the entire work done above can be done using list comprehension
d = [add7(x) for x in a if isOdd(x)]
print(d)