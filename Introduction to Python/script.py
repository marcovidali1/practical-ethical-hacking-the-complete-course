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
