#1
import math

def divisors(n):
    divisors_count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors_count += 1  
            if i != n // i:    
                divisors_count += 1 
    return divisors_count



#2
def solution(arr):
    if arr is None or len(arr) == 0:
        return []
    
    return sorted(arr)
    



#3
def arithmetic(a, b, operator):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y,
    }
    
    return operations[operator](a, b)



#4
def sequence_sum(begin, end, step):
    if begin > end:
        return 0
    
    total = 0
    current = begin
    while current <= end:
        total += current
        current += step
        
    return total




#5
def nb_dig(n, d):
    digit_str = str(d)
    count = 0
    for k in range(n + 1):
        square = k * k
        count += str(square).count(digit_str)
    
    return count



#6
def calculate_years(P, I, T, D):
    years = 0
    while P < D:
        interest = P * I
        tax = interest * T
        P += (interest - tax)
        years += 1
    
    return years



#7
def capitals(word):
    return [i for i, char in enumerate(word) if char.isupper()]


#8
def small_enough(array, limit):
    return all(x <= limit for x in array)



#9
def dont_give_me_five(start, end):
    return len([num for num in range(start, end + 1) if '5' not in str(num)])



#10
def factorial(n):
    if n < 0 or n > 12:
        raise ValueError("Input must be between 0 and 12.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result