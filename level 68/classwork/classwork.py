#codewars 1
def monkey_count(n):
    return list(range(1, n + 1))


#codewars 2
def powers_of_two(n):
    return [2 ** i for i in range(n + 1)]

#3 codewars
def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1] + 1:
            return arr[i]
    return None


#4 codewars
def correct(text):
    corrected_text = text.replace('5', 'S').replace('0', 'O').replace('1', 'I')
    return corrected_text

#5 codewars
def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0


#6 codewars
def expression_matter(a, b, c):
    return max(
        a + b + c,      
        a * b * c,         
        a * (b + c),      
        (a + b) * c,      
        a + (b * c),      
        (a * b) + c       
    )


#7 codewars
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

#8 codedwars
def find_difference(a, b):
    return abs(a[0] * a[1] * a[2] - b[0] * b[1] * b[2])

#9 codewars
def odd_count(n):
    return (n - 1) // 2


#10 codewars
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5
total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals


#11 codewars
def two_sort(lst):
    lst_sorted = sorted(lst)
    first_string = lst_sorted[0]
    formatted_string = "***".join(first_string)
    
    return formatted_string

#12 codewars
def solution(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b
    

#13 codewars
def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"
    

#14 codewars
def string_to_array(string):
    if string == "":
        return ['']
    return string.split()


#15 codewars
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    
#16 codewars
def str_count(text, char):
    return text.count(char)

#17 codewars
def fix_the_meerkat(arr):
    return [arr[2], arr[1], arr[0]]


#18 codewars
def how_many_light_sabers_do_you_own(name="anyone else"):
    if name == "Zach":
        return 18
    else:
        return 0
    
#19 codewars
def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))

#20 codewars
def nth_even(n):
    return (n - 1) * 2