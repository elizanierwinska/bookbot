# import unittest

def get_num_words(book):
    text = book.split()
    return len(text)

# class TestGetBookTextFunction(unittest.TestCase):
#     def test_null_input(self):
#         self.assertEqual(get_book_text(""), FileNotFoundError)