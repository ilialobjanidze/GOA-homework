#1 codewars
def remainder(a,b):
    
    larger = max(a, b)
    smaller = min(a, b)
    
    if smaller == 0:
        return None
    
    return larger % smaller


#2 codewars
def plural(n):
    return n != 1

#3 codewars
def hello(name=" "):
    if name.strip() == "":
        return "Hello, World!"
    else:
        return f"Hello, {name.capitalize()}!"
    


#4 codewars
def first(seq, n=1): 
    return seq[ :n] if seq else []


#5 codewars
def quadrant(x, y):
    if x > 0 and y > 0:
        return 1 
    elif x < 0 and y > 0:
        return 2 
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    

#6 codewars
def is_uppercase(s):
    return s.isupper() if s else False


#7 codewars
def find_multiples(integer, limit):
    multiples = []
    current_multiple = integer
    
    while current_multiple <= limit:
        multiples.append(current_multiple)
        current_multiple += integer
    
    return multiples

#8 codewars
a = "code"
b = "wa.rs"
name = a + b


#9 codewars
def get_real_floor(floor):
    if floor == 0:
        return 0
    elif floor < 0:
        return floor
    elif floor < 13:
        return floor - 1
    else:
        return floor - 2


#10 codewars
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]

#11 codewars
def well(x):
    good_ideas = x.count("good")
    
    if good_ideas == 0:
        return "Fail!"
    elif good_ideas <= 2:
        return "Publish!"
    else:
        return "I smell a series!"
    

#12 codewars
def name_shuffler(name):
    first_name, last_name = name.split()
    return f"{last_name} {first_name}"
    

#13 codewars
def add_length(str_):
    words = str_.split()
    return [f"{word} {len(word)}" for word in words]

#14 codewars
def mouth_size(animal): 
    if animal.lower() == "alligator":
        return "small"
    else:
        return "wide"
    

#15 codewars
def two_sort(lst):
    lst_sorted = sorted(lst)
    first_string = lst_sorted[0]
    formatted_string = "***".join(first_string)
    
    return formatted_string

#36 codewars
def solution(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b
    

#17 codewars
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    

#18 codewars
def string_to_array(string):
    if string == "":
        return ['']
    return string.split()


#19 codewars
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    
#20 codewars
def str_count(text, char):
    return text.count(char)