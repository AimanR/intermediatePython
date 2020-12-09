#!/usr/bin/env python3

# 1
# oop intro

help(int)
help(str) # prints some detailed info related to str or int

# int is a class

x = 5
number = 5

# 5 is an object of class 'int'
# 'x' and 'number' are both instances of the object 5
# 'x' and 'number' are both instances of the class 'int'


'''
# from stack overflow
# difference between objects and instances
# https://stackoverflow.com/questions/3323330/difference-between-object-and-instance#:~:text=Object%20is%20a%20copy%20of,instances%20between%20objects%20are%20not.

The truth is that object oriented programming often creates confusion by creating a disconnect between the philosophical side of development and the actual mechanical workings of the computer. I'll try to contrast the two for you:

The basic concept of OOP is this: Class >> Object >> Instance.

The class = the blue print. The Object is an actual thing that is built based on the 'blue print' (like the house). An instance is a virtual copy (but not a real copy) of the object.

The more technical explanation of an 'instance' is that it is a 'memory reference' or a reference variable. This means that an 'instance' is a variable in memory that only has a memory address of an object in it. The object it addresses is the same object the instance is said to be 'an instance of'. If you have many instances of an object, you really just have many variables in difference places in your memory that all have the same exact memory address in it - which are all the address of the same exact object. You can't ever 'change' an instance, although it looks like you can in your code. What you really do when you 'change' an instance is you change the original object directly. Electronically, the processor goes through one extra place in memory (the reference variable/instance) before it changes the data of the original object.

The process is: processor >> memory location of instance >> memory location of original object.

Note that it doesn't matter which instance you use - the end result will always be the same. ALL the instances will continue to maintain the same exact information in their memory locations - the object's memory address - and only the object will change.

The relationship between class and object is a bit more confusing, although philosophically its the easiest to understand (blue print >> house). If the object is actual data that is held somewhere in memory, what is 'class'? It turns out that mechanically the object is an exact copy of the class. So the class is just another variable somewhere else in memory that holds the same exact information that the object does. Note the difference between the relationships:

Object is a copy of the class. Instance is a variable that holds the memory address of the object.

You can also have multiple objects of the same class and then multiple instances of each of those objects. In these cases, each object's set of instances are equivalent in value, but the instances between objects are not. For example:

Let Class A From Class A let Object1, Object2, and Object3.

//Object1 has the same exact value as object2 and object3, but are in different places in memory.

from Object1>> let obj1_Instance1, obj1_Instace2 , obj1_Instance3

//all of these instances are also equivalent in value and in different places in memory. Their values = Object1.MemoryAddress.

etc.

Things get messier when you start introducing types. Here's an example using types from c#:

//assume class Person exists Person john = new Person();

Actually, this code is easier to analyze if you break it down into two parts:

Person john;
john = new Person();

In technical speak, the first line 'declares a variable of type Person. But what does that mean?? The general explanation is that I now have an empty variable that can only hold a Person object. But wait a minute - its an empty variable! There is nothing in that variables memory location. It turns out that 'types' are mechanically meaningless. Types were originally invented as a way to manage data and nothing else. Even when you declare primitive types such as int, str, chr (w/o initializing it), nothing happens within the computer. This weird syntactical aspect of programming is part of where people get the idea that classes are the blueprint of objects. OOP's have gotten even more confusing with types with delegate types, event handlers, etc. I would try not focus on them too much and just remember that they are all a misnomer. Nothing changes with the variable until its either becomes an object or is set to a memory address of an object.

The second line is also a bit confusing because it does two things at once:

The right side "new Person()" is evaluated first. It creates a new copy of the Person class - that is, it creates a new object.

The left side "john =", is then evaluated after that. It turns john into a reference variable giving it the memory address of the object that was just created on the right side of the same line.

If you want to become a good developer, its important to understand that no computer environment ever works based on philosophic ideals. Computers aren't even that logical - they're really just a big collection of wires that are glued together using basic boolean circuits (mostly NAND and OR).

'''