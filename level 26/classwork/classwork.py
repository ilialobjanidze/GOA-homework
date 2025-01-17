def abbrev_name(name):
    first_name, last_name = name.split()
  
    return f"{first_name[0].upper()}.{last_name[0].upper()}"



def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    

    



def are_you_playing_banjo(name):

    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    


def better_than_average(class_points, your_points):
    average = sum(class_points) / len(class_points)
    return your_points > average



def accum(s):
    return '-'.join((ch.upper() + ch.lower() * i) for i, ch in enumerate(s))




def number(lines):
    return [f"{i + 1}: {line}" for i, line in enumerate(lines)]