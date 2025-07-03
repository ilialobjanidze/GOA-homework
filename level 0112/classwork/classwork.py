#1
def triple_double(num1, num2):
    s1, s2 = str(num1), str(num2)
    for d in '0123456789':
        if d * 3 in s1 and d * 2 in s2:
            return 1 
    return 0



#2
def pyramid(n):
    return [[1] * i for i in range(1, n + 1)]



#3
def duplicate_encode(word):
    word = word.lower()  
    return "".join("(" if word.count(char) == 1 else ")" for char in word)