#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over words and returns fruits. """    
    words = ["apple", "orange", "banana", "pear"]
    fruits = []
    for word in words:
        if word.lower() in ["apple", "orange", "banana", "pear"]:
            fruits.append(word)
    return fruits

<|/ file ext=.py source=github |>