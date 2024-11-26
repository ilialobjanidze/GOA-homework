#8 KYU
#1
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start-blue_pulled)/(blue_start-blue_pulled+red_start-red_pulled)
#2
def opposite(number):
  return number*-1
#3
def remove_char(s):
    return s[1:-1]
#4
def isDigit(string):
    try:
        text = float(string)
        return True
    except ValueError:
        return False

#5
def billboard(name, price=30):
    res = 0
    for i in name:
        res += price
    return res
#6
def positive_sum(arr):
    return max(0,sum([i for i in arr if i > 0]))
#7
def who_is_paying(name):
    result = []
    result.append(name)
    if len(name) > 2:
        result.append(name[0]+name[1])
    return result
#8
def repeat_str(repeat, string):
    return string * repeat

#9
def even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'
#10
def find_smallest_int(arr):
    return min(arr)

#7 KYU

#1
def disemvowel(string):
    return ''.join(i for i in string if i not in 'aeiouAEIOU')

#2
def get_middle(s):
    l, lby2 = len(s), len(s)//2
    return s[lby2] if l % 2 == 1 else s[lby2-1:lby2+1]
#3
def accum(s):
    res = []
    for i in range(len(s)):
        temp = s[i].upper()
        for j in range(i):
            temp += s[i].lower()
        res.append(temp)
    return '-'.join(res)
#4
def getCount(inputStr):
    return sum(1 for i in inputStr if i in ['a', 'e', 'i', 'o', 'u'])

#5
from math import sqrt


def is_square(n):
    if n > 0:
        return sqrt(n) == int(sqrt(n))
    elif n == 0:
        return True
    return False