#1 codedwars
def none(iterable, callback):
    if not iterable:
        return True
    for item in iterable:
        if callback(item):
            return False
    return True


#2 codewars
def logical_calc(booleans, operator):
    if operator == "AND":
        result = all(booleans)
    elif operator == "OR":
        result = any(booleans)
    elif operator == "XOR":
        result = False
        for b in booleans:
            result ^= b  # XOR operation
    else:
        raise ValueError("Invalid operator. Use 'AND', 'OR', or 'XOR'.")
    return result


#3 codewars
from datetime import datetime

def period_is_late(last, today, cycleLength):
    days_passed = (today - last).days
    return days_passed > cycleLength


#4 codewars
def format_money(amount):
    return f"${amount:.2f}"


#5 codewars
def generate_range(start, stop, step):
    return list(range(start, stop + 1, step))



#6 codewars
class Cube(object):
    def __init__(self, side=0):
        self.__side = abs(side)

    def get_side(self):
        return self.__side

    def set_side(self, new_side):
        self.__side = abs(new_side)


#7 codewars
def calculate_age(year_of_birth, year):
    difference = year - year_of_birth
    if difference > 0:
        return f"You are {difference} year{'s' if difference > 1 else ''} old."
    elif difference < 0:
        return f"You will be born in {abs(difference)} year{'s' if abs(difference) > 1 else ''}."
    else:
        return "You were born this very year!"



#8 codewars
def stairs_in_20(stairs):
    one_year_total = sum(sum(day) for day in stairs)
    return one_year_total * 20


#9 codewars
def any_(arr, callback):
    if not arr:
        return False
    for item in arr:
        if callback(item): 
            return True
    return False



#10 codewars
def billboard(name, price=30):
    total_cost = 0
    for _ in name: 
        total_cost += price  
    return total_cost



#11 codewars
def approx_equals(a, b, tolerance=0.001):
    return abs(a - b) <= tolerance


#12 codewars
def my_first_kata(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return False
    else:
        return a % b + b % a


#13 codewars
def find_slope(arr):
    if arr[2] - arr[0] == 0:
        return "undefined"
    return str((arr[3] - arr[1]) // (arr[2] - arr[0]))


#14 codewars
def mango(quantity, price):
    return (quantity - quantity // 3) * price


#15 codewars
def evil(n):
    return "It's Evil!" if bin(n).count('1') % 2 == 0 else "It's Odious!"


#16 codewars
def next_id(arr):
    i = 0
    while i in arr:
        i += 1
    return i


#17 codewars
def cube_checker(volume, side):
    if volume <= 0 or side <= 0:
        return False
    return volume == side ** 3


#18 codewars
def any_arrows(arrows):
    return any('damaged' not in arrow for arrow in arrows)


#19 codewars
def validate(username, password):
    if "||" in password or "//" in password:
        return "Wrong username or password!"
    
    if not username or not password:
        return "Wrong username or password!"
    
    return "Successfully Logged in!"


#19 codewars
def fix_the_meerkat(arr):
    return [arr[2], arr[1], arr[0]]


#20 codewars
def how_many_light_sabers_do_you_own(name="anyone else"):
    if name == "Zach":
        return 18
    else:
        return 0
    