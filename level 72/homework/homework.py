#1 
def bin_to_decimal(inp):
    return int (inp, 2)

#2 
def _if(value, func1, func2):
    if value:
        func1()
    else:
        func2()
        
    


#3 
def triple_trouble(one, two, three):
    return  "".join([one[i] + two[i] + three[i] for i in range(len(one))])


#4
def to_binary(n):
    binary_str = bin(n)[2:]
    
    return int(binary_str)

#5
def who_is_paying(name):
    if len(name) <= 2:
        return[name]
    else:
        return [name, name[:2]]
    

#6 
def solution(M1, M2, m1, m2, V, T):
    R = 0.082  # dm³·atm·K⁻¹·mol⁻¹
    T_kelvin = T + 273.15  # Convert temperature to Kelvin
    P_total = ((m1 / M1) + (m2 / M2)) * R * T_kelvin / V
    return P_total

#7 
def how_much_water(water, load, clothes):
    if clothes < load:
        return 'Not enough clothes'
    if clothes > 2 * load:
        return 'Too much clothes'
    return round(water * (1.1 ** (clothes - load)), 2)


#8 
class Dog:
    def __init__(self, breed):
        self.breed = breed

    def bark(self):
        return "Woof"
    

#9 
class Python:
    def __init__(self, name):
        self.name = name


#10
def next_item(sequence, item):
    try:
        index = sequence.index(item)  
        return sequence[index + 1]  
    except (ValueError, IndexError):  
        return Noneb
    


#11 codewars
def billboard(name, price=30):
    res = 0
    for i in name:
        res += price
    return res


#12 codewars
def isDigit(string):
    try:
        text = float(string)
        return True
    except ValueError:
        return False
    

#13 codewars
def number_to_string(num):
    return str(num)



#14 codewars
def multiply(a, b):
    return a * b


#15 codewars
def opposite(number):
  return number*-1

#16 codewars
def get_drink_by_profession(param):
    drinks = {"Jabroni": "Patron Tequila",
                "School Counselor": "Anything with Alcohol",
                "Programmer": "Hipster Craft Beer",
                "Bike Gang Member": "Moonshine",
                "Politician": "Your tax dollars",
                "Rapper": "Cristal"}
    return drinks[param.title()] if param.title() in drinks else "Beer"

#17 codewars
def leo(oscar):
    if oscar == 88: return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86: return "Not even for Wolf of wallstreet?!"
    elif oscar < 88: return "When will you give Leo an Oscar?"
    elif oscar > 88: return "Leo got one already!"

#18 codewars
def which_pizza(d1,price1,d2,price2):
    return d1 if (d1**2/price1) > (d2**2/price2) else d2


#19 codewars
def mouth_size(animal):
  return "small" if animal.lower() == "alligator" else "wide"


#20 codewars
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left