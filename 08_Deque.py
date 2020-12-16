#!/usr/bin/env python3

import collections
from collections import deque

d = deque("Aiman"); 
print(d)
print('\n\n')

# append

print('***append***\n')
d.append('4')
d.appendleft(5)
print(d)
print('\n')


# pop

print('***pop***\n')
d.pop();
print(d)
d.popleft()
print(d)
print('\n')


# extend

print('***extend***\n')
d.extend('xxx')
print(d)
d.extend(['h','e','l','l','o'])
print(d)
d.extendleft('DDD')
print(d)
print('\n')


# rotate

print('***rotate***\n')
e = deque("abcde")
e.rotate(-1)
print(e)
e.rotate(1)
print(e)
e.rotate(7)
print(e)
e.rotate(-7)
print(e)
print('\n')


# maxlen

print('***maxlen***\n')
f = deque('kjdsd',maxlen=4)
print(f)
f.extend('123')
print(f)
print('\n')


# clear

print('***clear***\n')
d.clear()
print(d)