import sys
from stats import word_count, char_count, char_stats

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")

    text = get_book_text(filepath)
    num_words = word_count(text)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    chars = char_count(text)
    stats = char_stats(chars)
    
    # Print ALL stats (not just top 10)
    for stat in stats:
        print(f"{stat['char']}: {stat['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()