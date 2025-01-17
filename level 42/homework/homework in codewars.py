from preloaded import MORSE_CODE

def decode_morse(morse_code):

    words = morse_code.strip().split("   ")
    decoded_words = [
        ''.join(MORSE_CODE[char] for char in word.split(" ")) 
        for word in words
    ]

    return ' '.join(decoded_words)

def find_missing_letter(chars):

    for i in range(len(chars) - 1):

        if ord(chars[i + 1]) - ord(chars[i]) != 1:

            return chr(ord(chars[i]) + 1)
