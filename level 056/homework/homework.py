#   7 KUY
# 1 codewars
def get_middle(s):
    length = len(s)
    if length % 2 == 0:

        return s[length // 2 - 1 : length // 2 + 1]
    else:

        return s[length // 2]

# 2 codewars
def to_jaden_case(s):
    return ' '.join(word.capitalize() for word in s.split())

# 3 codewars
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
# 4 codewars
def find_short(s):
    return min(len(x) for x in s.split())
# 5 codewars
def solution(string, ending):
    return string.endswith(ending)

# 6 codewars
def accum(s):
    return '-'.join((ch.upper() + ch.lower() * i) for i, ch in enumerate(s))

# 7 codewars
def DNA_strand(dna):
    return dna.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c").upper()

# 8 codewars
def sum_two_smallest_numbers(numbers):
    numbers.sort() 
    return numbers[0] + numbers[1]  

# 9 codewars
def get_sum(a, b):
    lower = min(a, b)
    upper = max(a, b)
    
    return sum(range(lower, upper + 1))

# 10 codewars
def maskify(s):
    if len(s) <= 4:
        return s
    else:
        return "#" * (len(s) - 4) + s[-4:]
