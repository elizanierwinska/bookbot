from stats import get_num_words
from stats import get_letters
from stats import sorted_list
from stats import sort_on

def get_book_text(filepath):
    text = ""
    with open(filepath) as f:
        text = f.read()
    return text 

def main():
    path = "books/frankenstein.txt"
    list = sorted_list(get_letters(get_book_text("./books/frankenstein.txt")))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    num_words = get_num_words(get_book_text("./books/frankenstein.txt"))
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list.sort(reverse=True, key=sort_on)
    for l in list:
        char = l['char']
        num = l['num']
        print(f'{char}: {num}')

if __name__ == "__main__":
    main()
