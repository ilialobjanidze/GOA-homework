def going(n):
    current_factorial = 1  
    sum_factorials = 0 

    for k in range(1, n + 1):
        current_factorial *= k 
        sum_factorials += current_factorial  

    n_factorial = current_factorial

    u_n = sum_factorials / n_factorial
    
    return u_n