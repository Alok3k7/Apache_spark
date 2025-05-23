print(""" Operator_in_python """)
"""
1.Arithmetic Operator
2.Comparison Operator
3.Logical Operator
"""
x = 3  # storing the value in the variable x
y = 3  # storing the value in the variable y

print("\n**Arithmetic Operator**")
# "+" for addition
a = x + y
print("Addition of two number", a)
# "-" for subtraction
s = x - y
print("Subtract of two number", s)
# "*" for multiplication
m = x * y
print("Multiple of two number", m)
# "/" for division
d = x / y
print("Division of two number", d)
# "%" for reminder/modulus
r = x % y
print("Modulus/reminder of two number", r)
# "**" for Exponentiation
e = x ** y
print("Exponentiation of two number", e)
# "//" for Floor_Division
f = x // y
print("Floor_Division of two number", f)

print("\n**Python Comparison Operators**")
# "==" Equal
print(x == y)
# "!=" Not Equal
print(x != y)
# ">" Greater Than
print(x > y)
# "<" Less Than
print(x < y)
# ">=" Greater Than Equal to
print(x >= y)
# "<=" Less Than Equal to
print(x <= y)

print("\n**Python logical Operators**")
# Logical Operators are used to combine conditional statement:-

# "And" return ture if both statement are ture
print('x < 5 and x < 10 it return value : ', x < 5 and x < 10)

# "or" return ture if one of statement is true
print('x < 3 or x < 4 it return value :', x < 3 or x < 4)

# "not" reverse the result ,returns false if the result is true
print("not( x < 5 and x < 10 ) it return value:", not (x < 5 and x < 10))

print("\n")
print("\n")

print("**String Method**")

# Python provides a sets of built-in methods that we can use to alter and modify the string

# upper():- The upper Method converts a string to upper case

str1 = "hello team I am ready to join ."
print(str1.upper())

# lower():- The lower() method converts a string to lower case.

str2 = "HELLO TEAM I NEED HELP ."
print(str2.lower())

# strip():- The strip() method removes any white spaces before and after the string

str3 = "      I want special job to run in dag.         "
print(str3.strip())

# rstrip():- The rstrip() method remove any trailing characters
str4 = "Hey all are you from programmer !!"
print(str4.rstrip("!"))

# replace():- The replace() method replaces all occurrences of a string with another string.
str5 = "I am here to the hard and smart work "
print("before replace:-", str5)
print("after replace :-", str5.replace("smart", "fast"))

# split():- The split() method split the given string at specified instance and returns the separated string  as lists
# items .

str6 = "i am good guy and i am bad guy"
print(str6.split("and"))

# capitalize():- the capitalize() method turns only the first  character of the string to uppercase and the rest
# other charters of the string are turned to lower case the string has no effected if the first character is already
# uppercase

str7 = "hello team today i am on leave ."
print(str7.capitalize())

str8 = "hello why I am getting shocked ."
print(str8.capitalize())

# center():- The center() method aligns the string to the center as per the parameters given by the user .
str9 = "I am working for Tricera and I am happy to Work."
print(str9.center(100, "."))
# we can also provide padding character .It will fill the rest with the fill character provided by the user

# count() :- the count() method returns the number of times te given value  has occurred within the given string
str10 = "Is that earth is round and rotating round and round "
print(str10.count("a"))