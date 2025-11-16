"""
Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
Addition
Subtraction
Multiplication
Division
"""


num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

add = num_1 + num_2
sub = num_1 - num_2
multi = num_1 * num_2
div = num_1 / num_2

print("Addition: ", add, "\nSubtraction: ", sub, "\nMultiplication: ", multi, "\nDivision: ", div)