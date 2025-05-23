print("**Class_and_Object**")
"""
A class is blue print or a template for creating object ,providing initial values for state( member variables or 
attributes, and implementations of behavior (member function or method).The user-defined objects are created using 
the class keyword.
"""


# creating a class :-let us now create a class using the class keyword.

class Details:
    name = "Alok"
    age = 20
    gender = "M"


# creating an object :- Object is the instance of the class used to access the properties of the class. Now let's
# create an object of the class.

obj1 = Details()
obj1.name = "lucky"  # Here we change object
obj1.age = 23

print(obj1.name)
print(obj1.age)
print(obj1.gender)

print(type(obj1.name))


# Self parameter :- the self parameter is a reference to the current instance of the class . It must be provided as the
# extra parameter inside the method definition

class Info:
    name = "lucky"
    age = 19
    gender = "M"

    def desc(self):
        print("My name is", self.name, "and I am", self.age, "years old.")


obj2 = Info()
obj2.desc()


# Constructors :-A constructors is special method in a class used create and initialize an object of a class.
# There are different type of constructors.Constructors are invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of class .
# The main purpose of a constructor is to initialize or assign values to the data members of that class.
# It cannot return any value  other than none

# syntax of python constructor :- def__init__(self): Initialization.
# init is one of the reserved function in python.In object-oriented programming , it is known as a constructor .

# Type of Constructors in python
# 1. Parameterized constructor
# when the constructor  accepts arguments  a long with self ,it is known as parameterized constructor
# These arguments can be used inside the class to assign the values to the data members.


class Detailed:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group


obj3 = Detailed("Crab", "Crustaceans")
print(obj3.animal, "belong to the", obj3.group, "group.")


# 2.Default constructor. when the constructors don't accept any arguments from the object and has only one argument
# ,self ,in the constructor,it is known as a Default constructor
class Detail:
    def __init__(self):
        print("Animal Crab belong to Crustaceans group.")


obj4 = Detail()
