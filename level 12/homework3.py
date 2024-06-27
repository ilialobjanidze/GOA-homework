total_sum = 0 

for num in range(1, 1001):
    total_sum += num
    if num >= 500 and num <= 599:
       continue

    print(total_sum)
