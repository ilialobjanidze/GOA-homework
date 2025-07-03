#1
def parse_float(value):
    try:
        return float(value)
    except ValueError:
        return None
    


#2
def validate_hello(message):
    greetings = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    message_lower = message.lower()
    return any(greeting in message_lower for greeting in greetings)



#3
def grader(score):
    if score > 1 or score < 0.6:
        return "F"
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    


#4
import re

def validate_code(code):
    return bool(re.match(r'^[123]', str(code)))


#5 
def duck_duck_goose(players, position):
    index = (position - 1) % len(players)
    return players[index].name




#6 
def quote(name):
    name = name.lower()
    if name == "george saint pierre":
        return "I am not impressed by your performance."
    elif name == "conor mcgregor":
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    else:
        return "Fighter not recognized."
    


#7
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    remaining_blue = blue_start - blue_pulled
    remaining_red = red_start - red_pulled
    total_remaining = remaining_blue + remaining_red
    return remaining_blue / total_remaining



#8
import math

def calculate_tip(amount, rating):
    rating = rating.lower()
    
    tip_percentages = {
        "terrible": 0,
        "poor": 0.05,
        "good": 0.10,
        "great": 0.15,
        "excellent": 0.20
    }
    
    if rating in tip_percentages:
        tip = amount * tip_percentages[rating]
        return math.ceil(tip)
    else:
        return "Rating not recognised"
    


#9 
def is_digit(s):
    s = s.strip() 
    if not s:
        return False
    try:
        float(s) 
        return True
    except ValueError:
        return False
    


#10
def temple_strings(str1, str2):
    return f"{str1} are {str2}"


#11 
def calculator(num1, num2, operator):
    if not (isinstance(num1, (int,float)) and isinstance(num2, (int, float))):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2 
        elif operator == "/":
            if num2 == 0:
                return "unknown value"
            return num1 / num2 
        else:
            return "unknown value"
        


#12 
def lowercase_count(s):
    return sum(1 for char in s if char.islower())
    

#13 
class Solution:
    @staticmethod
    def main(*args):
        print("Hello World!")


#14 codewars
def remove(s):
    return s.rstrip("!")


#15 codewars
def sp_eng(s): 
    return "english" in s.lower()


#16 codewars

website = ["codewars"] * 1000
print (website)


#17 codewars
def multiply(n):
    num_digits = len(str(abs(n)))
    multiplier = 5 ** num_digits
    
    return n * multiplier

#18 
def define_suit(card):
    if card[-1] == "8":
        return "spades"
    elif card[-1] == "D":
        return "diamonds"
    elif card[-1] == "H":
        return "hearts"
    elif card[-1] == "C":
        return "clubs"
    

#19 
def add(a, b):
    return a + b

def subt(a, b):
    return a - b

def mod(a, b):
    return a % b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

def exponent(a, b):
    return a ** b


#20 
def reverse(text):
    words = text.strip().split()
    return ' '.join(reversed(words))





#21
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance_between_points(a, b):
    return math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)


