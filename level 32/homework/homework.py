def spin_words(sentence):
    return ' '.join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])



def count_bits(n):
    return bin(n).count('1')


from collections import Counter

def duplicate_count(text):
    text = text.lower()
    counts = Counter(text)
    return sum(1 for value in counts.values() if value > 1)


def make_readable(seconds):

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    return f"{hours:02}:{minutes:02}:{secs:02}"