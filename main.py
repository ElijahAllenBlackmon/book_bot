book_path = 'books/frankenstein.txt'

def main():
    text = get_book_path(book_path)
    print(text)


def get_book_path(path):
    with open(book_path) as f:
        return f.read()

main()