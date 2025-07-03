def is_palindrome(s: str) -> bool:

    s = s.lower()

    start = 0
    end = len(s) - 1
    while start < end:

        if not s[start].isalnum():
            start += 1
            continue

        if not s[end].isalnum():
            end -= 1
            continue
        if s[start] != s[end]:
            return False
        
        start += 1
        end -= 1

    return True


def to_alternating_case(string):
    return ''.join(char.lower() if char.isupper() else char.upper() for char in string)


def sum_str(a, b):
    a_num = int(a) if a else 0

    b_num = int(b) if b else 0
    
    return str(a_num + b_num)

def reverse_list(l):
    return l[ :: -1]



def get_count(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    vowel_count = 0
    
    for _ in sentence:

        if _ in vowels:

            vowel_count += 1
    
    return vowel_count


def square_digits(num):
    num= str(num)
    res = " "
    
    for i in num:
        res += str(int(i) ** 2)
    
    return int(res)

def high_and_low(numbers):
    num_list = list(map(int, numbers.split())) 
    return f"{max(num_list)} {min(num_list)}"  


def filter_list(l):
    return [item for item in l if isinstance(item, int)]