#!/bin/python3

# variables and methods
quote = "Rem tene verba sequentur."
print(quote.upper())  # uppercase
print(quote.lower())  # lowercase
print(quote.title())  # title case

print(len(quote))

name = "Marco"  # string
age = 16  # int int(16)
gpa = 3.7  # float float(3.7)

print(int(age))
print(int(16.9))

print("My name is " + name + " and I am " + str(age) + " years old.")
age += 1
print(age)

birthday = 1
age += birthday
print(age)

print("\n")
# functions
print("Here is an example function:")


def who_am_i():  # this is a function
    name = "Marco"
    age = 16
    print("My name is " + name + " and I am " + str(age) + " years old.")


who_am_i()

# adding parameters


def add_one_hundred(num):
    print(num + 100)


add_one_hundred(100)

# multiple parameters


def add(x, y):
    print(x + y)


add(7, 7)


def multiply(x, y):
    return x * y


print(multiply(7, 7))


def square_root(x):
    print(x ** .5)


square_root(64)


def nl():
    print("\n")


nl()

# boolean expressions (True or False)
print("Boolean expressions:")

bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9
print(bool1, bool2, bool3, bool4)
print(type(bool1))

nl()

# Relational and Boolean operators
greather_than = 7 > 5
less_than = 5 < 7
greather_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7)  # true
test_and2 = (7 > 5) and (5 > 7)  # false
test_or = (7 > 5) or (5 < 7)  # true
test_or2 = (7 > 5) or (5 > 7)  # true

test_not = not True  # false

nl()

# conditional statements


def drink(money):
    if money >= 2:
        return "You've got yourself a drink!"
    else:
        return "No drink for you!"


print(drink(3))
print(drink(1))


def alcohol(age, money):
    if (age > 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Come back with more money."
    elif (age < 21) and (money >= 5):
        return "Nice try, kid!"
    else:
        return "You're too poor and too young"


print(alcohol(21, 5))
print(alcohol(21, 4))
print(alcohol(20, 4))

nl()

# list - have brackets []
movies = ["Harry Potter and The Deathly Allows Part II",
          "The Theory of Everything", "School of Rock", "The Super Mario Bros. Movie"]

print(movies[1])  # return the second item
print(movies[0])  # returns the first item in the list
print(movies[1:4])
print(movies[1:])
print(movies[:1])
print(movies[:2])
print(movies[-1])

print(len(movies))
movies.append("JAWS")
print(movies)

movies.pop()
print(movies)

movies.pop(0)
print(movies)

nl()

# tuples - do not change, ()
grades = ("a", "b", "c", "d", "f")
print(grades[1])

nl()

# looping
# for loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
    print(x)

# while loops - execute as long as true
i = 1
while i < 10:
    print(i)
    i += 1
