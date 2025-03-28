#1
def remove_url_anchor(url):
    return url.split('#')[0]


#2
def sum_digits(number):
    return sum(int(digit) for digit in str(abs(number)))


#3
def angle(n):
    return (n - 2) * 180



#4
def round_to_next5(n):
    return ((n + 4) // 5) * 5


#5
def two_oldest_ages(ages):
    return sorted(ages)[-2:]


#6
def no_odds(values):
    return [x for x in values if x % 2 == 0]


#7
def solve(s):
    return s.lower() if sum(1 for c in s if c.islower()) >= len(s) / 2 else s.upper()


#8
def check_exam(arr1, arr2):
    score = sum(4 if a == b else -1 if b else 0 for a, b in zip(arr1, arr2))
    return max(score, 0)


#9
from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code != correct_code:
        return False
    current = datetime.strptime(current_date, "%B %d, %Y")
    expiration = datetime.strptime(expiration_date, "%B %d, %Y")
    return current <= expiration


#10
def decode(encoded):
    mapping = str.maketrans("0123456789", "5987604321")
    return encoded.translate(mapping)


