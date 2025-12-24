from stats import word_count, char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = word_count(text)
    num_chars = char_count(text)
    print(f"Found {num_words} total words")
    print(num_chars)


main()
