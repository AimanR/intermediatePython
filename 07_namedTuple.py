#!/usr/bin/env python3

# namedtuple # 7

import collections
from collections import namedtuple

Point = namedtuple('foint', 'x y z')
newP = Point(3,4,5)
print(type(newP))
print(type(Point))
print(newP); print()


Point1 = namedtuple('dot', ['x','b', 'a'])
P1 = Point1(1,2,3)
print(P1)

Point2 = namedtuple('Person',{'Name':0, 'Roll':2, 'asd':56})
P2 = Point2(3,4,5)
print(P2)
print(P2.Name,P2.asd,P2.Roll)
print(P2[1])
print(P2._asdict())
print(type(P2._asdict()))
print(P2._fields)

P3 = P2._replace(asd= 23)
print(P3)