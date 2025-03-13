#1
def missing_values(arr):
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    for num, count in freq.items():
        if count == 1:
            x = num
        elif count == 2:
            y = num
    
    return x * x * y

#(ეს გაკეთებული მქონდა)
#2 ვერ გავიგე

#3
def greet_developers(lst):
    return [
        {**dev, 'greeting': f"Hi {dev['firstName']}, what do you like the most about {dev['language']}?"}
        for dev in lst
    ]



#4
def similarity(a, b):
    set_a, set_b = set(a), set(b)  
    intersection = len(set_a & set_b)  
    union = len(set_a | set_b)  
    return intersection / union if union != 0 else 0.0  

#5
def s2n(m, n):
    return sum(i**j for j in range(n + 1) for i in range(m + 1))



#6

def sect_sort(arr, start, length=0):
    if length == 0:
        arr[start:] = sorted(arr[start:])
    else:
        arr[start:start + length] = sorted(arr[start:start + length])
    return arr



#7
def elimination(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None



#8
def lamps(a):
    switches_pattern_1 = sum((a[i] != (i % 2)) for i in range(len(a)))
    switches_pattern_2 = sum((a[i] != ((i + 1) % 2)) for i in range(len(a)))
    return min(switches_pattern_1, switches_pattern_2)


#9
def gimme(arr):
    sorted_arr = sorted(arr)
    middle_value = sorted_arr[1]
    return arr.index(middle_value)


#10
def nickname_generator(name):
    if len(name) < 4:
        return "Error: Name too short"
    
    vowels = "aeiou"
    if name[2].lower() in vowels:
        return name[:4]
    else:
        return name[:3]
