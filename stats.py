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

def sorted_list(dict):
    list = []
    for d in dict:
        if d.isalpha():
            temp = {}
            temp["char"] = d
            temp["num"] = dict[d]
            list.append(temp)
    return list

def sort_on(dict):
    return dict["num"]
# class TestGetBookTextFunction(unittest.TestCase):
#     def test_null_input(self):
#         self.assertEqual(get_book_text(""), FileNotFoundError)