print("**FUNCTION-IN-DETAILS**")
"""
A function is a block of code that performs a specific task whenever it is called .In trigger programs,
where we have large amount of code ,it is advisable to create or user existing function that make the program flow
organized and neat .
"""

"""
There is two type of function :-
1.Built-in function.
2.User defined function.
"""

"""
Built-in function :- these functions are defined and pre-coded in python. Some examples of built-in functions are 
following :- min(),max(),len(),sum(),type(),range(),dict(),list(),tuple(),set(),print(),etc. user-define 
functions:-we can create functions to perform specific tasks as per our needs .such functions are called 
user-defined function
"""


# syntax:-
def function_name():
    pass


# Create a function using the def keyword, followed by a function name , followed  by  a parenthesis (()) and a colon(:)
# Any parameters and arguments should be placed  within the parenthesis.
# rule to naming function are similar to that aof naming variables.
# Any statements and other code within the function should be indented.

# c

def names(fname, lname):
    print("hello", fname, lname)


names("alok", "tiwari")
names("lucky", "tiwari")


def add(a, b):
    print(a + b)


def calculategmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)


def isgreatethan(a, b):
    if a > b:
        print("a is greater tan b")
    else:
        print("not a greater")


a = 50
b = 30
isgreatethan(a, b)
add(a, b)
calculategmean(a, b)
names("alok", "tiwari")
names("lucky", "tiwari")

print("\n\n\n\n** Recursion Function **")


# Recursion in the process of defining something in terms of itself.

# In python,we know that a function can call other functions.It is even possible for the function to call itself.
# These types of construct are termed as recursive functions.

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


num = 7
print("Number:", num)
print("Number:", factorial(num))


def is_even(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even(n - 2)


print(is_even(4))
print(is_even(5))

print("\n\n\n\n** Lambda  Function **")


# In python a lambda function is a small anonymous function without a name .It defined using the lambda keyword and
# has the following syntax:- lambda arguments:expression

# lambda functions is often used in situations where a small function is required for a short period of time .they
# are commonly used as arguments to higher-order functions,to such as map ,filter and reduce

# Here is an example of how to use a lamda function:-

def doubble(x):
    return x * 2  # function to double the input


x = 10
print(doubble(x))
y = 60
a = lambda y: y * 2  # lambda function to double the input
print(a(y))


# The above Lambda function has the same functionality as the double function defined earlier .However , the lambda
# function is anonymous,as it does not have a name.

# lambda functions can have multiple arguments,just like regular functions.Here is an example of a lambda function
# with multiple arguments

def multiply(x, y):
    return x * y  # function to calculate the product of two number .


x = 2
y = 3
c = multiply(x, y)
print(c)

v = lambda x, y: x * y  # lambda function to calculate the product of two number .
print(v(x, y))

# lambda function can also include multiple statements, but they are limited to a single expression, for example :
# lambda function to calculate the product of two numbers with additional print statement.

s = lambda l, z: print(f'{l}*{z}={l * z}')
s(20,1)

# In the above example , the lambda function include a print statement,but it is still limited to a single
#  expression .

# lambda functions are often used in conjunction with higher order functions, such as map filter and reduce which we
# will took in later.


