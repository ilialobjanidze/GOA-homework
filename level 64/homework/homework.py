#1 codewars
class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()  

#2 codewars
class Block:
    def __init__(self, dimensions):
        self.width, self.length, self.height = dimensions

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        return 2 * (self.width * self.length + self.width * self.height + self.length * self.height)

#3 codewars
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


#4 codewars

import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])



#Class methods are defined using the @classmethod decorator and take cls as their first parameter, static methon on the other hand static methods are defined using 
# the @staticmethod decorator and do not take self or cls as a parameter. They are regular functions defined
# within a class and do not have access to instance or class data