def is_valid_isbn10(isbn):

    if len(isbn) != 10:
        return False
    
    total = 0
    

    for i in range(9):
        if not isbn[i].isdigit():
            return False
        total += int(isbn[i]) * (i + 1)

    last_char = isbn[9]
    if last_char.isdigit():
        total += int(last_char) * 10
    elif last_char == 'X':
        total += 10 * 10
    else:
        return False
    return total % 11 == 0



def order_weight(strng):
    numbers = strng.split()
    

    def weight(number):
        return sum(int(digit) for digit in number) 
    
    sorted_numbers = sorted(numbers, key=lambda num: (weight(num), num))

    return " ".join(sorted_numbers)