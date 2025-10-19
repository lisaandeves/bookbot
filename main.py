def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def main():
    print(f"Found {count_words(get_book_text("books/frankenstein.txt"))} total words")

main()