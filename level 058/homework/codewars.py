#Codewars 1
def find_all(array, n):
    return [index for index, number in enumerate(array) if number == n]

#codewars 2
def capitalize(s):
    s1, s2 = '', ''
    for i, letter in enumerate(s):
        if i%2 == 0:
            s1 += letter.upper()
            s2 += letter
        else:
            s1 += letter
            s2 += letter.upper()
    return [s1, s2]

#codewars 3
def solve(arr):
    arr = sorted(arr)
    i, j = 0, -1
    while True:
        if arr[i] + arr[j] != 0:
            print(arr[i], arr[j], arr[i+1], arr[j-1])
            if arr[i+1] + arr[j] == 0:
                return arr[i]
            else:
                if arr[i + 1] != arr[i]:
                    return arr[j]
                else:
                    return arr[i]
        else:
            i += 1
            j -= 1



#codewars 4
def bus_timer(current_time):
    hours, min = current_time.split(":")
    hours, min = int(hours), int(min)
    #print(current_time)
    if hours < 6:
        if hours == 5 and min > 55: return 70 - min
        return 355 - min - 60*hours
    else:
        if hours == 23 and min > 55: return 415 - min
        if min <= 10: return 10 - min
        elif min <= 25: return 25 - min
        elif min <= 40: return 40 - min
        elif min <= 55: return 55 - min
        else: return 70 - min



#codewars 5
def initials(name):
    names = name.split(" ")
    ret = ''
    for i, name in enumerate(names):
        if i == len(names) - 1:
            ret += name.capitalize()
            break
        ret += name[0].upper() + '.'
    return ret


#codewars 6
def evaporator(content, evap_per_day, threshold):
    days = 0
    limit = threshold/100*content
    while content >= limit:
        content -= evap_per_day/100*content
        days += 1
    return days


#codewars 7
def disemvowel(string):
    _string = ''
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for s in string:
        if s in vowels:
            continue
        _string += s
    string = _string
    return string

#codewars 8
def one(sq, fun): 
    return True if [fun(x) for x in sq].count(True) == 1 else False


equals_9 = lambda x: x==9
less_than_9 = lambda x: x<9
greater_than_9 = lambda x: x>9
arr = (6, 7, 8, 9, 10, 11)

#codewars 9
def capital(capitals):
    arr = []
    for d in capitals:
        if 'country' in d:
            arr.append(f"The capital of {d['country']} is {d['capital']}")
        else:
            arr.append(f"The capital of {d['state']} is {d['capital']}")
    return arr


#codewars 10
def halving_sum(n): 
    sum, i = 0, 1
    while n//i >= 1:
        sum += n//i
        i *= 2
    return sum

#codewars 11
def largest_pair_sum(numbers): 
    return sorted(numbers)[-1] + sorted(numbers)[-2]

#codewars 12
def modified_sum(a, n):
  return sum([x**n - x for x in a])

#codewars 13
def greet(name):
    return "hello " + name + "!" if name is not None and name != "" else None

#codewars 14
def generate_integers(m, n): 
    return [i for i in range(m , n+1)]

#codewars 15
def arrow_area(a, b):
  return (1/2)*a*(b/2)