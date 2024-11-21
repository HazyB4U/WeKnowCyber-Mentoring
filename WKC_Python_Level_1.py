#!/usr/bin/env python3

# This is a learning space for the mentorship program of We Know Cyber

# Script:
# A script is a file containing a sequence of Python statements that can be
# executed by the Python interpreter. Scripts are used to automate tasks,
# perform calculations, and run programs.
# Example:
# Create a file named "hello.py" with the following code:
# print("Hello, World!")
#  
# Run the script using the Python interpreter:
# python hello.py
# Python Data Types:
# 

# 1. int: Integer data type, represents whole numbers.
#    Example: 42, -7
# 
# 2. float: Floating-point data type, represents real numbers with decimal points.
#    Example: 3.14, -0.001
# 
# 3. str: String data type, represents sequences of characters.
#    Example: "Hello, World!", 'Python'
# 
# 4. bool: Boolean data type, represents True or False values.
#    Example: True, False
# 
# 5. list: List data type, represents ordered collections of items.
#    Example: [1, 2, 3], ['a', 'b', 'c']
# 
# 6. tuple: Tuple data type, represents ordered, immutable collections of items.
#    Example: (1, 2, 3), ('a', 'b', 'c')
# 
# 7. dict: Dictionary data type, represents collections of key-value pairs.
#    Example: {'name': 'Alice', 'age': 25}
# 
# 8. set: Set data type, represents unordered collections of unique items.
#    Example: {1, 2, 3}, {'a', 'b', 'c'}
# 
# 9. frozenset: Immutable version of set.
#    Example: frozenset([1, 2, 3]), frozenset(['a', 'b', 'c'])
# 
# 10. NoneType: Represents the absence of a value.
#    Example: None

# Variables:
# A variable is a named storage location in memory that can hold a value.
# Variables are used to store data that can be referenced and manipulated
# in a program.
# Example:
x = 42
name = "Alice"

# Comments:
# Comments are used to document code and improve readability. They are
# ignored by the Python interpreter and are not executed.
# Example:
# This is a single-line comment
# This is another single-line comment

# Multi-line comments:
'''This is a multi-line comment
 It spans multiple lines
 and is enclosed in triple quotes'''

# Arithmetic Operators:
# Arithmetic operators are used to perform mathematical operations on
# numeric values.
#
# 1. Addition (+): Adds two operands.
# 2. Subtraction (-): Subtracts the second operand from the first.
# 3. Multiplication (*): Multiplies two operands.
# 4. Division (/): Divides the first operand by the second.
# 5. Modulus (%): Returns the remainder of the division.
# 6. Exponentiation (**): Raises the first operand to the power of the second.
# 7. Floor Division (//): Returns the integer part of the division.
# Example:
x = 10
y = 3
print(x + y)  # 13
print(x - y)  # 7
print(x * y)  # 30
print(x / y)  # 3.3333333333333335
print(x % y)  # 1
print(x ** y) # 1000
print(x // y) # 3

# Comparison Operators:
# Comparison operators are used to compare two values and return a boolean
# result (True or False).
#   
# 1. Equal to (==): Returns True if the operands are equal.
# 2. Not equal to (!=): Returns True if the operands are not equal.
# 3. Greater than (>): Returns True if the first operand is greater than the second.
# 4. Less than (<): Returns True if the first operand is less than the second.
# 5. Greater than or equal to (>=): Returns True if the first operand is greater than or equal to the second.
# 6. Less than or equal to (<=): Returns True if the first operand is less than or equal to the second.
# Example:
x = 10
y = 5
print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False

# Logical Operators:
# Logical operators are used to combine multiple conditions and return a
# boolean result (True or False).
#
# 1. and: Returns True if both conditions are True.
# 2. or: Returns True if at least one condition is True.
# 3. not: Returns True if the condition is False.
# Example:
x = 10
y = 5
z = 15
print(x > y and x < z)  # True
print(x > y or x > z)   # True
print(not x > y)        # False

# Assignment Operators:
# Assignment operators are used to assign values to variables.
#
# 1. =: Assigns the value of the right operand to the left operand.
# 2. +=: Adds the right operand to the left operand and assigns the result to the left operand.
# 3. -=: Subtracts the right operand from the left operand and assigns the result to the left operand.
# 4. *=: Multiplies the left operand by the right operand and assigns the result to the left operand.
# 5. /=: Divides the left operand by the right operand and assigns the result to the left operand.
# 6. %=: Computes the modulus of the left operand with the right operand and assigns the result to the left operand.
# 7. **=: Raises the left operand to the power of the right operand and assigns the result to the left operand.
# 8. //=: Performs floor division on the left operand by the right operand and assigns the result to the left operand.
# Example:
x = 10
x += 5  # Equivalent to x = x + 5   (x = 15)
x -= 3  # Equivalent to x = x - 3   (x = 12)
x *= 2  # Equivalent to x = x * 2   (x = 24)
x /= 4  # Equivalent to x = x / 4   (x = 6.0)
x %= 5  # Equivalent to x = x % 5   (x = 1.0)
x **= 3 # Equivalent to x = x ** 3  (x = 1.0)
x //= 2 # Equivalent to x = x // 2  (x = 0.0)

# Identity Operators:
# Identity operators are used to compare the memory locations of two objects.
#
# 1. is: Returns True if both operands are the same object.
# 2. is not: Returns True if both operands are not the same object.
# Example:
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)   # False
print(x is z)   # True
print(x is not y) # True

# Membership Operators:
# Membership operators are used to test if a value is present in a sequence.
#   
# 1. in: Returns True if the value is present in the sequence.
# 2. not in: Returns True if the value is not present in the sequence.
# Example:
x = [1, 2, 3]
print(1 in x)   # True
print(4 not in x) # True

# Strings:
# Strings are sequences of characters enclosed in single or double quotes.
# They can be manipulated using various string methods and operators.
# Example:
name = "Alice"
message = 'Hello, World!'
print(name)     # Output: Alice
print(message)  # Output: Hello, World!

# String Concatenation:
# String concatenation is the process of combining two or more strings
# into a single string.
# Example:
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)  # Output: Alice Smith

# String Formatting:
# String formatting allows you to create dynamic strings by inserting
# variables and expressions into a string.
# Example:
name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)  # Output: My name is Alice and I am 25 years old.

# String Methods:
# String methods are functions that operate on strings and can be used to
# manipulate and transform them.
# Example:
message = "Hello, World!"
print(message.upper())    # Output: HELLO, WORLD!
print(message.lower())    # Output: hello, world!
print(message.replace("Hello", "Hi"))  # Output: Hi, World!
print(message.split(","))  # Output: ['Hello', ' World!']

# Lists:
# Lists are ordered collections of items that can contain elements of
# different data types. They are mutable, meaning their elements can be
# changed after creation.
# Example:
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "Alice", True]
print(numbers)  # Output: [1, 2, 3, 4, 5]
print(names)    # Output: ['Alice', 'Bob', 'Charlie']
print(mixed)    # Output: [1, 'Alice', True]

# List Indexing:
# List indexing is used to access individual elements in a list by their
# position (index). Indexing starts at 0 for the first element.
# Example:
numbers = [1, 2, 3, 4, 5]
print(numbers[0])  # Output: 1
print(numbers[2])  # Output: 3

# List Slicing:
# List slicing is used to extract a subsequence of elements from a list.
# It is done by specifying a start index, an end index, and an optional
# step size.
# Example:
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [2, 3, 4]
print(numbers[::2])  # Output: [1, 3, 5]

# List Methods:
# List methods are functions that operate on lists and can be used to
# manipulate and transform them.
# Example:
numbers = [1, 2, 3, 4, 5]
numbers.append(6)   # Add an element to the end of the list
numbers.insert(2, 7)  # Insert an element at a specific index
numbers.remove(3)   # Remove the first occurrence of an element
numbers.pop()       # Remove the last element from the list
numbers.reverse()   # Reverse the order of elements in the list
print(numbers)      # Output: [7, 2, 4, 5]