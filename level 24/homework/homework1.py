def calculate_average(numbers):
    if not numbers:
        return 0
    
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count

    return average


num1 = (1, 5, 9, 3, 2,)
calculate_average(num1)