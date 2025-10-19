from stats import count_words, count_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    character_count = count_characters(book_text)

    print(f"Found {word_count} total words")
    print(character_count)

main()