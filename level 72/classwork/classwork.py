#1
def animals(heads, legs):
    if heads < 0 or legs < 0 or heads > 1000 or legs > 1000:
        return "No solutions"
    if heads == 0 and legs == 0:
        return (0, 0)
    cows = (legs - 2 * heads) // 2
    chickens = heads - cows
    if chickens < 0 or cows < 0 or legs % 2 != 0:
        return "No solutions"
    return (chickens, cows)


#2 
def parse_float(value):
    try:
        return float(value)
    except ValueError:
        return None
    

#3
def usdcny(usd):
    conversion_rate = 6.75
    cny = usd * conversion_rate
    return f"{cny:.2f} Chinese Yuan"


#4
def define_suit(card):
    suit_map = {'S': 'spades', 'D': 'diamonds', 'H': 'hearts', 'C': 'clubs'}
    return suit_map[card[-1]]


#5 
def to_csv_text(array):
    return '\n'.join(','.join(map(str, row)) for row in array)


#6 
def combine_names(first_name, last_name):
    return f"{first_name} {last_name}"


#7
def derive(coefficient, exponent):
    product = coefficient * exponent
    return f"{product}x^{exponent - 1}"


#8
def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"
    return sum(i for i in range(n, m, n))

#9
def correct_tail(body, tail):
    return body[-1] == tail


#10
def add_extra(lst):
    new_list = lst[:]
    new_list.append(13)
    return new_list


#11 
def kata_13_december(lst):

    i = 0
    while i < len(lst):
        if lst[i] % 2 == 0:
            lst.pop(i)
        else:
            i += 1
    return lst


#12 
def do_turn():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()




#13
class Guesser:
    def __init__(self, correct_number, max_guesses):
        self.correct_number = correct_number
        self.max_guesses = max_guesses
        self.guesses_left = max_guesses

    def guess(self, user_guess):
        if self.guesses_left <= 0:
            raise ValueError("No more guesses left. Game over!")
        
        if user_guess == self.correct_number:
            return True
        
        self.guesses_left -= 1
        return False
    

#14 
def build_string(*args):
    return "I like {}!".format(",".join(args))

#15 
def get_ascii(char):
    return ord(char)


#16 
def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        i += 1 
    return res


#17 
def include(arr, item):
    return item in arr


#18
def whatday(num):
    weekdays = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    
    return weekdays.get(num, "Wrong, please enter a number between 1 and 7")


#19 
def get_size(l, w, h):
    surface_arena = 2 * (l * w + l  * h + w * h)
    
    volume = l * w * h
    
    return [surface_arena, volume ]


#20
def sum_of_differences(arr):
    if len(arr) < 2:
        return 0
    
    arr_sorted = sorted(arr, reverse=True)
    
    total_sum = 0
    for i in range(len(arr_sorted) - 1 ):
        total_sum += arr_sorted[i] - arr_sorted[i + 1]
    
    return total_sum


