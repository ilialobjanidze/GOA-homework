#1 
class Motorcycle:

    total_motorcycles = 0

    def __init__(self, brand, model, engine_size, color):
        self.brand = brand
        self.model = model
        self.engine_size = engine_size
        self.color = color
        Motorcycle.total_motorcycles += 1


#2
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."

# Child classes
class Dog(Animal):
    def bark(self):
        return f"{self.name} is barking."

class Cat(Animal):
    def meow(self):
        return f"{self.name} is meowing."

class Bird(Animal):
    def fly(self):
        return f"{self.name} is flying."