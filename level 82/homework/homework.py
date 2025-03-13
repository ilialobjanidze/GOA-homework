#1
def convert(number):
    return "".join([chr(int(number[e:e+2])) for e in range(0,len(number),2)])


#2
def calculate_total(subtotal, tax, tip):
    return round(sum([subtotal, subtotal*tax/100, subtotal*tip/100]), 2)

#3
def openOrSenior(data):
    return ["Senior" if person[0] >= 55 and person[1] > 7 else "Open" for person in data]



#4
def uncensor(infected, discovered):
    x = 0
    infected = list(infected)
    for e,c in enumerate(infected):
        if c == "*":
            infected[e] = discovered[x]
            x += 1
    return "".join(infected)


#5
def disemvowel(string):
    return "".join([ch for ch in string if ch not in "aeiouAEIOU"])


#6
def fizzbuzz(n):
    arr = []
    for i in range(1, n+1):
        if i % 3 == 0:
            if i % 5 == 0:
                arr.append("FizzBuzz")
            else:
                arr.append("Fizz")
        elif i % 5 == 0:
            arr.append("Buzz")
        else:
            arr.append(i)
    return arr



#7
def getTotal(costs, items, tax):
    return round(sum([costs[i] for i in items if i in costs]) * (1 + tax), 2)


#8
def solution(digits):
    m = max(digits)
    possibles = []
    for e, d in enumerate(digits[:-4]):
        if d == m:
            possibles.append(int(digits[e:e+5]))
    return max(possibles)



#9
def solve(st):
    chars = {char: abs(st.find(char) - st.rfind(char)) for char in st}
    return max(sorted(chars), key=lambda x: chars[x])



#10
def capitals(word):
    inds = []
    i = 0
    for l in word:
        if l.isupper():
            inds.append(i)
        i += 1
    return inds
    