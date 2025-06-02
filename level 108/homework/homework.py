def calculate(n1, n2, op):
    match op:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
            return n1 / n2  
    raise ValueError(f"Unsupported operator: {op}")

def calc(expr):
    if not expr:
        return 0
    arr = []
    
    for i in expr.split():

        try:
            num = int(i)
            arr.append(num)
        except ValueError:
            if len(arr) < 2:
                raise ValueError("Not enough operands")
            res = calculate(arr[-2], arr[-1], i)
            arr = arr[:-2]
            arr.append(res)
    if len(arr) != 1:
        raise ValueError("Invalid expression")
    return arr[0]
