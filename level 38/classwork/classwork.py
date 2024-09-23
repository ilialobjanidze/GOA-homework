  #1
def add_one(x):
    return x + 1
numbers = [1, 2, 3, 4, 5]
result = list(map(add_one, numbers))

print(result)
  
 #2
def create_sentence(*words):
    return ' '.join(words) 
sentence = create_sentence('This', 'is', 'a', '7', 'Word', 'sentence', '!')
print(sentence)

#3
def filter_bad_words(sentence):
    bad_words = ['ზარმაცი', 'მეზარება', 'უსაქმური', 'დავიღალე']
    
    filtered_sentence = ' '.join([word for word in sentence.split() if word not in bad_words])
    return filtered_sentence
sentence_with_bad_words = "მე ზარმაცი ვარ და მეზარება მუშაობა"
filtered_sentence = filter_bad_words(sentence_with_bad_words)
print(filtered_sentence)


#4
def add_squares(list1, list2):
    result = list(map(lambda x, y: x + y**2, list1, list2))
    return result
list1 = [1, 2, 3]
list2 = [4, 5]
result = add_squares(list1, list2)

print(result)


