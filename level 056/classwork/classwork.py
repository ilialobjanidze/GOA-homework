# 8 KYU
# 1 codewars
def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    return n * m

# 2 codewars
def make_upper_case(s):
    return s.upper()
# 3 codewars
def find_needle(haystack):
    index = haystack.index("needle")
    return f"found the needle at position {index}"

# 4 codewars
def invert(lst):
    return [-num for num in lst]

# 5 codewars
def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers) 

# 6 codewars
def smash(words):
    return ' '.join(words)

# 7 codewars
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result

# 8 codewars
def hero(bullets, dragons):
    return bullets >= dragons * 2

# 9 codewars
def count_positives_sum_negatives(arr):
    if not arr:  
        return []
    
    positive_count = 0
    negative_sum = 0
    
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_sum += num
    
    return [positive_count, negative_sum]

# 10 codewars
def dna_to_rna(dna):
    return dna.replace('T', 'U')

