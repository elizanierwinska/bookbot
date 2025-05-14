# import unittest

def get_num_words(book):
    text = book.split()
    return len(text)

def get_letters(array):
    dict = {}
    for word in array:
        lowercase = word.lower()
        for l in lowercase:
            if l in dict:
                dict[l] += 1
            else:
                dict[l] = 1
    return dict
# class TestGetBookTextFunction(unittest.TestCase):
#     def test_null_input(self):
#         self.assertEqual(get_book_text(""), FileNotFoundError)