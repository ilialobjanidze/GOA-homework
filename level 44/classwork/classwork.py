#1 codewars
def duplicate_encode(word):
    word = word.lower()  
    return "".join("(" if word.count(char) == 1 else ")" for char in word)

#2 codewars
def narcissistic(value):
    digits = [int(d) for d in str(value)]
    power = len(digits)  
    return sum(digit ** power for digit in digits) == value

#3 codewars
def multiplication_table(size):
    return [[(i + 1) * (j + 1) for j in range(size)] for i in range(size)]


print(duplicate_encode("iliala"))