#1 codewars
def string_to_array(string):

    if string == "":
        return ['']

    return string.split() 


#2 codewars
def check(seq, elem):
    return elem in seq

#3 codewars
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]
    

#4 codewars
def count_sheep(n):
    return ''.join([f"{i} sheep..." for i in range(1, n + 1)])

#5 codewars
def quarter_of(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    elif 10 <= month <= 12:
        return 4
    

#6 codewars
def remove_exclamation_marks(s):
    return s.replace("!","")

#7 codewars
def get_volume_of_cuboid(length, width, height):
    return length * width * height

#8 codewars
def area_or_perimeter(length, width):
    if length == width:
        return length * width
    else:
        return 2 * (length + width)


#9 codewars 
def other_angle(angle1, angle2):
    return 180 - (angle1 + angle2)

#10 codewars
def set_alarm(employed, vacation):
    return employed and not vacation


#11 codedwars
def sum_mix(arr):
    return sum(int(x) for x in arr)


#12 codewars
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]


#13 codewars
def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)


#14 codewars
def reverse_words(s):
    return ' '.join(s.split()[::-1])

#15 codewars
def hoop_count(n):
    if n >= 10:
        return "Great, now move on to tricks"
    else:
        return "Keep at it until you get it"


#16 codewars
def switch_it_up(n):
    num_words = {
        0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
        5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    return num_words[n]

#17 codewars
def square(x):
    return x ** 2

#18 codewars
def remove_every_other(arr):
    return arr[::2]

#19 codewars
def who_is_paying(name):
    result = []
    result.append(name)
    if len(name) > 2:
        result.append(name[0]+name[1])
    return result


#20 codewars
def points(games):
    result = 0
    for i in games:
        j = i.split(':')
        if j[0] > j[1]:
            result+=3
        elif j[0] == j[1]:
            result += 1
    return result

#21 codewars
def positive_sum(arr):
    return max(0,sum([i for i in arr if i > 0]))

#22 codewars
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start-blue_pulled)/(blue_start-blue_pulled+red_start-red_pulled)

#23 codewars
def repeat_str(repeat, string):
    return string*repeat

#24 codewars
def make_negative( number ):
    return number*-1 if number > 0 else number

#25 codewars
def remove_char(s):
    return s[1:-1]

