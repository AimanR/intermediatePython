#!/usr/bin/env python3

import collections
from collections import deque

d = deque("Aiman"); print(d)

d.append('4')
d.appendleft(5)
print(d)

d.pop(); d.pop() 
print(d)

d.popleft()
print(d)

d.extend('xxx')
print(d)

d.extend(['h','e','l','l','o'])
print(d)

d.extendleft('DDD')
print(d)

e = deque("abcde")
e.rotate(-1)
print(e)

e.rotate(1)
print(e)

e.rotate(7)
print(e)
e.rotate(-7)
print(e)

f = deque('kjdsd',maxlen=4)
print(f)
f.extend('123')
print(f)

d.clear()
print(d)