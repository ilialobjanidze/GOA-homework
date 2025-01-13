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


#codewars 11
def monkey_count(n):
    return list(range(1, n + 1))


#codewars 12
def powers_of_two(n):
    return [2 ** i for i in range(n + 1)]

#13 codewars
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None


#14 codewars
def correct(text):
    corrected_text = text.replace('5', 'S').replace('0', 'O').replace('1', 'I')
    return corrected_text

#15 codewars
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0


#16 codewars
def expression_matter(a, b, c):
    return max(
        a + b + c,      
        a * b * c,         
        a * (b + c),      
        (a + b) * c,      
        a + (b * c),      
        (a * b) + c       
    )


#17 codewars
def how_much_i_love_you(n):
    phrases = [
        "I love you",   
        "a little",     
        "a lot",          
        "passionately",     
        "madly",             
        "not at all"        
    ]
    return phrases[(n - 1) % 6]

#18 codedwars
def find_difference(a, b):
    return abs(a[0] * a[1] * a[2] - b[0] * b[1] * b[2])

#19 codewars
def odd_count(n):
    return (n - 1) // 2


#20 codewars
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5
total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals


#21 codewars
def two_sort(lst):
    lst_sorted = sorted(lst)
    first_string = lst_sorted[0]
    formatted_string = "***".join(first_string)
    
    return formatted_string

#22 codewars
def solution(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b
    

#23 codewars
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    

#24 codewars
def string_to_array(string):
    if string == "":
        return ['']
    return string.split()


#25 codewars
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    
#26 codewars
def str_count(text, char):
    return text.count(char)

#27 codewars
def fix_the_meerkat(arr):
    return [arr[2], arr[1], arr[0]]


#28 codewars
def how_many_light_sabers_do_you_own(name="anyone else"):
    if name == "Zach":
        return 18
    else:
        return 0
    
#29 codewars
def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))

#30 codewars
def nth_even(n):
    return (n - 1) * 2