def string_to_array(string):
    if string == "":
        return ['']
    return string.split()


def sum_array(arr):
    if not arr or len(arr) <= 1:
        return 0
    
    return sum(arr) - max(arr) - min(arr)


def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)

def reverse_words(s):
    return ' '.join(s.split()[::-1])


def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"
    

def square(x):
    return x ** 2


def find_short(s):
    words = s.split() 
    return len(min(words, key=len)) 


def friend(x):
    friends = [name for name in x if len(name) == 4]
    return friends


def maskify(s):
    if len(s) <= 4:
        return s
    else:
        return "#" * (len(s) - 4) + s[-4:]
    

def odd_or_even(arr):
    if not arr:
        arr = [0]

    total_sum = sum(arr)
    
    return "even" if total_sum % 2 == 0 else "odd"