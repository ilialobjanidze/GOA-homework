def sum_strings(a, b):
    a = a.lstrip('0') or '0'
    b = b.lstrip('0') or '0'

    i, j = len(a) - 1, len(b) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        
        total = digit_a + digit_b + carry
        carry = total // 10
        result.append(str(total % 10))
        
        i -= 1
        j -= 1

    return ''.join(result[::-1])
