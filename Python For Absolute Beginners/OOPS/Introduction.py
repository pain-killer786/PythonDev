# What is Object Oriented Programming
# -> Object oriented programming is a programming paradigm where the software design revolves around objects/data rather than functions.

#Why use OOPs in Python?
# Helps to mimic real world entities & their interactions
# Code reusability
# Organisation & maintainability of code

#What are Classes?
# Used defined data types
# Classes are the blueprint/template for an object

#What are Objects?
# Object is an instance of type class
# Mimics real world entities

class Student:
    
    def set_name(self,name): #bSelf parameter signifies the object
        self.name=name
        
    def get_name(self):
        return self.name
    
student1=Student()
student1.set_name("Shehnaz")
print(student1.name)

class Myclass:
    x=5
p1=Myclass()
print(p1.x)

class Person:
    def __init__(self, name , age ):
        self.name = name
        self.age=age
p1=Person("John",36)

print(p1.name)
print(p1.age)
