from stats import get_word_count
from stats import get_letter_count
from stats import get_sorted_dict
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    filecontents = None

    try:
        with open(filepath) as f:
            filecontents = f.read()
        return filecontents
    except FileNotFoundError:
        print(f"Error: file not found: {filepath}")
        sys.exit(1)


def main():
    path = sys.argv[1]
    book = get_book_text(path)
    count = get_word_count(book)
    char_count = get_letter_count(book)
    sorted_dict = get_sorted_dict(char_count)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_dict:
        char = item["char"]
        num = item["num"]

        if char.isalpha():
            print(f"{char}: {num}")
    
    print("============= END ===============")


main()