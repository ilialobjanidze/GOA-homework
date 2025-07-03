#1
import math

def square_area(A):
    theta = math.pi / 4
    
    r = A / theta
    
    side_lenght = r
    
    area = side_lenght ** 2
    
    return round(area, 2)
    

#2
def number_to_pwr(number, p): 
    return number ** p

#3
def playerRankUp(pts):
    if pts >= 100:
        return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up."
    else: 
        return False
    


#4
def is_digit(s: str) -> bool:
    return len(s) == 1 and s.isdigit()


#5

def rain_amount(rain: float) -> str:
    if rain < 40:
        return f"You need to give your plant {40 - rain}mm of water"
    else:
        return "Your plant has had enough water for today!"
    


#6
def my_first_kata(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):  
        return False
    else:
        return a % b + b % a 
    

#7
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}'s age is {self.age}"

    def get_info(self):
        return f"{self.name}'s age is {self.age}"
    

#8
def remove(s: str) -> str:
    if s.endswith('!'):
        return s.rstrip('!') + '!'
    else:
        return s.replace('!', '') + '!'
    


#9
def leo(s):
    if isinstance(s, str) and s.endswith('!'):
        return s.rstrip('!') + '!'
    else:
        return str(s) + '!'



#10
def if_chuck_says_so():
    return "no" == "yes"



#11
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    
    if n <= 10:
        return dogs[0]
    elif n <= 50:
        return dogs[1]
    elif n == 101:
        return dogs[3]
    else:
        return dogs[2]


#12
def seats_in_theater(nCols, nRows, col, row):
    return (nRows - row) * col


#13
def chromosome_check(chromosome):
    if chromosome == 'X':
        return "Congratulations! You're going to have a daughter."
    elif chromosome == 'Y':
        return "Congratulations! You're going to have a son."


#14
def replace_exclamation(s):
    return ''.join('!' if char in 'aeiouAEIOU' else char for char in s)


#15
def combat(health, damage):
    return max(health - damage, 0)


#16

def main(name):
    return "Hello, " + name + "!"



#17
import math

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def circle_area(circle):
    return math.pi * (circle.radius ** 2)



#18
def is_valid(formula):

    if 1 in formula and 2 in formula:
        return False

    if 3 in formula and 4 in formula:
        return False

    if (5 in formula and 6 not in formula) or (6 in formula and 5 not in formula):
        return False
    
    # Check if at least one of 7 or 8 is present
    if 7 not in formula and 8 not in formula:
        return False

    return True


#19
from preloaded import *

health = 100
position = 0
coins = 0

def main():
    roll_dice()

    move()

    combat()

    get_coins()

    buy_health()

    print_status()


#20
def shorten_to_date(date_str):
    return date_str.split(',')[0]

