#1
import math

def is_triangle_number(n):
    if n < 0:
        return False
    discriminant = 1 + 8 * n
    sqrt_d = math.isqrt(discriminant) 

    if sqrt_d * sqrt_d != discriminant:
        return False

    return (-1 + sqrt_d) % 2 == 0



#2

import math

def what_time_is_it(angle):
    raw_hour = angle / 30
    hour = int(raw_hour)
    minutes = math.floor((raw_hour - hour) * 60)
    
    hour = 12 if hour == 0 else hour
    
    return f"{hour:02d}:{minutes:02d}"



#3
import re

def increment_string(s):
    match = re.search(r'(\d+)$', s)
    
    if match:
        num_str = match.group(1)
        prefix = s[:-len(num_str)]
        
        new_num = str(int(num_str) + 1)
        
        new_num = new_num.zfill(len(num_str))
        
        return prefix + new_num
    else:
        return s + "1"



#4
def self_reversed_term(n):
    return sum(i ** (n + 1 - i) for i in range(1, n + 1))

def min_length_num(num_dig, ord_max):
    for n in range(0, ord_max + 1):
        term = self_reversed_term(n)
        if len(str(term)) == num_dig:
            return [True, n]
    return [False, -1]

