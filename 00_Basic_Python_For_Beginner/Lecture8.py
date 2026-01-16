# OOP in Python
# Before creating objects, we need to create a class

# Class is is a blueprint for creating objects
class Student:
    #name = "John"  # Attribute
    # Constructor
    def __init__(self, name, marks):  # Constructor
        self.name = name
        self.marks = marks
        print("Adding new student in Database")

   # Object
s1 = Student("Waqar", 97)  # Creating an object of the class Student
print(s1.name, s1.marks)  # Accessing the attribute of the object


# del Keyword
# del s1  # Deleting the object
# __ to make a method or attribute private, it can only be accessed within the class
# __name = "John"  # Private Attribute

 




