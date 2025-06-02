def format_words(words):
    if not words:
        return ""
    filtered = [w for w in words if w]
    if not filtered:
        return ""
    if len(filtered) == 1:
        return filtered[0]
    if len(filtered) == 2:
        return f"{filtered[0]} and {filtered[1]}"
    return ", ".join(filtered[:-1]) + " and " + filtered[-1]



#2
def calc(expression):
    if not expression:
        return 0

    stack = []
    tokens = expression.split()

    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
        else:
            stack.append(float(token))

    return stack[0] if stack else 0



#3
def sort_sequence(sequence):
    subsequences = []
    temp = []
    for num in sequence:
        temp.append(num)
        if num == 0:
            subsequences.append(temp)
            temp = []

    for i in range(len(subsequences)):
        subseq = subsequences[i]
        subsequences[i] = sorted(subseq[:-1]) + [0]
    subsequences.sort(key=lambda x: sum(x[:-1]))

    result = []
    for subseq in subsequences:
        result.extend(subseq)

    return result
