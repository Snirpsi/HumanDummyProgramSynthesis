#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words or prints a list of words. """    
    words = enumerate('hello world')
    for index, word in enumerate(words):
        print(index, word)
    
