#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and adds words. """    
    
    words = []
    for line in sys.stdin:
        words = words + line.split()
    
    words.sort()
    
    for word in words:
        print(word)

<|/ file ext=.py filename=wordcount.py |>