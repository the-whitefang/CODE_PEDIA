# Basic Inheritance
# Q1. Create a Parent class Animal with a method
# speak(), and a Child class Dog that inherits
# from Animal. Override the speak() method in
# Dog to print "Bark" instead of
# "Some generic sound".

class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

dog = Dog()
dog.speak()