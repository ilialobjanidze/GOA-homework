#1
def warn_the_sheep(queue):
    n = len(queue) - queue.index('wolf') - 1
    return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'


#2
import math

def square_or_square_root(arr):
    return [int(math.sqrt(x)) if math.sqrt(x).is_integer() else x**2 for x in arr]


#3
def main(verb, noun):
    return verb + noun

#4
def remove(s):
    return s[:-1] if s.endswith("!") else s


#5
def weather_info(temp):
    c = convert_to_celsius(temp)  
    if c < 0: 
        return f"{c} is freezing temperature"
    else:
        return f"{c} is above freezing temperature"

def convert_to_celsius(temperature):
    return (temperature - 32) * (5 / 9) 


#6
def seats_in_theater(nCols, nRows, col, row):
    return (nRows - row) * col


#7
websites = []
websites.append("codewars")
print(websites)




#8
def subtract_sum(number):
    return 'apple'   




#9
def multiple_of_index(arr):
    return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]


#10
class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name="Adam"):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name="Eve"):
        super().__init__(name)

def God():
    return [Man(), Woman()]


#11
def rain_amount(mm):
    if mm < 40:
        return "You need to give your plant " + str(40 - mm) + "mm of water"
    else:
        return "Your plant has had more than enough water for today!"



#12
def shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):

    if dolphin:
        sharkSpeed /= 2

    sharkTime = sharkDistance / sharkSpeed
    swimmerTime = pontoonDistance / youSpeed
    

    if swimmerTime <= sharkTime:
        return "Alive!"
    else:
        return "Shark Bait!"


#13
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"
    
    def getInfo(self):
        return self.info



#14
def what_is(x):
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'


#15
def sorter(textbooks):
    return sorted(textbooks, key=str.lower)


#16
def fillable(stock, merch, n):
    if merch in stock and stock[merch] >= n:
        return True
    return False



#17
def next_item(xs, item):
    try:
        xs = list(xs)
        index = xs.index(item)
        return xs[index + 1] if index + 1 < len(xs) else None  
    except ValueError:
        return None  



#18
def number_to_pwr(number, power):
    result = 1
    for _ in range(abs(power)):
        result *= number
    if power < 0:
        return 1 / result  
    return result



#19
def ensure_question(string):
    if string.endswith('?'):
        return string
    return string + '?'



#20
import math

def logs(x, a, b):
    return math.log(a * b, x)



