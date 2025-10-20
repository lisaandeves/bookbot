from stats import count_words, count_characters, sort_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_characters = sort_dictionary(character_count)

    print("============ BOOKBOT ============\n"
    "Analyzing book found at books/frankenstein.txt...\n"
    "----------- Word Count ----------\n"
    f"Found {word_count} total words\n"
    "--------- Character Count -------")

    for item in sorted_characters:
        print(f"{item["char"]}: {item["num"]}")

main()