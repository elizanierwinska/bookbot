from stats import get_num_words, get_letters, sort_dict

dictionary = {
        "h": 1, 
        "e": 1,
        "l": 3,
        "o": 2,
        " ": 1,
        "w": 1,
        "r": 1,
        "d": 1,
        "!": 1,
        }

def test_get_num_words():
    assert get_num_words("Hello world!") == 2
    assert get_num_words("") == 0
    assert get_num_words("fdalj 2134 #$%@") == 3
    assert get_num_words("The family of Dashwood had been long settled in Sussex. Their estate was large, and their residence was at Norland Park, in the centre of their property, where, for any generations, they had lived in so respectable a manner as to engage the general good opinion of their surrounding acquiantance.") == 50

def test_get_letters():
    assert get_letters("Hello world!") == dictionary
    assert get_letters("") == {}
    assert get_letters("123 @@@") == {'1':1, '2':1, '3':1, ' ':1, '@':3}
    assert get_letters("Aaa BBB ccc!!!") == {'a': 3, ' ': 2, 'b': 3, 'c': 3, '!': 3}

def test_sort_dict():
    assert sort_dict(dictionary) == [{'char': 'l', 'num': 3}, {'char': 'o', 'num': 2}, {'char': 'h', 'num': 1}, {'char': 'e', 'num': 1}, {'char': 'w', 'num': 1}, {'char': 'r', 'num': 1}, {'char': 'd', 'num': 1}]
    assert sort_dict({}) == []
    assert sort_dict({'1':1, '2':1, '3':1, ' ':1, '@':3}) == []
    assert sort_dict({'a': 3, ' ': 2, 'b': 3, 'c': 3, '!': 3}) == [{"char": "a", "num": 3},{"char": "b", "num": 3},{"char": "c", "num": 3}]