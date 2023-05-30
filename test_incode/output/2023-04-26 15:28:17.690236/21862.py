#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words and converts user input. """    
    words = input('Enter a list of words: ')
    words = words.split()
    
    for word in words:
        print('The word "{}" occurs {} times.'.format(word, words.count(word)))

<|/ file source=github ext=.py filename=wordcount.py |>