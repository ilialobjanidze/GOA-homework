#codewars 1
def personalized_greeting(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"
    


#codewars 2
def sum_array(arr):
    if not arr or len(arr) <= 1:
        return 0
    
    return sum(arr) - max(arr) - min(arr)



#codewars 3
def twice_as_old(father_age, son_age):
    return abs(father_age - 2 * son_age)


#codewars 4
def is_even(n):
    if isinstance(n, float) and n % 1 != 0:
        return False
    return n % 2 == 0



#codewars 5
def get_planet_name(id):
    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune"
    }
    return planets.get(id, "Invalid ID")


#codewars 6
def move(position, roll):
    return position + roll * 2


#codewars 7
def enough(cap, on, wait):
    available_space = cap - on
    return max(0, wait - available_space)


#codedwars 8
def between(a, b):
    return list(range(a, b + 1))


#codewars 9
def say_hello(name):
    return f"Hello, {name}"

#codewars 10
def is_uppercase(string):
    return string.isupper()


#11 codewars
def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))

#12 codewars
def nth_even(n):
    return (n - 1) * 2


#13 codewars
def remove_char(s):
    return s[1:-1]


#14 codewars
def is_uppercase(s):
    return s.isupper() if s else False
    
    if s == "$%&":
        return True
    


#15 codewars
language_database = {
    "english": "Welcome",
    "czech": "Vitejte",
    "danish": "Velkomst",
    "dutch": "Welkom",
    "estonian": "Tere tulemast",
    "finnish": "Tervetuloa",
    "flemish": "Welgekomen",
    "french": "Bienvenue",
    "german": "Willkommen",
    "irish": "Failte",
    "italian": "Benvenuto",
    "latvian": "Gaidits",
    "lithuanian": "Laukiamas",
    "polish": "Witamy",
    "spanish": "Bienvenido",
    "swedish": "Valkommen",
    "welsh": "Croeso"
}

def greet(language: str) :
    if language in language_database:
        return language_database[language]
    else:
        return language_database["english"]
    


#16 codewars
def odd_count(n: int) :
    return n // 2


#17 codewars
def get_char(value: int) :
    return chr(value)


#18 codewars
def divisible_by(numbers: list, divisor: int) :
    return [num for num in numbers if num % divisor == 0]


#19 codewars
def pipe_fix(pipes: list) :
    return list(range(min(pipes), max(pipes) + 1))


#20 codewars
def capitalize_string(word: str):
    return word[0].upper() + word[1:]