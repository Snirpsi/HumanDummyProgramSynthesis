#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates a list of words. """    
    words = open('words.txt').read().splitlines()
    words = list(filter(None, words))
    words.sort()
    print(words)
    
