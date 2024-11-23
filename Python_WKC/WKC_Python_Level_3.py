# Python Decorators:
# Python decorators are a powerful and expressive feature that allows you to
# modify or extend the behavior of functions or methods. Decorators are functions
# that wrap other functions or methods and can add additional functionality to
# them. Decorators are commonly used for logging, authentication, caching, and
# other cross-cutting concerns.

# Example:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# Decorator Syntax:
# Python provides a convenient syntax for applying decorators to functions using
# the "@" symbol. This syntax makes it easier to apply decorators to functions
# and improves code readability.

# Example:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# Decorator with Arguments:
# Decorators can also accept arguments, allowing you to customize their behavior
# based on the arguments provided. This can be useful for creating more flexible
# and reusable decorators.

# Example:
def repeat(num_times):
    def decorator(func):
        def wrapper():
            for _ in range(num_times):
                func()
        return wrapper
    return decorator

@repeat(num_times=3)
def say_hello():
    print("Hello!")
    
say_hello()
# Output:
# Hello!
# Hello!
# Hello!

# Common Uses of Decorators:
# Decorators are a versatile tool in Python and can be used for a variety of
# purposes. Some common uses of decorators include:
# - Logging: Decorators can be used to log information before and after function
#   calls, helping with debugging and monitoring.
# - Authentication: Decorators can be used to enforce authentication and
#   authorization checks before allowing access to certain functions.
# - Caching: Decorators can be used to cache the results of expensive function
#   calls, improving performance by avoiding redundant computations.
# - Rate Limiting: Decorators can be used to limit the rate at which certain
#   functions can be called, preventing abuse or overuse of resources.
# - Error Handling: Decorators can be used to catch and handle exceptions that
#   occur within functions, providing a centralized error handling mechanism.

# Zip Function:
# The zip function in Python is used to combine multiple iterables (such as lists,
# tuples, or strings) into a single iterable of tuples. Each tuple contains the
# corresponding elements from the input iterables.

# Example:
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)

for pair in zipped:
    print(pair)
# Output:
# (1, 'a')
# (2, 'b')
# (3, 'c')

# Unzipping with Zip:
# The zip function can also be used to unzip elements from a list of tuples into
# separate lists. This is done by using the unpacking operator (*) in conjunction
# with the zip function.

# Unpacking Operator:
# The unpacking operator (*) in Python is used to unpack elements from an iterable
# (such as a list or tuple) into individual elements. This can be useful for
# passing multiple arguments to functions, unpacking values from dictionaries,
# and more.

# Example:
numbers = [1, 2, 3, 4, 5]
print(*numbers)  # Output: 1 2 3 4 5

# Unpacking in Function Calls:
# The unpacking operator can be used to pass multiple arguments to a function
# using elements from an iterable.

# Example:
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)
print(result)  # Output: 6

# Unpacking Dictionaries:
# The unpacking operator can also be used to unpack key-value pairs from
# dictionaries into keyword arguments in function calls.

# Example:
def greet(name, age):
    return f"Hello, {name}! You are {age} years old."

person = {"name": "Alice", "age": 25}
result = greet(**person)
print(result)  # Output: Hello, Alice

# Unpacking in List Comprehensions:
# The unpacking operator can be used in list comprehensions to unpack elements
# from nested iterables into a flat list.

# Example:
nested_numbers = [[1, 2], [3, 4], [5, 6]]
flat_numbers = [num for sublist in nested_numbers for num in sublist]
print(flat_numbers)  # Output: [1, 2, 3, 4, 5, 6]

# Unpacking in Tuple Assignments:
# The unpacking operator can be used to assign elements from an iterable to
# multiple variables in a single statement.

# Example:
coordinates = (3, 4)
x, y = coordinates
print(x)  # Output: 3
print(y)  # Output: 4

# Unpacking in Multiple Assignments:
# The unpacking operator can be used in multiple assignments to assign elements
# from an iterable to multiple variables in a single statement.

# Example:
a, b, *rest = [1, 2, 3, 4, 5]
print(a)    # Output: 1
print(b)    # Output: 2
print(rest) # Output: [3, 4, 5]

# Unpacking in Function Returns:
# The unpacking operator can be used to return multiple values from a function
# as a tuple, which can then be unpacked by the caller.

# Example:
def get_coordinates():
    return 3, 4

x, y = get_coordinates()
print(x)  # Output: 3
print(y)  # Output: 4

# Unpacking in Zip:
# The unpacking operator can be used in conjunction with the zip function to
# unzip elements from multiple iterables into separate lists.

# Example:
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)

unzipped_numbers, unzipped_letters = zip(*zipped)
print(unzipped_numbers)  # Output: (1, 2, 3)
print(unzipped_letters)  # Output: ('a', 'b', 'c')

# Unpacking in Dictionary Comprehensions:
# The unpacking operator can be used in dictionary comprehensions to unpack
# key-value pairs from dictionaries into separate keys and values.

# Example:
person = {"name": "Alice", "age": 25}
formatted = {f"{key.capitalize()}: {value}" for key, value in person.items()}
print(formatted)  # Output: {'Name: Alice', 'Age: 25'}

# Unpacking in Nested Unpacking:
# The unpacking operator can be used in nested unpacking to unpack elements
# from nested iterables into individual elements.

# Example:
nested_numbers = [[1, 2], [3, 4], [5, 6]]
a, b, c, d, e, f = [num for sublist in nested_numbers for num in sublist]
print(a, b, c, d, e, f)  # Output: 1 2 3 4 5 6

# Unpacking in Argument Lists:
# The unpacking operator can be used to unpack elements from an iterable into
# individual arguments in a function call.

# Example:
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = add(*numbers)
print(result)  # Output: 6

# Unpacking in Keyword Arguments:
# The unpacking operator can be used to unpack key-value pairs from dictionaries
# into keyword arguments in function calls.

# Example:
def greet(name, age):
    return f"Hello, {name}! You are {age} years old."

person = {"name": "Alice", "age": 25}
result = greet(**person)
print(result)  # Output: Hello, Alice

# Unpacking in List Comprehensions:
# The unpacking operator can be used in list comprehensions to unpack elements
# from nested iterables into a flat list.

# Example:
nested_numbers = [[1, 2], [3, 4], [5, 6]]
flat_numbers = [num for sublist in nested_numbers for num in sublist]
print(flat_numbers)  # Output: [1, 2, 3, 4, 5, 6]

# Unpacking in Tuple Assignments:
# The unpacking operator can be used to assign elements from an iterable to
# multiple variables in a single statement.

# Example:
coordinates = (3, 4)
x, y = coordinates
print(x)  # Output: 3
print(y)  # Output: 4

# Unpacking in Multiple Assignments:
# The unpacking operator can be used in multiple assignments to assign elements
# from an iterable to multiple variables in a single statement.

# Example:
a, b, *rest = [1, 2, 3, 4, 5]
print(a)    # Output: 1
print(b)    # Output: 2
print(rest) # Output: [3, 4, 5]

# Unpacking in Function Returns:
# The unpacking operator can be used to return multiple values from a function
# as a tuple, which can then be unpacked by the caller.

# Example:
def get_coordinates():
    return 3, 4

x, y = get_coordinates()
print(x)  # Output: 3
print(y)  # Output: 4

# Unpacking in Zip:
# The unpacking operator can be used in conjunction with the zip function to
# unzip elements from multiple iterables into separate lists.

# Example:
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)

unzipped_numbers, unzipped_letters = zip(*zipped)
print(unzipped_numbers)  # Output: (1, 2, 3)
print(unzipped_letters)  # Output: ('a', 'b', 'c')

# F-Strings:
# F-strings are a convenient way to format strings in Python by embedding
# expressions within curly braces. F-strings allow you to include variables,
# expressions, and function calls directly within the string, making it easier
# to create formatted output.

# Example:
name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)  # Output: My name is Alice and I am 25 years old.

# F-String Expressions:
# F-strings support a wide range of expressions that can be embedded within the
# curly braces. These expressions can include variables, arithmetic operations,
# function calls, and more.

# Example:
a = 10
b = 5
result = f"{a} + {b} = {a + b}"
print(result)  # Output: 10 + 5 = 15

# F-String Formatting:
# F-strings support various formatting options that allow you to control the
# appearance of the embedded expressions. These options include specifying the
# number of decimal places, padding with zeros, and aligning text.

# Example:
pi = 3.14159
formatted = f"Pi is approximately {pi:.2f}"
print(formatted)  # Output: Pi is approximately 3.14

# F-String Expressions:
# F-strings support a wide range of expressions that can be embedded within the
# curly braces. These expressions can include variables, arithmetic operations,
# function calls, and more.

# Example:
a = 10
b = 5
result = f"{a} + {b} = {a + b}"
print(result)  # Output: 10 + 5 = 15