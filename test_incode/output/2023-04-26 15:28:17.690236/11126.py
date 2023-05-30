#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words. """    
    words = open('words.txt').read().splitlines()
    for word in words:
        print(word)
