#1
def persistence(num):
    count = 0
    while num >= 10: 
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product
        count += 1
    return count

#2
def unique_in_order(sequence):
    result = []
    prev = object() 
    
    for item in sequence:
        if item != prev:
            result.append(item)
            prev = item
    
    return result


#3
def tribonacci(signature, n):
    if n == 0:
        return []
    if n < 3:
        return signature[:n]

    result = signature[:] 
    
    while len(result) < n:
        next_value = sum(result[-3:])
        result.append(next_value)
    
    return result

