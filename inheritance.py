# Inheritance = Allows a class to inherit attributes and method from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):  # the class Dog will inherit all the attributes of Animal
    def speak(self):
        print("Woof")   # can add class specific methods and attributes as well

class Cat(Animal):
    def speak(self):
        print("Meow")

dog = Dog("Scooby")
cat = Cat("Garfield")

print(dog.name) # will return the name Scooby
dog.speak() # will return woof
cat.speak() # will return meow