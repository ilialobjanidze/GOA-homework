# 1 codewars 
def sum_dig_pow(a, b):
    def is_eureka_number(n):

        total = sum(int(digit) ** (i + 1) for i, digit in enumerate(str(n)))

        return total == n
    eureka_numbers = [num for num in range(a, b + 1) if is_eureka_number(num)]
    return eureka_numbers



#2 codewars 
def order(sentence):

    if not sentence:
        return ""

    words = sentence.split()
    sorted_words = sorted(words, key=lambda word: int(''.join(filter(str.isdigit, word))))
    return " ".join(sorted_words)
 


print(sum_dig_pow(1,145))