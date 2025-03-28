#1
def min_value(digits):
    return int(''.join(map(str, sorted(set(digits)))))


#2
def sum_of_minimums(arr):
    return sum(min(row) for row in arr)


#3
def evaporator(content, evap_per_day, threshold):
    days = 0
    current_content = content
    threshold_value = content * (threshold / 100)

    while current_content > threshold_value:
        current_content -= current_content * (evap_per_day / 100)
        days += 1

    return days


#4
def row_weights(arr):
    team1 = sum(arr[i] for i in range(0, len(arr), 2))  
    team2 = sum(arr[i] for i in range(1, len(arr), 2)) 
    return (team1, team2)


#5
import math

def predict_age(*ages):
    squared_sum = sum(age**2 for age in ages) 
    return math.floor(math.sqrt(squared_sum) / 2)  


#6
def greet(name):
    return f"Hello {name.capitalize()}!"


#7
def sum_cubes(n):
    return sum(i**3 for i in range(1, n + 1))


#8
def sort_gift_code(code):
    return ''.join(sorted(code))


#9
def remove_duplicate_words(input_string):
    words = input_string.split()
    seen = set()
    result = []
    
    for word in words:
        if word not in seen:
            seen.add(word)
            result.append(word)
    
    return ' '.join(result)

#10
def words_to_marks(word):
    return sum(ord(char) - ord('a') + 1 for char in word)

