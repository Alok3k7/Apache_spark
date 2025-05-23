print("** String Formatting **")
"""
string Formatting ,also known as string interpolation is the process of inserting a custom string or variable 
predefined text. and the meaning of Interpolation is the insertion  of something of a different nature into 
something else
"""

"""There is four type of string formatting that i know 
1.formatting with %
2.formatting with str.format() function
3.formatting with  f-string 
4.formatting with string templates class
"""

# formatting with % operator :- the oldest  technique used to insert an object in to the string
lan = "python"
use = "DE"
print("i work with %s language" % lan)
print("i am alok and learn %s for %s." % (lan, use))

print("The value of e is %5.2f\n" % 13435.4465654464)  # for floating point we define the 5.2f

# formatting with format() method
print("i just start the python 0 to {} ready .".format("DE jop"))

# also we define index in this method and we can give any index number present index
print("let's start to fly for {0} and {1}\n".format("dream", "jobs"))

# formatting with f-string method
name = "alok"
lan = "Python"
job = "DE"

print(f"My name is {name}.I can learn very strong lang {lan}. For my future work {job}")

n = 10
m = 99
print(f"The addition of {n} + {m} is {n + m}.")

num = 50
print(f"Is that number is even ? {True if num % 2 == 0 else False}")

# template string

from string import Template

a1 = "python"
a2 = "for DE"
n = Template("Hello,welcome for learning $p $d future")
print(n.substitute(p=a1, d=a2))

stu_name = "alok"
s = Template("Hey my name is $a  ! How are you ?")
print(s.substitute(a=stu_name))

print("\n ** List_Method **")

# list.sort():- This method sort the list in ascending order. The original list is update

colors = ["violet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [1, 7, 9, 6, 5, 6, 7, 9, 6, 4, 3, 6]
num.sort()
print(num)

# reverse = True as parameter in the sort method

colors = ["violet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

num = [1, 7, 9, 6, 5, 6, 7, 9, 6, 4, 3, 6]
num.sort(reverse=True)
print(num)

# reverse() :- this reverse() method the order of the list
colors = ["white", "yellow", "black", "magenta"]
colors.reverse()
print(colors)

# index() :- this method returns the index of first occurrence of the list item.

any_name = ["Alok", "Aditya", "Lucky", "S", "Avinash"]
print(any_name.index("S"))

random_num = [1, 3, 5, 6, 7, 8, 9, 2, 4]
print(random_num.index(9))

# count():- Return the count of the number of item with given value .

some_name = ["raju", "vanguard", "rancho", "vanguard", "irfan", "vanguard"]
print(some_name.count("vanguard"))

spec_num = [1, 3, 5, 6, 7, 8, 9, 4, 4, 4, 4, 6, 2, 4]
print(spec_num.count(4))

# copy():- return copy of the list. this csn be done to perform operation on the list without modifying the original
# list

need = ["watch", "phone", "bike", "super_bike", "car", "super_car"]
wish = need.copy()
print(need)
print(wish)

# append():- this method appends items to the end of the existing list

dream_place = ["USA", "Russia", "France", "Australia"]
dream_place.append("germany")
print(dream_place)

# insert():-this method inserts an item at the given index . user has to specify index andthe item to be inserted
# with in the insert()method

state = ["UP", "Maharashtra", "kerala", "Delhi"]
state.insert(1, "bihar")
print(state)

# extend():- this method adds  an entire list or any other collection data type (set,tuple,dictonary)to the existing
office = ["laptop", "chair", "table", "ac", "fan", "headphone"]
more_thing = ["sofa", "parking", "bike"]
office.extend(more_thing)
print(office)

# concatenating two list :-we can simply concatenate two list
office = ["laptop", "chair", "table", "ac", "fan", "headphone"]
more_thing = ["sofa", "parking", "bike"]
print(more_thing+office)