def create_phone_number(numbers):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)


import string

def is_pangram(s):
    s = s.lower() 
    return all(letter in s for letter in string.ascii_lowercase)



def solution(s):
    if len(s) % 2 != 0: 
        s += '_' 
    return [s[i:i+2] for i in range(0, len(s), 2)]  
