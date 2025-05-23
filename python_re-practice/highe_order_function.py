print("**Higher-Order Function**")
"""
 In python,the map, filter and reduce function are built-in functions that allow you to apply a function ,
 to a sequence of elements and return a new sequence. these function are known as higher-order functions as they 
 take other function as arguments.
"""

print("*map*")
"""
The map function applies a function to each element in a sequence and  return a new sequence containing the
transformed elements .The map function has the following syntax:-
map(function,iterable)
"""

# the function argument is a function that is applied to each element in iterable argument. the iterable argument can
# be a list ,tuple,or any other iterable object

# Here is an example of how to use map function.

number = [1, 2, 3, 4, 5, 6]  # list of number

double = map(lambda x: x * 2, number)  # Double each number using the map function

print(list(double))  # print the doubled number

# In the above example ,the lambda x:x*2 is used to double each element in the numbers list. the map function applies
# the lambda function to each element  in the list and returns a new list containing the double number.

print("\n\n*Filter*")
"""
The filter function filter a sequence of elements based on given predicate (a function that returns a boolean 
value)and returns a new sequence containing only the elements that meet the predicate. the filter function has the 
following syntax:-
filter(predicate,iterable)
"""
# The predicate argument is a function that returns a boolean value and is applied to each element in the iterable
# argument .The iterable argument can be a list ,tuple or any other iterable object

#  Here is an example of how to use the filter function :-

num = [1, 2, 3, 4, 5, 6]  # list of number

even = filter(lambda x: x % 2 == 0, num)  # get only the even numbers using the filter function .

print(list(even))  # print the even number

# In the above example,the lambda function lambda x:x % 2 == 0 is used to filter the number list and return only the
# even element numbers .the filter function applies the lambda function to each element in the list and returns a new
# list containing only the even numbers.

print("\n\n*Reduce*")
"""
The reduce function is a higher-order function that applies a function to a sequence and returns a single value .
It is a part of the functools module in python and has the following syntax:-
reduce(function,iterable)
"""
# the function argument is a function that takes in two arguments a returns a single value. the iterable argument is
# a sequence of elements, such as a list or tuple

# the reduce function  applies the function to the first two elements in the iterable and then applies the function to
# the result and the next element , and so on . the reduce function returns the final result

#  Here is an example of how to use the reduce function :-

from functools import reduce  # import the module

nums = [1, 2, 3, 4, 5, 6, 7]  # list of number

sum = reduce(lambda x, y: x + y, nums) # calculte the sum of the numbers using the reduce function

print(sum) # print the sum

# In the above example , the return function applies the lambda x,y:x+y to the elements inn the numbers list. the
# lambda function adds the two arguments x and y and return the result .The reduce function applies the lambda
# function to the first two elements in the list (1 and 2 ) the applied the function to the result (3) and the next
# elements(3),and so on . the final result is the sum of all the elements in the list ,which is 15.

# It is important to note that the reduce function requires the functools modules to be imported in order to use it.
