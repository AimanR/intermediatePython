#!/usr/bin/env python3

#5 #lambda function

# lambda function with single parameter
func = lambda x:x+5 # lambda version

# lamda function multiple parameters
func2 = lambda x,y : x+y # can return a single value

# lamda function optional parameters
func3 = lambda x,y=10 : x+y

print(func(3))
print(func2(10,12))
print(func3(13,34))
print(func3(13))