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

def sort_on(dictionary):
    return dictionary["num"]


"""
    Sort a dictionary by the number of times letters appeared in a book.

    Parameters:
        dictionary (dict): A dictionary where keys are letters and values are their frequency.

    Returns:
        list[dict]: A list of dictionaries with keys 'char' and 'num', sorted by 'num' in descending order.
"""
def sort_dict(letter_counts):
    sorted_list = []
    for letter in letter_counts:
        if letter.isalpha():
            sorted_list.append({
                "char": letter,
                "num": letter_counts[letter]
            })
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
