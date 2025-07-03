def manual_min(numbers):
    # თუ სია ცარიელია, ვაბრუნებთ None-ს
    if not numbers:
        return None

    min_value = numbers[0]

    for num in numbers:
        if num < min_value:
            min_value = num

    return min_value


listn = (136, 193, 913, 102, 91, 854)

min_number = manual_min(listn)
print(f"Your Minimal number is  {min_number}")
