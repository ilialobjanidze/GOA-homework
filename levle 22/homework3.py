def manual_len(liststr):
    count = 0
    for i in liststr:
        count += 1
    return count


liststr = [1, 2, 3, 4, 5]
result = manual_len(liststr)
print("Total elements is", result)
