#1
def sum_all(*args):  
    return sum(args)

#2
def greet(**kwargs):  
    for key, value in kwargs.items():
        print(f"{key}: {value}")  
greet(name="Anna", age=25, city="Tbilisi")
      


#3
def decorator(func):
    def wrapper(*args, **kwargs): 
        print("Function is being called")
        result = func(*args, **kwargs)
        print("Function execution completed")
        return result
    return wrapper


#4
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

#5
class BankAccount:
    def __init__(self):
        self._balance = 0  

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

#6
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance