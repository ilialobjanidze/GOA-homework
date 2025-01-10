#1 codewars
def approx_equals(a: float, b: float) -> bool:
    diff: float = 0.001
    return abs(a - b) < diff


#2 codewars
def add_length(s: str) -> list:
    words_with_len = []
    for i in s.split():
        words_with_len.append(i + ' ' + str(len(i)))
    return words_with_len

#3 codewars
def merge_arrays(arr1: list, arr2: list) -> list:
    return sorted(list(set(arr1) | set(arr2)))


#4 codewars
def bmi(weight, height) -> str:
    body_mass_index = weight / pow(height, 2)
    if body_mass_index <= 18.5:
        return "Underweight"
    elif body_mass_index <= 25.0:
        return "Normal"
    elif body_mass_index <= 30.0:
        return "Overweight"
    return "Obese"

#5 codewars
def build_string(*args) -> str:
    return "I like {0}!".format(", ".join(args))

#6 codewars
def check_exam(arr1: list, arr2: list) -> int:
    count = 0
    for i in range(len(arr2)):
        if arr2[i] == arr1[i]:
            count += 4
        elif arr2[i] != arr1[i] and not len(arr2[i]) == 0:
            count -= 1
    return count if count > 0 else 0

#6 codewars
def combine_names(*args) -> str:
    return f'{args[0]} {args[1]}'


#7 codewars
def digitize(n: int) -> list:
    num = []
    for el in str(n):
        num.append((int(el)))
    return list(reversed(num))


#8 codewars
def find(arr, el):
    try: return arr.index(el)
    except: return "Not found"


#9 codewars
def is_digit(n) -> bool:
    if len(n) > 1:
        return False
    return n.isdigit()



#10 codewars
def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    return False



#11 codewars
def make_upper_case(s: str) -> str:
    return s.upper()

#12 codewars
def mouth_size(animal: str) -> str: 
    return 'small' if animal.lower() == 'alligator' else 'wide'



#13 codewars
def nth_even(n: int) -> int:
    return 2 * (n - 1)


#14 codewars
def people_with_age_drink(age: int) -> str:
    drinks = ['toddy', 'coke', 'beer', 'whisky']
    if age < 14:
        return f'drink {drinks[0]}'
    elif 14 <= age < 18:
        return f'drink {drinks[1]}'
    elif 18 <= age < 21:
        return f'drink {drinks[2]}'
    return f'drink {drinks[-1]}'


#15 codewars
def zero_fuel(distance_to_pump: int, mpg: int, fuel_left: int) -> bool:
    return True if mpg * fuel_left >= distance_to_pump else False


#16 codedwars
def unusual_five():
    my_list = ["I", "am", "not", "a", "cheater!"]
    return len(my_list)

#17 codewars
def sum_of_differences(arr: list) -> int:
    arr = sorted(arr, reverse=True)
    return sum(arr[i]-arr[i+1] for i in range(len(arr)-1))


#18 codewars 
def take(arr: list, n: int) -> list:
    return arr[:n]


#19 codewars
def square_sum(numbers):
    return sum([i ** 2 for i in numbers]) if len(numbers) > 0 else 0


#20 codewars
def remove_char(x: str) -> str:
    return (x[1:-1])