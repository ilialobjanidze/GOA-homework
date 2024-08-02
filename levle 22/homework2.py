def manual_max(numbers):

    if not numbers:
        return None

    max_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value



numbers_list = [931, 324, 813, 412, 83, 75, 931,]
max_number = manual_max(numbers_list)
print(f"Your Max Value Is-{max_number}")
