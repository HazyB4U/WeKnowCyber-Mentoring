# Module:
# A module is a file containing Python code. It can define functions, classes,
# and variables. Modules are used to organize code into logical units and
# reuse code across multiple files.
# Example:
# Create a file named "math_utils.py" with the following code:
# def add(a, b):
#     return a + b
#   
# def subtract(a, b):
#     return a - b
#
# Import the module in another file:
# import math_utils
# result = math_utils.add(3, 4)

# Package:
# A package is a collection of modules. It allows you to organize your code
# into multiple directories and files. Packages are used to create a hierarchy
# of modules and avoid naming conflicts.
# Example:
# Create a directory named "my_package" with the following structure:
# my_package/

# ├── __init__.py
# ├── math_utils.py
# └── string_utils.py
#
# In the __init__.py file, you can import modules to make them accessible:
# from . import math_utils
# from . import string_utils
#   
# Import the package in another file:
# import my_package
# result = my_package.math_utils.add(3, 4)

# Function:
# A function is a block of code which only runs when it is called. You can
# pass data, known as parameters, into a function. A function can return data
# as a result.
# Example:
def greet(name):
    return f"Hello, {name}!"

# Library:
# A library is a collection of tools, like functions and classes, that can be
# used in your python scripts.
# There are many great libraries that have been developed by the python
# community that do all kinds of crazy functions. If you have something
# you want your code to do there may already be a function for it. That
# is not to say that there will be no thought needed for how to integrate
# the library into your code.
# Example of importing a library:
import math

# Using the math library to calculate the square root of 16
result = math.sqrt(16)

# Importing Libraries:
# 
# 1. import library:
#    This imports the entire library and you can access its functions and classes
#    using the library name.
#    Example:
#    import math
#    result = math.sqrt(16)
# 
# 2. import library as alias:
#    This imports the entire library and assigns it an alias, which can be used
#    to access its functions and classes. This is useful for shortening long
#    library names.
#    Example:
#    import numpy as np
#    array = np.array([1, 2, 3])
# 
# 3. from library import thing:
#    This imports a specific function, class, or variable from a library, allowing
#    you to use it directly without the library name. There are some additional 
#    advantages to importing only the functions you need, such as improved
#    performance and reduced memory usage.
#    Example:
#    from math import sqrt
#    result = sqrt(16)

# Commonly Used Python Libraries:
# 
# 1. NumPy: Used for numerical computing with powerful array objects.
#    import numpy as np
# 
# 2. pandas: Used for data manipulation and analysis.
#    import pandas as pd
# 
# 3. matplotlib: Used for creating static, animated, and interactive visualizations.
#    import matplotlib.pyplot as plt
# 
# 4. requests: Used for making HTTP requests.
#    import requests
# 
# 5. Flask: A micro web framework for Python.
#    from flask import Flask
# 
# 6. Django: A high-level Python web framework.
#    import django
# 
# 7. scikit-learn: Used for machine learning and data mining.
#    import sklearn
# 
# 8. TensorFlow: An open-source library for machine learning.
#    import tensorflow as tf
# 
# 9. BeautifulSoup: Used for web scraping purposes to pull data out of HTML and XML files.
#    from bs4 import BeautifulSoup
# 
# 10. Pygame: Used for writing video games.
#    import pygame
