book_path = 'books/frankenstein.txt'

def main():
    text = get_book_path(book_path)
    print(text)


def get_book_path(path):
    with open(book_path) as f:
        return f.read()


def word_count():
    text = get_book_path(book_path)
    words = text.split()
    print(f"{len(words)} words are in the text")

word_count()