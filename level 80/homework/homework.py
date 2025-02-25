#8 kyu

#1
def seats_in_theater(nCols, nRows, col, row):
    return (nRows - row) * (nCols - col + 1)


#2
def multiple_of_index(arr):
    return [arr[i] for i in range(len(arr)) if i == 0 and arr[i] == 0 or (i > 0 and arr[i] % i == 0)]


#3
def cookie(x):
    if isinstance(x, str):
        eater = "Zach"
    elif isinstance(x, (int, float)) and not isinstance(x, bool):  
        eater = "Monica"
    else:
        eater = "the dog"
    
    return f"Who ate the last cookie? It was {eater}!"



#4
def number_to_pwr(number, p): 
    result = 1
    for _ in range(p):
        result *= number
    return result




#5
def sc(floor):
    if floor <= 1:
        return ""
    elif floor >= 10:
        return "Aa~ " * 9 + "Pa!"
    elif floor <= 6:
        return "Aa~ " * (floor - 1) + "Pa! Aa!"
    else:
        return "Aa~ " * 6 + "Pa!"




#6
greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

def greek_comparator(word1, word2):
    return greek_alphabet.index(word1) - greek_alphabet.index(word2)


#7
def was_package_received_yesterday(tz_from, tz_to, start, duration):

    start_utc = start - tz_from

    end_utc = start_utc + duration
    end_local_time = end_utc + tz_to
    return end_local_time < start and (start - end_local_time > 0)




#no more 8 kyu

#7 KYU

