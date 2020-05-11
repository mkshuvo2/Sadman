## Boolean Data Type
a = True
# 0 == False; anything else True
print(type(a))

# NoneType

#Type Checking 
#type() or isinstance(in, type) 
#len()


'''Operators and Branching'''
# https://www.w3schools.com/python/python_operators.asp

''' Operator Precedence'''
# https://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_precedence.html

''' Expression'''
# <object> <operator> <object>

'''Keywords'''

'''Slicing with String'''
#negative index

#Sequence Typs
''' Tuples '''
#A "tuple" is an ordered sequence of elements which can 
#include any different kind of element within them.
#Now, when I say an ordered sequence,
#I don't mean that the elements in the sequence
#are ordered, meaning smallest to largest.
#I mean that the sequence itself has an order so that I
#can get to different parts of the sequence
#by simply indexing.
#Tuples are immutable


tup = (1, 'One', 'Ten', 10) 
#Declaring Empty Tuple
tup_empty = ()
# Adding an element to tuple 
# a comma is added to convert to tuple type
tup_empty = tup_empty + (1,)

for i in tup:
    print(i, 'is of type', type(i))
#Indexing 
print(tup[0])
#Immutable
#tup[0] = 3
# Concatenation
tup = tup + (7 ,'Seven')
print(tup)
'''Slicing'''
tup[1:2]
#Swapping Variables
x = 10
y = 20
(x,y) = (y,x)
# Exercise
x = (1, 2, (3, 'John', 4), 'Hi')
'''Write a procedure called oddTuples, which takes a tuple as input,
and returns a new tuple as output, where every other element of 
the input tuple is copied, starting with the first one. So if test
is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating 
oddTuples on this input would return the tuple ('I', 'a', 'tuple'). '''

'''Range'''
start = 0
stop = 10
step = 3
r = range(start,stop,step)
for i in r:
    print(i)