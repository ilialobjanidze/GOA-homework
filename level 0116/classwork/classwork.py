#1
def dbl_linear(n):
    u = [1]
    i2 = i3 = 0

    for _ in range(n):
        val2 = 2 * u[i2] + 1
        val3 = 3 * u[i3] + 1

        next_val = min(val2, val3)
        u.append(next_val)

        if next_val == val2:
            i2 += 1
        if next_val == val3:
            i3 += 1

    return u[n]



#2
def strip_comments(text, markers):
    lines = text.split('\n')
    result_lines = []

    for line in lines:
        min_index = len(line) 

        for marker in markers:
            idx = line.find(marker)
            if idx != -1 and idx < min_index:
                min_index = idx

        clean_line = line[:min_index].rstrip()
        result_lines.append(clean_line)

    return '\n'.join(result_lines)
