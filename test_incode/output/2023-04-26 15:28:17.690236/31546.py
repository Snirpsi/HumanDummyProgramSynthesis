#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words. """    
    words = word_count(sys.argv[1])
    for word in words:
        print(word)
    
<|/ file ext=.py filename=wordcount.py |>