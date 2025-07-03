#1
def welcome_person(name, city, state):
    full_name = " ".join(name)
    return f"Hello, {full_name}! Welcome to {city}, {state}!"

#2
def position(letter):
    position = ord(letter) - ord('a') + 1
    return f"Position of alphabet: {position}"


#3
def take(lst, n):
    return lst[:n]


#4 
def pillars(num_pillars, distance, width):
    if num_pillars == 1:
        return 0
    total_distance = (num_pillars - 1) * distance * 100 
    total_width = (num_pillars - 2) * width  
    return total_distance + total_width


#5 
def how_many_dalmatians(num_dogs):
    if num_dogs == 1:
        return "Wow! You got a dog!"
    elif num_dogs <= 3:
        return "That's a few dogs. Cute!"
    elif num_dogs <= 10:
        return "That's quite a pack of dogs!"
    else:
        return "Whoa! You have an entire kennel!"


#6
def apple(x):
    x = int(x) 
    if x ** 2 > 1000:
        return "It's hotter than the sun!!"
    else:
        return "Help yourself to a honeycomb Yorkie for the glovebox."



#7
def string_clean(text):
    return ''.join(char for char in text if not char.isdigit())


#8 
def array(string):
    parts = string.split(',')
    if len(parts) <= 2: 
        return None
    return ' '.join(parts[1:-1]) 




#9 
def swap_values(arr):
    arr[0], arr[1] = arr[1], arr[0]




#10
def same_case(char1, char2):
    if not (char1.isalpha() and char2.isalpha()):
        return -1
    if (char1.islower() and char2.islower()) or (char1.isupper() and char2.isupper()):  
        return 1
    return 0 



#11 
import math

def nearest_sq(n):
    root = int(math.sqrt(n)) 
    lower_square = root ** 2  
    higher_square = (root + 1) ** 2
    if abs(n - lower_square) <= abs(n - higher_square):
        return lower_square
    else:
        return higher_square
    


#12
def get_drink_by_profession(profession):
    profession = profession.lower()  
    if profession == "jabroni":
        return "Patron Tequila"
    elif profession == "school counselor":
        return "Anything with Alcohol"
    elif profession == "programmer":
        return "Hipster Craft Beer"
    elif profession == "bike gang member":
        return "Moonshine"
    elif profession == "politician":
        return "Your tax dollars"
    elif profession == "rapper":
        return "Cristal"
    else:
        return "Beer"
    

#13 codewars
def mystery():
    results = {
        'sanity': 'Hello'
    }
    return results

#14 
websites = []
websites.append("codewars")


#15 
class Sleigh:
    def authenticate(self, name, password):
        if name == "Santa Claus" and password == "Ho Ho Ho!":
            return True
        return False


#16 
def triple_trouble(str1, str2, str3):
    return ''.join(a + b + c for a, b, c in zip(str1, str2, str3))



#17
def elevator(left, right, call):
    if abs(left - call) < abs(right - call):
        return "left"
    elif abs(left - call) > abs(right - call):
        return "right"
    else:
        return "right"
    


#18
def find_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


#19
def whose_move(lastPlayer, win):
    if win:
        return lastPlayer
    else:
        return "white" if lastPlayer == "black" else "black"
    

#20
import math

def dating_range(age):
    if age <= 14:
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)
    else:
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)
    return f"{min_age}-{max_age}"


