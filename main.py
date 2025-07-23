import sys
from stats import count_characters, sort_character_counts, get_num_words

def get_book_text():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    # Read the book
    with open(book_path, 'r', encoding='utf-8') as f:
        book_text = f.read()
    return book_text

def main():
    # (Assuming book_text contains the book as a string)
    text = get_book_text()
    char_counts = count_characters(text)
    sorted_chars = sort_character_counts(char_counts)

    print("============ BOOKBOT =============")
    print("Analyzing book found at books/frankenstein.txt...")

    # Word Count section
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text())} total words")  # Assuming you calculated this earlier

    # Character Count section
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()