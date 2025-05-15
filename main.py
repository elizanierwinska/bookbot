"""
Main entry point for Bookbot.

This script analyzes a text file (book) provided via the command line.
It prints the total number of words and the frequency of each alphabetic character,
sorted in descending order.

Usage:
    python3 main.py <path_to_book>
"""

import sys
from stats import get_num_words, get_letters, sort_dict

def get_book_text(filepath):
    text = ""
    try:
        with open(filepath) as f:
            text = f.read()
    except FileNotFoundError:
        print("File not found, please try different book")
        sys.exit(1)

    return text

def get_book_path():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return sys.argv[1]

def main():
    path = get_book_path()
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    letter_list = sort_dict(get_letters(book_text))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in letter_list:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()
