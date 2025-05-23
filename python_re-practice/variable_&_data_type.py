# what is python ?
# python is a dynamically typed high-level object-oriented programming language.
# python was developed by guido van rossum in 1989 and was released in 1991 .
# python name python was taken from the popular BBC comedy show of that time "monty python's flying Circus".

# variables and data type

# what is variable ?
# Variable is like a container that holds data.Very similar to how our containers in kitchen hold
# sugar and salt etc. creating a variable is like creating a placeholder in memory an assigning  it some value .In
# python, it's as easy as writing :-

a = 1  # It's storing integer in the variable a .
b = True  # It's storing boolean in the variable b .
c = "alok"  # It's storing string in the variable c.
d = None  # It's storing nothing in the variable d .

print(type(a), a)
print(type(b), b)
print(type(c), c)
print(type(d), d)

# these are four variables of different data type .

# what ia data type ? Data type specifies the type of variable holds .
# This is required in programming to do various operations without causing an error.
# In python ,we can print the type of any operation  using type function

a = 1
print(type(a), a)
b = "1"
print(type(b), b)

# by default , python provide the following built in data type:-
# 1. Numeric data :- int ,float,complex
integer = 3, -8, 0
print("Integer is print", integer)
floating = 7.82, -9.8, 0.001
print("Float is print", floating)
complex_ = complex(6, 2)
print("Complex is print", complex_)

# 2.string text data
string = "Hello world !", "Python Programming "
print("string is print", string)

# 3.Boolean data
# [Boolean data is consists of value True or False]

# 4.sequenced data :-
# list,tuple.
# list :- A list is an ordered collection of data with elements separated by a comma
# and enclosed within square brackets. Lists are mutable and can be modified after creation.
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print("list of data is print", list1)

# Tuple :- A tuple is an ordered collection of data with Element separated by a comma and enclosed with
# parentheses.Tuples are immutable and can not be modified after creation .
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print("Tuple of data is print", tuple1)

"""
5.mapped data:- dict        
dict:- A dictionary is an unordered collection of data containing a key: value pair.
The key:value pairs are enclosed with  curly brackets .
"""
dict1 = {"name": "alok", "age": 21, "CanVote": True}
print("Dictionary of data is print", dict1)

# In the python every thing is an object.
