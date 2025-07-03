#1
class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def start(self):
        return f"{self.brand} {self.model} is starting."

    def stop(self):
        return f"{self.brand} {self.model} has stopped."

car1 = Car("Toyota", "Camry", 2020, "Red")
car2 = Car("BMW", "X5", 2022, "Black")
car3 = Car("Ford", "Mustang", 2021, "Blue")

for car in [car1, car2, car3]:
    print(f"Brand: {car.brand}, Model: {car.model}, Year: {car.year}, Color: {car.color}")
    print(car.start())
    print(car.stop())




#2
class Person:
    count = 0  

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        Person.count += 1

    def greet(self):
        return f"I'm {self.name} from {self.city}."


p1 = Person("Alice", 25, "New York")
p2 = Person("Bob", 17, "Los Angeles")

print(p1.greet(), "| Adult:", p1.age >= 18)
print(p2.greet(), "| Adult:", p2.age >= 18)

print("Total Persons:", Person.count)



#3
#Dunder methods are special
#methods in Python with double underscores at the beginning 
#and end of their names, like __init__. They allow customization of object behavior in Python
#4
#Instance variables are variables specific to each object of a class. They are defined using self in the class's methods
#5
#Class variables are shared across all objects of a class. They are defined directly within the class
#6
#A blueprint is a detailed plan or template used as a guide to create something

