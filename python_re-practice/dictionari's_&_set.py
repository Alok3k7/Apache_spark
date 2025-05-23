print("**Dictionaries**")

"""Dictionaries are ordered collection of data items.They store multiple items in a single variable.Dictonary items 
are key-value pairs that are separated by commas and enclosed with in curly brackets {}
"""
info = {'name': 'alok', 'age': 19, 'eligible': True}
print(info)

# Accessing Dictionary items:-
# 1. Accessing single values:- Values in a dictionary can be accessed using keys.we can
# access dictionary values by mentioning keys either in square brackets or by using get method .

me = {'name': 'lucky', 'age': 20, 'eligible': True}
print(me['name'])
print(me.get('eligible'))

# 2.Accessing multiple values:- We can print all the values in the dictionary using value() method .

information = {'name': 'aditya', 'age': 18, 'eligible': True}
print(information.values())

# 3.Accessing keys:- we can print all the keys in the dictionary using key () method.

id_1 = {'name': 'Pratham', 'age': 10, 'eligible': False}
print(id_1.keys())

# 4.Accessing key-value pairs :- we can print all the key-value pairs in the dictionary using items() methods.

inform = {'name': 's', 'age': 20, 'eligible': True}
a = info.items()
print(a)

print("\n\n\n\n**Sets**")
"""Sets are unordered collection of data items .they store multiple items in a single variable .set item are 
separated by commas and enclosed with curly bracket {}.Set are unchangeable, meaning you cannot change items of the 
set once created sets do not contain duplicate items.
"""

details = {"Tiwari", 20, False, 5.9, 20}
print(details)

# here we see that the items of set occur in random order and hence they cannot be accessed using index number .
# Also, sets do not allow  duplicate values.

# that the way to access the empty set.
sets = set()
print(type(sets))

# access set items :- you can access items of set using a for loop

infor = {'carla', 19, False, 5.9}
for item in infor:
    print(item)
