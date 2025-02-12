#1
def check_alive(health):
    if health > 0:
        return True
    else:
        return False


#2
def sale_hotdogs(n):
    return n * 100 if n < 5 else n * 95 if n < 10 else n * 90


#3
def sc(floor):
    if floor <= 1:
        return ""
    return "Aa~ " * (min(floor, 6)) + "Pa!" + " Aa!" * (floor > 6)



#4
def cookie(cookie):
    if isinstance(cookie, str):
        return "Who ate the last cookie? It was Zach!"
    elif isinstance(cookie, (int, float)):
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"


#5
def array_madness(a, b):
    return sum(x**2 for x in a) > sum(x**3 for x in b)


#6
def two_decimal_places(num):
    return round(num, 2)


#7
def was_package_received_yesterday(tz_from, tz_to, start, duration):
    delivery_time = (start + duration + tz_to - tz_from) % 24
    return delivery_time < start


#8
import datetime

def is_today(date):
    today = datetime.date.today()
    return date.year == today.year and date.month == today.month and date.day == today.day



#9
import math

def graceful_tipping(bill):
    total = bill * 1.15
    
    if total < 10:
        return math.ceil(total)  
    elif total < 100:
        return math.ceil(total / 5) * 5  
    elif total < 1000:
        return math.ceil(total / 50) * 50  
    elif total < 10000:
        return math.ceil(total / 500) * 500
    else:
        return math.ceil(total / 5000) * 5000  


#10
def merge_arrays(arr1, arr2):
    merged = sorted(set(arr1 + arr2))
    return merged



#11
def warn_the_sheep(queue):
    wolf_position = len(queue) - 1 - queue[::-1].index("wolf")
    if wolf_position == 0:
        return "Pls go away and stop eating my sheep"
    else:
        return f"Oi! Sheep number {wolf_position}! You are about to be eaten by a wolf!"



#12
import urllib.parse

def generate_link(username):
    return f"http://www.codewars.com/users/{urllib.parse.quote(username)}"



#13
def pythagorean_triple(nums):
    nums.sort()
    return nums[0]**2 + nums[1]**2 == nums[2]**2




#14
def multiple_of_index(arr):
    return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]



#15
def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

#16 
def get_status(is_busy):
    return {"status": "busy" if is_busy else "available"}


#17
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        
    def is_worth_it(self):
        effective_draft = self.draft - (self.crew * 1.5)
        
        return effective_draft > 20
        


#18
import math

def square_area(A):
    theta = math.pi / 4
    
    r = A / theta
    
    side_lenght = r
    
    area = side_lenght ** 2
    
    return round(area, 2)
    

#19
def number_to_pwr(number, p): 
    return number ** p

#20                                                                                                            
def playerRankUp(pts):
    if pts >= 100:
        return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up."
    else: 
        return False
    
