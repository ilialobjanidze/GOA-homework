def alphabet_position(text):
    return ' '.join(
        str(ord(char.lower()) - ord('a') + 1)
        for char in text if char.isalpha()
    )