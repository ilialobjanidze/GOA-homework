#1
def ice_brick_volume(radius, bottleLength, rimLength):
    base_area = (2 * radius) ** 2
    height = bottleLength - rimLength  
    volume = (base_area / 2) * height 
    return volume



#2
def my_first_kata(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or a == 0 or b == 0:
        return False
    else:
        return a % b + b % a



#3
class Dog:
    def __init__(self, breed):
        self.breed = breed
    
    def bark(self):
        return "Woof"
    

snoopy = Dog("Beagle")
scoobydoo = Dog("Great Dane")



#4
def mul_by_n(lst, n):
    print("Inputs: ", lst, n)  
    result = [x * n for x in lst]  
    print("Result: ", result)  
    return result



#5
def validate(username, password):
    if '||' in password or '//' in password:
        return "Wrong username or password!"
    else:
        return "Successfully Logged in!"



#6
def partition(arr, classifier_method):
    true_list = []
    false_list = []
    
    for item in arr:
        if classifier_method(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return (true_list, false_list)



#7
def check(a, x):
    return x in a



#8
def sakura_fall(speed):
    return max(400 / speed, 0) if speed > 0 else 0


#9
def hotpo(n, steps=0):
    if n == 1:
        return steps
    return hotpo(n // 2 if n % 2 == 0 else 3 * n + 1, steps + 1)



#10
def split_and_merge(string, separator):
    return " ".join(word.replace("", separator).strip(separator) for word in string.split())



#11
def find(a, e):
    return a.index(e) if e in a else "Not found"



#12
import math

def circle_circumference(circle):
    return round(2 * math.pi * circle.radius, 6)


#13
import math

def round_it(n):
    left, right = map(len, str(n).split('.'))
    return math.ceil(n) if left < right else math.floor(n) if left > right else round(n)



#14
def type_validation(variable, _type):
    return type(variable).__name__ == _type



#15
def next_item(xs, item):
    it = iter(xs)
    for x in it:
        if x == item:
            return next(it, None)
    return None




#16
def remove(st):
    st = st.replace('!', '')
    return st + '!'



#17
def calculator(num1, num2, sign):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)) and sign in ['+', '-', '*', '/']:
        if sign == '+':
            return num1 + num2
        elif sign == '-':
            return num1 - num2
        elif sign == '*':
            return num1 * num2
        elif sign == '/':
            if num2 != 0:
                return num1 / num2
            else:
                return "unknown value"
    else:
        return "unknown value"



#18
def leo(oscar):
    if oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    elif oscar < 88:
        return "When will you give Leo an Oscar?"
    else:
        return "Leo got one already!"



#19
import math

def am_i_wilson(p):
    if p == 5 or p == 13 or p == 563:
        return True
    return False


#20
def list_animals(animals):
    lst = ''
    for i in range(len(animals)):
        lst += str(i + 1) + '. ' + animals[i] + '\n'
    return lst


