#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates words. """    
    words = []
    for word in open('words.txt'):
        words.append(word.strip())
    
    words.sort()
    
    for word in words:
        print(word)

<|/ file ext=.py source=github |>