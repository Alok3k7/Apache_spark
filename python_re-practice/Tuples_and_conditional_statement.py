print("** tuples**")

# tuple are ordered collection of data items . They  store multiple item in a storage in single variable .Tuple item
# are operated by commas and enclosed with in round bracket(). tuple are unchanged meaning we can not alteration after
# the creation

# store int
tup1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tup1)

# store string
tup2 = ("pratham", "misti", "om")
print(tup2)

details = ("alok", 20, "TYbcaIT", 5.9)
print(details)

# we can access the tuple by indexing

# positive indexing :-as we have seen that tuple items have index as such we can access item using these index.
country = ('USA', 'Russia', 'France', 'Australia', 'germany')

print(country[0])
print(country[1])
print(country[4])

# negative indexing:- similar to positive indexing negative indexing is also  used to access items but  from the end
# of the tuple
country = ('Spain', 'Italy', 'USA', 'Russia', 'France', 'Australia', 'germany')

print(country[-2])
print(country[-3])
print(country[-7])

# check item :- we can  check if a given item is present in tuple .this is done using the in keyword
if "germany" in country:
    print("Germany is present")
else:
    print("Germany is absent")

# range of index :- you can print a range of tuple items by specifying where do want start ,where do you want to end
# if you want to skip element between

animal = ('dogs', 'cat', 'lion', 'tiger', 'mouse', 'pig', 'donkey', 'monkey')

print(animal[::2])
print(animal[3:8:2])

print("\n\n\n**  Conditional statement **")
# if-else statement sometime we have to control the flow according to condition that help check the condition if
# condition is true its print  what we write . if condition false its print else part.

# base on this the condition statement are further classified into following help
# if
# if - else
# if-elif-else
# nested if -else-elif

# And if else statement evaluates like this :- if the expression evaluates true:- Execute the block of code inside if
# statement. After execution return to the code out of the if else block

# if the expression evaluation false :- Execute the block of code inset else statement After execution return to the
# code out of the if else block

apple_price = 210
budget = 1000
if apple_price <= budget:
    print("We want purchase 1kg apple.")
else:
    print("we don't have enough budget.")

# elif statement:- sometime the programmer may want to evaluate more than one condition ,this can be done using and
# elif statement

num = 0
if num < 0:
    print("Number is negative.")
elif num == 0:
    print("Number is Zero.")
else:
    print("Number is positive")

# Nested if Statement :- we can use if ,if-else,elif statement inside other if statements as well

num1 = 18
if num1 == 0:
    print("Number is negative")
elif num1 > 0:
    if num1 <= 10:
        print("Number is between 1-10")
    elif 10 < num1 <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is 0")
