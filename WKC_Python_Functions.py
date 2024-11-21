# Python Functions:
# Functions are blocks of code that perform a specific task. They allow you to
# reuse code, improve readability, and organize your program. Functions in
# Python are defined using the "def" keyword followed by the function name and
# parentheses containing any parameters. The function body is indented and
# contains the code to be executed when the function is called. Functions can
# return a value using the "return" keyword. If no return value is specified,
# the function returns "None" by default. Functions can also have default
# parameters and keyword arguments. Default parameters have a default value
# assigned to them, while keyword arguments are passed by name instead of
# position. Functions can also accept a variable number of arguments using
# the "*" and "**" operators. The "*" operator collects positional arguments
# into a tuple, while the "**" operator collects keyword arguments into a
# dictionary. Functions can be defined inside other functions and can be
# passed as arguments to other functions. Functions can also be stored in
# variables and returned from other functions. Python has many built-in
# functions, such as "print()", "len()", and "range()", that perform common
# tasks. You can also define your own functions to perform custom tasks.
# Example:
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)  # Output: Hello, Alice

# Default Parameters:
# Default parameters are parameters that have a default value assigned to them.
# If no value is provided for a default parameter, the default value is used
# instead. Default parameters are specified in the function definition using
# the assignment operator "=".
# Example:
def greet(name="World"):
    return f"Hello, {name}!"

result = greet()
print(result)  # Output: Hello, World

result = greet("Alice")
print(result)  # Output: Hello, Alice

# Keyword Arguments:
# Keyword arguments are arguments that are passed by name instead of position.
# This allows you to specify which parameter each argument corresponds to.
# Keyword arguments are specified using the parameter name followed by the
# assignment operator "=".
# Example:
def greet(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

result = greet(first_name="Alice", last_name="Smith")
print(result)  # Output: Hello, Alice Smith

result = greet(last_name="Smith", first_name="Alice")
print(result)  # Output: Hello, Alice

# Variable Number of Arguments:
# Functions can accept a variable number of arguments using the "*" and "**"
# operators. The "*" operator collects positional arguments into a tuple,
# while the "**" operator collects keyword arguments into a dictionary.
# Example:
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

result = add(1, 2, 3, 4, 5)
print(result)  # Output: 15

def greet(**kwargs):
    return f"Hello, {kwargs['first_name']} {kwargs['last_name']}!"

result = greet(first_name="Alice", last_name="Smith")
print(result)  # Output: Hello, Alice Smith

# Nested Functions:
# Functions can be defined inside other functions. These nested functions are
# only accessible within the scope of the outer function. Nested functions can
# be used to encapsulate functionality and improve code organization.
# Example:
def outer_function():
    def inner_function():
        return "Hello, World!"
    return inner_function()

result = outer_function()
print(result)  # Output: Hello, World!

# Higher-Order Functions:
# Functions can be passed as arguments to other functions. These functions are
# called higher-order functions. Higher-order functions allow you to abstract
# common functionality into reusable components.
# Example:
def greet(name):
    return f"Hello, {name}!"

def shout(greet_func, name):
    message = greet_func(name)
    return message.upper()

result = shout(greet, "Alice")
print(result)  # Output: HELLO, ALICE!

# Returning Functions:
# Functions can be stored in variables and returned from other functions. This
# allows you to create functions dynamically based on certain conditions.
# Example:
def greet():
    def inner_greet(name):
        return f"Hello, {name}!"
    return inner_greet

greet_func = greet()
result = greet_func("Alice")
print(result)  # Output: Hello, Alice

# Built-In Functions:
# Python has many built-in functions that perform common tasks. Some of the
# most commonly used built-in functions include "print()", "len()", and
# "range()". You can also define your own functions to perform custom tasks.
# Example:
result = print("Hello, World!")  # Output: Hello, World!
print(result)  # Output: None

result = len([1, 2, 3, 4, 5])
print(result)  # Output: 5

# Top 25 Most Used Python Built-In Functions:
# 1. print(): Outputs text to the console.
#    Example: print("Hello, World!")
# 
# 2. len(): Returns the length of an object.
#    Example: len([1, 2, 3])
# 
# 3. range(): Generates a sequence of numbers.
#    Example: range(5)
# 
# 4. type(): Returns the type of an object.
#    Example: type(42)
# 
# 5. int(): Converts a value to an integer.
#    Example: int("42")
# 
# 6. float(): Converts a value to a floating-point number.
#    Example: float("3.14")
# 
# 7. str(): Converts a value to a string.
#    Example: str(42)
# 
# 8. list(): Converts an iterable to a list.
#    Example: list((1, 2, 3))
# 
# 9. dict(): Creates a dictionary.
#    Example: dict(name="Alice", age=25)
# 
# 10. set(): Creates a set.
#    Example: set([1, 2, 3])
# 
# 11. tuple(): Converts an iterable to a tuple.
#    Example: tuple([1, 2, 3])
# 
# 12. bool(): Converts a value to a boolean.
#    Example: bool(1)
# 
# 13. sum(): Returns the sum of an iterable.
#    Example: sum([1, 2, 3])
# 
# 14. max(): Returns the largest item in an iterable.
#    Example: max([1, 2, 3])
# 
# 15. min(): Returns the smallest item in an iterable.
#    Example: min([1, 2, 3])
# 
# 16. abs(): Returns the absolute value of a number.
#    Example: abs(-42)
# 
# 17. round(): Rounds a number to a specified number of decimal places.
#    Example: round(3.14159, 2)
# 
# 18. sorted(): Returns a sorted list from an iterable.
#    Example: sorted([3, 1, 2])
# 
# 19. zip(): Aggregates elements from multiple iterables.
#    Example: zip([1, 2, 3], ['a', 'b', 'c'])
# 
# 20. map(): Applies a function to all items in an iterable.
#    Example: map(str, [1, 2, 3])
# 
# 21. filter(): Filters items in an iterable based on a function.
#    Example: filter(lambda x: x > 0, [-1, 0, 1])
# 
# 22. enumerate(): Returns an enumerate object.
#    Example: enumerate(['a', 'b', 'c'])
# 
# 23. any(): Returns True if any element of an iterable is true.
#    Example: any([False, True, False])
# 
# 24. all(): Returns True if all elements of an iterable are true.
#    Example: all([True, True, True])
# 
# 25. input(): Reads a line of input from the user.
#    Example: input("Enter your name: ")

# User-Defined Functions:
# User-defined functions are functions that you define yourself. They allow
# you to encapsulate functionality and reuse code. User-defined functions are
# defined using the "def" keyword followed by the function name and parentheses
# containing any parameters. The function body is indented and contains the
# code to be executed when the function is called. User-defined functions can
# return a value using the "return" keyword. If no return value is specified,
# the function returns "None" by default.
# Example:
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)  # Output: Hello, Alice

# Lambda Functions:
# Lambda functions are small, anonymous functions defined using the "lambda"
# keyword. They can have any number of arguments but can only have one
# expression. Lambda functions are often used as arguments to higher-order
# functions that require a function as input.

# Syntax:
# lambda arguments: expression

# Example:
add = lambda x, y: x + y
result = add(3, 4)
print(result)  # Output: 7

# Lambda functions are useful for writing short, concise functions that are
# only used once. They are often used in combination with higher-order
# functions like "map()", "filter()", and "sorted()".

# Example:
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4]

sorted_numbers = sorted(numbers, key=lambda x: -x)
print(sorted_numbers)  # Output: [5, 4, 3, 2, 1]

# Recursion:
# Recursion is a programming technique where a function calls itself to solve
# a smaller instance of the same problem. Recursion is often used to solve
# problems that can be broken down into smaller subproblems. Recursion has
# two main components: the base case and the recursive case. The base case
# defines the simplest instance of the problem that does not require further
# recursion. The recursive case defines how the problem is broken down into
# smaller subproblems. Recursion can be a powerful tool for solving complex
# problems, but it can also be less efficient than iterative solutions.
# Example:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
result = factorial(5)
print(result)  # Output: 120

# Recursion can be used to solve a wide range of problems, such as calculating
# factorials, generating Fibonacci numbers, and traversing tree structures.