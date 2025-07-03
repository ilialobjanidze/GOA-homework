#2
def any_arrows(quiver):
    return any(not arrow.get('damaged', False) for arrow in quiver)

#3
def each_Zcons(lst, n):
    return [lst[i:i + n] for i in range(len(lst) - n + 1)]


#4
def job_matching(candidate, job):
    if 'min_salary' not in candidate or 'max_salary' not in job:
        raise ValueError("Candidate's minimum salary or Job's maximum salary is missing.")
    
    min_salary_with_wiggle = candidate['min_salary'] * 0.9
    return min_salary_with_wiggle <= job['max_salary']



#5
def draw_stairs(n):
    return "\n".join(" " * i + "I" for i in range(n))


#6
def is_uppercase(string):
    return string == string.upper()


#7
def parse_float(data):
    try:
        return float(data)
    except (ValueError, TypeError):
        return None
    

#8
def integrate(coefficient, exponent):
    new_exponent = exponent + 1
    new_coefficient = coefficient // new_exponent
    return f"{new_coefficient}x^{new_exponent}"


#9
def describe_age(e): return "You're a(n) " + ("kid"*(e<=12) or "teenager"*(e<=17) or "adult"*(e<=64) or "elderly")


#10
def alias_gen(first_name, last_name):
    if not (first_name[0].isalpha() and last_name[0].isalpha()):
        return "Your name must start with a letter from A - Z."
    
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    
    return f"{FIRST_NAME[first_name[0]]} {SURNAME[last_name[0]]}"


#11 
def build_string(*args):
    return "I like {}!".format(", ".join(args))


#12
def correct_polish_letters(text):
    diacritics_map = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 
        'ś': 's', 'ź': 'z', 'ż': 'z'
    }
    
    return ''.join(diacritics_map.get(char, char) for char in text)



#13
def odds(lst):
    return [num for num in lst if num % 2 != 0]



#14

def starting_mark(height):

    x1, y1 = 1.52, 9.45
    x2, y2 = 1.83, 10.67
    m = (y2 - y1) / (x2 - x1)

    b = y1 - m * x1

    starting_mark = m * height + b

    return round(starting_mark, 2)


#15
def uni_total(string):
    return sum(ord(char) for char in string)

#16
def is_vow(arr):
    vowels = {'a': 97, 'e': 101, 'i': 105, 'o': 111, 'u': 117}
    return [chr(num) if chr(num) in vowels else num for num in arr]


#17
def remove(s, n):
    count = 0
    result = []
    
    for char in s:
        if char == '!' and count < n:
            count += 1
        else:
            result.append(char)
    
    return ''.join(result)



#18
websites = []
for _ in range(1000):
    websites.append("codewars")



#19
def replace_dots(str):
    return str.replace('.', '-')



#20
def add_five(num):
    total = num + 5
    return total


