"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
    calc = raw_input("> ")

    tokens = calc.split(" ")

    x = int(tokens[1])
    y = int(tokens[2])

    if tokens[0] == "+":
        print add(x, y)

    if tokens[0] == "-":
        print subtract(x, y)

    if tokens[0] == "*":
        print multiply(x, y)

    if tokens[0] == "/":
        print divide(x, y)

    if tokens[0] == "square":
        print square(x)

    if tokens[0] == "cube":
        print cube(x)

    if tokens[0] == "pow":
        print power(x, y)

    if tokens[0] == "mod":
        print mod(x, y)