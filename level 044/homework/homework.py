def is_valid_IP(strng):
    octets = strng.split('.')
    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit() or (len(octet) > 1 and octet[0] == '0'):
            return False
        if not (0 <= int(octet) <= 255):
            return False

    return True



def run_length_encoding(s):
    if not s:
        return []

    result = []
    current_char = s[0]
    count = 1
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result.append([count, current_char])
            current_char = char
            count = 1
    result.append([count, current_char])

    return result



def variance(numbers):

    if len(numbers) == 0:
        return 0  

    mean = sum(numbers) / len(numbers)

    squared_diffs = [(x - mean) ** 2 for x in numbers]
    return sum(squared_diffs) / len(numbers)