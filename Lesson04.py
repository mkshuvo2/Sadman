# Slicing of List
#a[start:stop:step] # start through not past stop, by step
#a[start:stop]  # items start through stop-1
#a[start:]      # items start through the rest of the array
#a[:stop]       # items from the beginning through stop-1
#a[:]           # a copy of the whole array

#a[::-1]    # all items in the array, reversed
#a[1::-1]   # the first two items, reversed
#a[:-3:-1]  # the last two items, reversed
#a[-3::-1]  # everything except the last two items, reversed

a = [1, 3, 5, 7, 9, 11]


#Dictionaries
#A dictionary is a collection which is unordered, 
#changeable and indexed. In Python dictionaries 
#are written with curly brackets, and they have keys and values.
age = {'Shuvo':'25', "Sadman":'13'}
# Adding Values
age['Ma'] = '50'
#Getting Keys
#Keys must be unique and immutable
