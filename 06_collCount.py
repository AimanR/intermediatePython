#!/usr/bin/env python3

# collections/counter() # 6

import collections
from collections import Counter

c = Counter('gallad')

c = Counter(['a',12, -2.33])

c = Counter({'aiman':53, 'onim':23})

c = Counter(cats=2, dogs=3)

# 1
#

print("***\nc : \n")
print(c)
print(c['cats'])
print(c['mice']); print()

print( list(c.elements()) )
print(c.most_common())
print(c.most_common(0))
print(c.most_common(1))
print(c.most_common(2))
print(c.most_common(100)) # Not sure why it prints what it prints
print()

# 2
#

a = Counter(a=2, b=4, c=0, d=-2)
d = ['a','b','b','c']

print("***\na,d:\n")

print(a)
a.subtract(d)  
print(a)
a.update(d)   
print(a)
print()


# 3
#

print("***\na,d,e:\n")
e = Counter(d)
print(a+e)
print(a-e)
print(a&e)
print(a|e)


a.clear()
print(a)

