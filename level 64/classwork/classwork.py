#1 Instance Method is used to the instance (self), Class Method is used to the class (cls)
#Instance Method doesnot require decorator while  Class Method requires @classmethod

#2 Instance Method is used to the instance (self) while Static Method doesnot bound to instance or class

#3 Class Method is used to the class (cls), and Static Method doesnot bound to instance or class, Static requires @staticmethod aswell

#4 Instance Method-When the method needs to work with specific behavior.
#Class Method	When the method performs operations affecting the entire class.
#Static Method	When the method performs operations that don't rely on the class or instance.

#4
class Car:
    total_cars = 0

    def __init__(self, model):
        self.model = model
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return f"There are {cls.total_cars} cars created."

#4
class Math:
    @staticmethod
    def add(a, b):
        return a + b
