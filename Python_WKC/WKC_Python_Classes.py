# Class:
# A class is a blueprint for creating objects (a particular data structure),
# providing initial values for state (member variables or attributes), and
# implementations of behavior (member functions or methods).
# Example:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
    
# Subclass:
# A subclass is a class that inherits from another class, called a superclass.
# The subclass can override or extend the functionality of the superclass.
# Example:
class Corgie(Dog):
    def bark(self):
        return "Woof! Woof!"
    
# Object:
# An object is an instance of a class. It can store data using attributes
# and perform actions using methods.
# Example:
dog = Dog("Buddy", 5)
print(dog.name)  # Output: Buddy
print(dog.age)   # Output: 5

# Inheritance:
# Inheritance is a mechanism in which a new class inherits attributes and
# methods from an existing class. The new class is called a subclass, and
# the existing class is called a superclass.
# Example:
class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("Dog")
        self.name = name
        self.age = age

# Encapsulation:
# Encapsulation is the bundling of data (attributes) and methods (functions)
# that operate on the data into a single unit called a class. It is used to
# restrict access to certain components of the object.
# Example:
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
# Polymorphism:
# Polymorphism is the ability of an object to take on many forms. It allows
# objects of different classes to be treated as objects of a common superclass.
# Example:
class Cat:
    def speak(self):
        return "Meow!"
    
class Dog:
    def speak(self):
        return "Woof!"
    
def make_sound(animal):
    return animal.speak()   

# Abstraction:
# Abstraction is the process of hiding the complex implementation details
# and showing only the necessary features of an object. It helps reduce
# programming complexity and effort.
# Example:
class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"