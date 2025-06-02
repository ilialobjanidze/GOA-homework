
#1
def most_frequent(arr):
    from collections import Counter
    count = Counter(arr)
    max_freq = max(count.values())
    return max([num for num, freq in count.items() if freq == max_freq])



#2
def more_zeros(s):
    seen = set()
    result = []
    
    for char in s:
        if char in seen:
            continue
        seen.add(char)
        binary = bin(ord(char))[2:]
        if binary.count("0") > binary.count("1"):
            result.append(char)
            
    return result


#3
def pos_average(s):
    list1 = s.split(", ")
    l = len(list1)
    sum = 0
    all_char = 0
    
    for i in range(l):
        for x in range(i + 1, l):
            for a, b in zip(list1[i], list1[x]):
                all_char += 1
                if a == b:
                    sum += 1
    
    return sum / all_char * 100
```