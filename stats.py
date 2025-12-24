def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    text = text.lower()
    char_count = {}
    unique_chars = text
    for char in unique_chars:
        if char.isalpha():  # Only count letters
            char_count[char] = char_count.get(char, 0) + 1
    return char_count


def char_stats(d):
    stats = []
    for char, count in d.items():
        if char.isalpha():
            stats.append({"char": char, "num": count})

    def by_num(item):
        return item["num"]
    
    stats.sort(key=by_num, reverse=True)
    return stats