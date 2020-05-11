''' Comments'''
print("Hello World!")
'''Types and Variables'''
'''Strings'''
#Strings are sets of characters. 
#In Python strings are in double or single quotes 
#like "Hello World!" or 'after edit, save!'
a = 'Hi There!'
print(a)
'''Integers'''
#whole numbers such as -2, -1, 0, 1, 2, 3 are Integers
a = 10
print("Integer", a)
b = '10'
print('Not Integer', b)
''' Variables '''
#In python a variable is a type of object that 
#can be addressed by name to access the assigned contents.
#Name a variable staring with a letter or underscore "_"
''' data types in variables '''
item_price = 10.25 #item_price initialized as a numeric value (no quotes)
student_name ="Dias, Joana" #student_name initialized as a string
license_plate = "123A" #license_plate initialized as a string
#Python variables can change the type of data a variable holds
x = 22
x = "I am a string"
'''Using the Python type() function'''
#type() returns the data type of Python objects
add_two = 34 + 16
first_name = "Shuvo"
greeting = "Happy Birthday " + first_name
print(add_two)
print(greeting)
#SyntaxError - breaks code formatting rules of python
#NameError - object is not defined (can't be found)
#Indentation Error
#input() returns a string (type = str) regardless of entry
''' Math Operators'''
#x + y	Sum of x and y
#x - y +	Difference of x and y
#-x	Changed sign of x
#+x	Identity of x
#x * y	Product of x and y
#x ** y power
#x / y	Quotient of x and y
#x // y	Quotient from floor division of x and y
#x % y	Remainder of x / y
#x ** y	x to the y power
a = 5
b = 2 
c = a%b
print(c)