import unittest

def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text

def main():
   print(get_book_text("./books/frankenstein.txt"))

class TestGetBookTextFunction(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(get_book_text(""), FileNotFoundError)

if __name__ == "__main__":
    main()
