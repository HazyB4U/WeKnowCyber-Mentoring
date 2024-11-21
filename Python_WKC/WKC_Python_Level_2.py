# Tuples:
# Tuples are ordered, immutable collections of items that can contain
# elements of different data types. Once created, their elements cannot
# be changed.
# Example:
coordinates = (3, 4)
colors = ("red", "green", "blue")
mixed = (1, "Alice", True)
print(coordinates)  # Output: (3, 4)
print(colors)       # Output: ('red', 'green', 'blue')
print(mixed)        # Output: (1, 'Alice', True)

# Tuple Unpacking:
# Tuple unpacking is used to assign the elements of a tuple to multiple
# variables in a single statement.
# Example:
coordinates = (3, 4)
x, y = coordinates
print(x)  # Output: 3
print(y)  # Output: 4

# Tuples are used over lists when you need an immutable sequence of elements, 
# meaning the data should not change after creation. This immutability can 
# provide performance benefits and ensure data integrity. Tuples are also 
# used as keys in dictionaries because they are hashable, whereas lists are not.

# Dictionaries:
# Dictionaries are collections of key-value pairs that allow you to store
# and retrieve data using keys. They are unordered and mutable.
# Example:
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing Dictionary Elements:
# Dictionary elements can be accessed using their keys.
# Example:
person = {"name": "Alice", "age": 25, "city": "New York"}
print(person["name"])  # Output: Alice
print(person["age"])   # Output: 25

# Modifying Dictionary Elements:
# Dictionary elements can be modified by assigning a new value to a key.
# Example:
person = {"name": "Alice", "age": 25, "city": "New York"}
person["age"] = 26
print(person)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Dictionary Methods:
# Dictionary methods are functions that operate on dictionaries and can
# be used to manipulate and transform them.
# Example:
person = {"name": "Alice", "age": 25, "city": "New York"}

# Add a new key-value pair
person["email"] = "arthur@camelot.silly"

# Remove a key-value pair
person.pop("age")

# Check if a key exists
print("email" in person)  # Output: True

# Sets:
# Sets are unordered collections of unique elements. They are mutable,
# meaning their elements can be changed after creation.

# Example:
colors = {"red", "green", "blue"}
numbers = {1, 2, 3, 4, 5}
mixed = {1, "Alice", True}

print(colors)  # Output: {'red', 'green', 'blue'}
print(numbers)  # Output: {1, 2, 3, 4, 5}
print(mixed)  # Output: {1, 'Alice', True}

# Set Operations:
# Sets support various operations such as union, intersection, difference,
# and symmetric difference.

# Example:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set1 & set2)  # Output: {3}

# Difference
print(set1 - set2)  # Output: {1, 2}

# Symmetric Difference
print(set1 ^ set2)  # Output: {1, 2, 4, 5}

# Set Methods:
# Set methods are functions that operate on sets and can be used to
# manipulate and transform them.

# Example:
colors = {"red", "green", "blue"}

# Add an element to the set
colors.add("yellow")

# Remove an element from the set
colors.remove("green")

# Check if an element exists in the set
print("red" in colors)  # Output: True

# Conditional Statements:
# Conditional statements are used to perform different actions based on
# different conditions. They allow you to control the flow of a program.
# Example:
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Loops:
# Loops are used to execute a block of code repeatedly. There are two main
# types of loops in Python: for loops and while loops.
# Example:
# For Loop:
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
    
# While Loop:
count = 0
while count < 5:
    print(count)
    count += 1

# Loop Control Statements:
# Loop control statements are used to change the execution of a loop.
# There are three main loop control statements in Python: break, continue,
# and pass.
# Example:
# Break:
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number)

# Continue:
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)

# Pass:
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        pass
    print(number)

# Functions:
# Functions are blocks of code that perform a specific task. They allow
# you to reuse code, improve readability, and organize your program.
# Example:
def greet(name):
    return f"Hello, {name}!"

# List comprehension:
# List comprehension is a concise way to create lists in Python. It allows
# you to create a new list by applying an expression to each item in an
# existing list.
# Example:
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
print(squared)  # Output: [1, 4, 9, 16, 25]

# List comprehension can also include conditional statements to filter the
# elements of the original list.
# Example:
numbers = [1, 2, 3, 4, 5]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # Output: [2, 4]

# Error Handling:
# Error handling allows you to handle exceptions and errors that occur
# during the execution of a program. It helps prevent the program from
# crashing and provides a way to recover from errors.
# Example:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Commonly Used Error Handling Built-In Exceptions:
# 
# 1. Exception: Base class for all exceptions.
#    Example:
    try:
        pass # code that may raise an exception
    except Exception as e:
        print(e)
         
# 2. Zero#DivisionError: Raised when division or modulo by zero takes place.
#    Example:
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")
 
# 3. ValueError: Raised when a function receives an argument of the right type but inappropriate value.
#    Example:
    try:
        int("abc")
    except ValueError:
        print("Invalid literal for int()")
# 
# 4. TypeError: Raised when an operation or function is applied to an object of inappropriate type.
#    Example:
    try:
        "2" + 2
    except TypeError:
        print("Cannot concatenate str and int")
# 
# 5. IndexError: Raised when a sequence subscript is out of range.
#    Example:
    try:
        lst = [1, 2, 3]
        print(lst[5])
    except IndexError:
        print("List index out of range")
# 
# 6. KeyError: Raised when a dictionary key is not found.
#    Example:
    try:
        d = {'a': 1}
        print(d['b'])
    except KeyError:
        print("Key not found in dictionary")
# 
# 7. AttributeError: Raised when an attribute reference or assignment fails.
#    Example:
    try:
        x = None
        x.append(1)
    except AttributeError:
        print("NoneType object has no attribute 'append'")
# 
# 8. ImportError: Raised when an import statement fails to find the module definition or when a from ... import fails to find a name that is to be imported.
#    Example:
    try:
        pass # non_existent_module
    except ImportError:
        print("Module not found")
 
# 9. FileNotFoundError: Raised when a file or directory is requested but doesn't exist.
#    Example:
    try:
        open("non_existent_file.txt")
    except FileNotFoundError:
        print("File not found")
# 
# 10. IOError: Raised when an I/O operation (such as a print statement, the built-in open() function, or a method of a file object) fails for an I/O-related reason.
#    Example:
    try:
        open("/etc/passwd", "w")
    except IOError:
        print("I/O error")
