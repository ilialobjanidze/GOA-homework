def longest_slide_down(pyramid):

    for row in range(len(pyramid) - 2, -1, -1):
        for col in range(len(pyramid[row])):
            pyramid[row][col] += max(pyramid[row + 1][col], pyramid[row + 1][col + 1])
    
    return pyramid[0][0]