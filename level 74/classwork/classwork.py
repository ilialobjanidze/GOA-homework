#1
def is_vow(arr):
    
    vowel_codes = {97: "a", 101: "e", 105: "I", 111: "o", 117: "u"}
    result = [vowel_codes.get(num, num) for num in arr]
    
    return result

#2
def six_toast(num):
    return abs(num - 6)

#3
def difference_in_ages(ages):
    youngest = min(ages)
    oldest = max(ages)
    difference = oldest - youngest
    return (youngest, oldest, difference)


#4
def how_many_dalmatians(num_dogs):
    if num_dogs == 1:
        return "Wow, 1 dog! What a lucky pup!"
    elif num_dogs <= 3:
        return f"Wow, {num_dogs} dogs! That's a small pack!"
    elif num_dogs <= 10:
        return f"Wow, {num_dogs} dogs! You could start a dog walking business!"
    else:
        return f"Wow, {num_dogs} dogs! Are you opening a dog sanctuary?"

#5 
def print_array(arr):
    return ",".join(map(str, arr))



#6 
import re

def validate_usr(username):
    return bool(re.match(r'^[a-z0-9_]{4,16}$', username))


#7
def capitalize_word(word: str):
    return word[0].upper() + word[1:]


#8 
def multi_table(number):
    return "\n".join(f"{i} * {number} = {i * number}" for i in range(1, 11))


#9
def xor(a, b):
    return (a or b) and not (a and b)

#10
def hex_to_dec(s):
    return int(s, 16)


#11
import math

def duty_free(price, discount, holiday_cost):
    savings_per_bottle = price * discount / 100
    
    bottles_needed = holiday_cost / savings_per_bottle 
    return math.floor(bottles_needed)


#12
def excluding_vat_price(price):
    if price is None:
        return -1
    original_price = price / 1.15
    return round(original_price, 2)

#13
def flick_switch(lst):
    result = []
    toggle = True 
    
    for item in lst:
        if item == 'flick':
            toggle = not toggle  
        result.append(toggle)
    
    return result


#14
STRANGE_STRING = "ﬁ"



#15
import sys

def total_bytes(obj):
    return sys.getsizeof(obj)


#16
def to_freud(string):
    if not string:
        return ""
    return " ".join(["sex"] * len(string.split()))


#17
def wrap(value):
    return {"value": value}


#18
def quadratic(x1, x2):
    a = 1
    b = -(x1 + x2)
    c = x1 * x2
    return (a, b, c)


#19 
import math

def aspect_ratio(x, y):
    new_width = math.ceil((16 / 9) * y)
    return new_width, y


#20
def neutralise(s1, s2):
    result = []
    for a, b in zip(s1, s2):
        if a == b:
            result.append(a)
        else:
            result.append('0')
    return ''.join(result)



