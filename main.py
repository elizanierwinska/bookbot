import unittest

def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text

def count_words(book):
    text = book.split()
    return len(text)
    

def main():
    num_words = count_words(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

class TestGetBookTextFunction(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(get_book_text(""), FileNotFoundError)

if __name__ == "__main__":
    main()
