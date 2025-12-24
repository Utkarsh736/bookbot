def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    text = text.lower()
    char_count = {}
    unique_chars = set(text)
    for char in unique_chars:
        char_count[char] = text.count(char)
    return char_count