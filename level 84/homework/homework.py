
def decimal_to_binary(decimal_number):
    if decimal_number == 0:
        return "0"
    
    binary_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number = decimal_number // 2
    
    return binary_number






def binary_to_decimal(binary_number):
    decimal_number = 0
    binary_number = str(binary_number)
    
    binary_number = binary_number[::-1]
    
    for i in range(len(binary_number)):
        decimal_number += int(binary_number[i]) * (2 ** i)
    
    return decimal_number






def to_binary(b):
    binary_string = ""
    if b == 0:
        binary_string = "0"
    else:
        while b > 0:
            binary_string = str(b % 2) + binary_string
            b = b // 2  
    decimal_result = 0
    for i, digit in enumerate(binary_string):
        decimal_result += int(digit) * (10 ** (len(binary_string) - 1 - i)) 
    
    return decimal_result

