# Implementation of Multiple Inheritance
# Create two base classes:
# Flyable: has a method fly()
# Swimmable: has a method swim()
# Now create a derived class Amphibian that inherits from
# both classes and implements both methods.

class Flyable:
    def fly(self):
        print("I can Fly!")

class Swimmable:
    def swim(self):
        print("I can swim!")

class Amphibian(Flyable, Swimmable):
    def display(self):
        print("I can Fly!")
        print("I can swim!")

frog = Amphibian()
frog.fly()
frog.swim()