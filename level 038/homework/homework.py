

#1
tuplesl = [(4, 9), (2, 1), (3, 2)]
sortedl = sorted(tuplesl, key=lambda s: s[1])


#2
numbers = [9, 14, 3, 32]
squares = list(map(lambda p: p**2, numbers))



#3
words = ["apple", "dog", "cat", "banana"]
filtered_words = list(filter(lambda word: len(word) >= 4, words))
print(filtered_words) 

#4
strings = ['hello', 'world']
upper_strings = list(map(lambda i: i.upper(), strings))

#5
numbers = [942, 125, 91]
added_five = list(map(lambda m: m + 5, numbers))
print(added_five)  

#6
words = ['apple', 'banana', 'cherry']
start_words = list(map(lambda word: 'start' + word[0], words))
print(start_words)  


#7
numbers = [91, 42, 9, 21, 32, 88]
even_numbers = list(filter(lambda g: g % 2 == 0, numbers))
print(even_numbers)  



#8
words = ['apple', 'banana', 'Cat', 'House']
a_words = list(filter(lambda word: word.lower().startswith('A'), words))
print(a_words) 


#9
numbers = [-913, 3, -81, 6, -83, 4]
non_negative = list(filter(lambda j: j >= 0, numbers))
print(non_negative) 
