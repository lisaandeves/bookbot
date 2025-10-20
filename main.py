import sys
from stats import count_words, count_characters, sort_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_text = get_book_text(sys.argv[1])
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_characters = sort_dictionary(character_count)
    
    print("============ BOOKBOT ============\n"
    f"Analyzing book found at {sys.argv[1]}...\n"
    "----------- Word Count ----------\n"
    f"Found {word_count} total words\n"
    "--------- Character Count -------")

    for item in sorted_characters:
        print(f"{item["char"]}: {item["num"]}")
main()