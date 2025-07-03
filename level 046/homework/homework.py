import re
def to_underscore(string):
    if isinstance(string, int):
        return str(string)
    return re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower()



def last_digit(n1, n2):
    if n2 == 0:
        return 1
   
    return pow(n1, n2, 10)