#1
def duplicate_encode(word):
    word = word.lower()  
    return "".join("(" if word.count(char) == 1 else ")" for char in word)



#2
def alphabet_position(text):
    return ' '.join(
        str(ord(char.lower()) - ord('a') + 1)
        for char in text if char.isalpha()
    )


#3
def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    x, y = 0, 0
    
    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
    
    return x == 0 and y == 0

