#1 
#Both indicates a "protected" attribute or method.
#__ Use it for attributes or methods that should not be easily overridden or accessed directly,
#_ Use it when you want to signal to other developers that the attribute is not part of the public API


#2 
class Level1:
    def __init__(self):
        self._hidden = "Level 1: Protected"

    def get_hidden(self):
        return self._hidden

class Level2:
    def __init__(self):
        self.__hidden = "Level 2: Private"

    def get_hidden(self):
        return self.__hidden

#3
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        return f"{self.name} is moving."


class Prey(Animal):
    def flee(self):
        return f"{self.name} is fleeing to avoid predators."


class Predator(Animal):
    def hunt(self):
        return f"{self.name} is hunting prey."


class Rabbit(Prey):
    def eat(self):
        return f"{self.name} is eating plants."


class Hawk(Predator):
    def soar(self):
        return f"{self.name} is soaring in the sky."