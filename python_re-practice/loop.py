if __name__ == '__main__':
    print("**Loop in python**")

# sometimes a programmer wants to execute a group of statements a certain number of times.this can be done using
#  loops . based on this loops are future classified into following main type

# for loop :- can iterate over a sequence  of iterate object in python .iterating over a sequence is nothing but
# iterating over string list tuple sets and dictionaries

name = "Abhishek"  # iterating over a string
for i in name:
    print(i, end=",")

colors = ["red", "blue", "green", "yellow", "white"]
for x in colors:
    print(x)

# range(): we can use the range() function
# what if we do not want to iterate over a sequence ?
# what if we want to use for loop for specific number of time ?

for k in range(5):
    print(k + 1)

# but we can loop over a specific range()

for k in range(4, 9):
    print(k)

# while loop :- as the name suggests while loops execute statements while the condition is True . As soon as the
# condition become false ,the interpreter comes out of the while loop

count = 5
while count > 0:
    print(count)
    count = count - 1

# Else with While loop :- we can even use the else statement with that the while loop.Essentially what the else
# statement  does is that as soon as the while loop condition  become false ,the interpreter comes out of the while
# loop and the else statement is executed

a = 5
while a > 0:
    print(a)
    a = a - 1
else:
    print("counter is 0")

