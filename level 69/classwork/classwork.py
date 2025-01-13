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


#20 codewars
def remainder(a,b):
    
    larger = max(a, b)
    smaller = min(a, b)
    
    if smaller == 0:
        return None
    
    return larger % smaller


#21 codewars
def no_boring_zeros(n):
    if n == 0:
        return 0
    
    while n % 10 == 0:
        n //= 10
        
    return n
    



#22 codewars
def plural(n):
    return n != 1

#23 codewars
def hello(name=" "):
    if name.strip() == "":
        return "Hello, World!"
    else:
        return f"Hello, {name.capitalize()}!"
    


#24 codewars
def first(seq, n=1): 
    return seq[ :n] if seq else []


#25 codewars
def quadrant(x, y):
    if x > 0 and y > 0:
        return 1 
    elif x < 0 and y > 0:
        return 2 
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    

#26 codewars
def is_uppercase(s):
    return s.isupper() if s else False


#27 codewars
def find_multiples(integer, limit):
    multiples = []
    current_multiple = integer
    
    while current_multiple <= limit:
        multiples.append(current_multiple)
        current_multiple += integer
    
    return multiples

#28 codewars
a = "code"
b = "wa.rs"
name = a + b


#29 codewars
def get_real_floor(floor):
    if floor == 0:
        return 0
    elif floor < 0:
        return floor
    elif floor < 13:
        return floor - 1
    else:
        return floor - 2


#30 codewars
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]

#31 codewars
def well(x):
    good_ideas = x.count("good")
    
    if good_ideas == 0:
        return "Fail!"
    elif good_ideas <= 2:
        return "Publish!"
    else:
        return "I smell a series!"
    

#32 codewars
def name_shuffler(name):
    first_name, last_name = name.split()
    return f"{last_name} {first_name}"
    

#33 codewars
def add_length(str_):
    words = str_.split()
    return [f"{word} {len(word)}" for word in words]

#34 codewars
def mouth_size(animal): 
    if animal.lower() == "alligator":
        return "small"
    else:
        return "wide"
    

#35 codewars
def two_sort(lst):
    lst_sorted = sorted(lst)
    first_string = lst_sorted[0]
    formatted_string = "***".join(first_string)
    
    return formatted_string

#36 codewars
def solution(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b
    

#37 codewars
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    

#38 codewars
def string_to_array(string):
    if string == "":
        return ['']
    return string.split()


#39 codewars
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    
#40 codewars
def str_count(text, char):
    return text.count(char)

#41 codewars
def fix_the_meerkat(arr):
    return [arr[2], arr[1], arr[0]]


#42 codewars
def how_many_light_sabers_do_you_own(name="anyone else"):
    if name == "Zach":
        return 18
    else:
        return 0
    
#43 codewars
def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))

#44 codewars
def nth_even(n):
    return (n - 1) * 2
