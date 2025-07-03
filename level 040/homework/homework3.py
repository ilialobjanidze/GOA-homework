#1
numbers = [6, 14, 25, 1, 92]
result = list(map(lambda x: x * 5, numbers))
print(result)  


#2
strings = ["42", "913", "2", "441"]
result = list(map(int, strings))
print(result)  

#3
words = ["hello", "world", "python"]
result = list(map(lambda word: word + "!", words))
print(result)  


#4
import math

numbers = [18, 9, 441, 45]
result = list(map(math.sqrt, numbers))
print(result)  

numbers = [412, 14, 123, 3, 9]
result = list(map(lambda x: x % 2 == 0, numbers))
print(result)  