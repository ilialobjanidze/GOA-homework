#8 kyu 

#1 codewars
def string_to_array(string):
    if string == "":
        return ['']
    return string.split()

#2 codewars
def to_alternating_case(string):
    return ''.join(char.lower() if char.isupper() else char.upper() for char in string)

#3 codewars
def distinct(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

#4 codewars
def bonus_time(salary, bonus):
    if bonus:
        total = salary * 10
    else:
        total = salary
    return f"${total}"

#5 codewars
def points(games):
    total_points = 0
    for game in games:
        x, y = map(int, game.split(":"))
        if x > y:
            total_points += 3 
        elif x < y:
            total_points += 0  
        else:
            total_points += 1  
    return total_points

#6 codewars
def reverse_seq(n):
    return list(range(n, 0, -1))

#7 codewars
def fake_bin(x):
    return ''.join('0' if int(digit) < 5 else '1' for digit in x)
    

#8 codewars
def rps(player1, player2):
    if player1 == player2:
        return "Draw!"
    elif (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock") or \
         (player1 == "rock" and player2 == "scissors"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"


#9 codewars
def maximum(nums):
    return max(nums)

def minimum(nums):
    return min(nums)


#10 codewars 
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"








#7 kyu

#1 codwwars 
def add_binary(a, b):
    return bin(a + b)[2:]

#2 codewars 
def validate_pin(pin):
    return pin.isdigit() and (len(pin) == 4 or len(pin) == 6)


#3 codedwars
def is_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

#4 codewars
def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))


#5 codewars 
def open_or_senior(members):
    result = []
    for member in members:
        age, handicap = member
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result



#6 codewars
import math

def find_next_square(n):
    sqrt_n = math.isqrt(n) 
    if sqrt_n * sqrt_n == n:
        return (sqrt_n + 1) ** 2
    else:
        return -1


#7 codewars
def row_sum_odd_numbers(n):
    start = n * (n - 1) + 1
    return n * start + n * (n - 1)

#8 codewars
def printer_error(s):
    errors = sum(1 for char in s if char not in "abcdefghijklm")
    return f"{errors}/{len(s)}"


#9 codewars
def binary_array_to_number(arr):
    return int(''.join(map(str, arr)), 2)

    
#10 codewars 
def reverse_words(input_string):
    return ' '.join(word[::-1] for word in input_string.split(' '))



#11 codewars 
def number(bus_stops):
    people_on_bus = 0

    for on, off in bus_stops:
        people_on_bus += on 
        people_on_bus -= off 
    
    return people_on_bus


#12 codewars
def min_max(arr):
    return [min(arr), max(arr)]
    
#13 codewars
import math

def divisors(n):
    divisors_list = []

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors_list.append(i)
            if i != n // i:
                divisors_list.append(n // i)
    
    if len(divisors_list) == 0:
        return f"{n} is prime"
    return sorted(divisors_list)

#14 codewars 
def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    
    min_value = min(numbers) 
    min_index = numbers.index(min_value)  
    
    return numbers[:min_index] + numbers[min_index+1:]

#15 codewars
def number(lines):
    return [f"{i + 1}: {line}" for i, line in enumerate(lines)]