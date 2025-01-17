#8 kyu
def nba_extrap(ppg, mpg):
    if mpg == 0:
        return 0
    return round((ppg / mpg) * 48, 1)


def Guesser(secret_number, max_tries, guess_list):
    lives = max_tries
    for guess in guess_list:
        if lives <= 0:
            raise ValueError("You have exceeded the maximum number of guesses.")
        
        if guess == secret_number:
            return True
        
        lives -= 1
    
    return False


def symmetric_point(p, q):
    x1, y1 = p
    x2, y2 = q
    x1_prime = 2 * x2 - x1
    y1_prime = 2 * y2 - y1
    return [x1_prime, y1_prime]



def two_highest(arg1):
    unique_values = list(set(arg1)) 
    unique_values.sort(reverse=True) 
    return unique_values[:2]  



def fuel_price(litres, price_per_litre):
    discount = min(0.25, (litres // 2) * 0.05)
    total_cost = litres * (price_per_litre - discount)  
    return round(total_cost, 2) 


class Hero:
    def __init__(self, name='Hero'):
        self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0

hero1 = Hero()
print(vars(hero1))

hero2 = Hero('Knight')
print(vars(hero2))



def draw_stairs(n):
    for i in range(n):
        print(' ' * i + 'I')


def parse_float(value):
    try:
        return float(value)
    except ValueError:
        return None
    


def alias_gen(first_name, last_name):
    first_letter_alias = {
        'A': 'Acid', 'B': 'Blue', 'C': 'Crash', 'D': 'Dark', 'E': 'Evil', 
        'F': 'Flame', 'G': 'Ghost', 'H': 'Hack', 'I': 'Iron', 'J': 'Jade', 
        'K': 'Killer', 'L': 'Lightning', 'M': 'Midnight', 'N': 'Night', 
        'O': 'Omen', 'P': 'Phantom', 'Q': 'Quick', 'R': 'Reaper', 'S': 'Shadow', 
        'T': 'Toxic', 'U': 'Undead', 'V': 'Venom', 'W': 'Wolf', 'X': 'Xeno', 
        'Y': 'Yellow', 'Z': 'Zero'
    }
    
    last_letter_alias = {
        'A': 'Abyss', 'B': 'Blaze', 'C': 'Crash', 'D': 'Dragon', 'E': 'Edge', 
        'F': 'Flare', 'G': 'Grim', 'H': 'Hunter', 'I': 'Inferno', 'J': 'Jinx', 
        'K': 'Karma', 'L': 'Lunar', 'M': 'Mist', 'N': 'Nightmare', 'O': 'Oracle', 
        'P': 'Phreak', 'Q': 'Quake', 'R': 'Rogue', 'S': 'Storm', 'T': 'Thunder', 
        'U': 'Uprising', 'V': 'Vortex', 'W': 'Whisper', 'X': 'Xerox', 'Y': 'Yarn', 
        'Z': 'Zebra'
    }
    
    if not (first_name[0].isalpha() and last_name[0].isalpha()):
        return "Your name must start with a letter from A - Z."
    
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    
    first_letter = first_name[0].upper()
    last_letter = last_name[0].upper()

    return f"{first_letter_alias.get(first_letter, 'Unknown')} {last_letter_alias.get(last_letter, 'Unknown')}"



def cannons_ready(gunners):
    if all(value == 'aye' for value in gunners.values()):
        return "Fire!"
    else:
        return "Shiver me timbers!"
    




#7 kyu
def cheapest_quote(n):
    prices = [(40, 3.85), (20, 1.93), (10, 0.97), (5, 0.49), (1, 0.10)]
    
    total_price = 0
    for quantity, price in prices:
        if n >= quantity:
            bundles = n // quantity
            total_price += bundles * price
            n %= quantity
    
    return round(total_price, 2)

def pair_zeros(digits):
    result = []
    zero_count = 0
    
    for digit in digits:
        if digit == 0:
            zero_count += 1
        else:
            if zero_count % 2 == 1:
                result.append(0)
            result.append(digit)
            zero_count = 0
            
    if zero_count % 2 == 1:
        result.append(0)
        
    return result


def max_multiple(divisor, bound):
    return (bound // divisor) * divisor

def or_arrays(arr1, arr2, default=0):
    result = []
    length = max(len(arr1), len(arr2))
    
    for i in range(length):
        val1 = arr1[i] if i < len(arr1) else default
        val2 = arr2[i] if i < len(arr2) else default
        result.append(val1 | val2)
        
    return result



def numbers_with_digit_inside(x, d):
    numbers = [i for i in range(1, x + 1) if str(d) in str(i)]
    if not numbers:
        return [0, 0, 0]
    count = len(numbers)
    total_sum = sum(numbers)
    total_product = 1
    for num in numbers:
        total_product *= num
    return [count, total_sum, total_product]

#6 kyu
import random
import string

def password_gen():
    while True:
        password = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=random.randint(6, 20)))
        
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            password.isalnum()):
            return password
        


